import os
import json
import pandas as pd
import traceback
import logging
import importlib
import utils.logs_driver as logs_driver
import utils.config_builder as config_builder
import utils.filepath as filepath
import utils.var_builder as var_build

import configs.general_config as general_config
import configs.io_config as io_config
import configs.spark_config as spark_config
import configs.variable_config as var_config

from pyspark.sql import SparkSession


class ETLdriver(object):
    def __init__(self, config_file):

        self._load_json(config_file)

        #settting up confs
        self.io_conf = io_config.IOConfig().build_from_json(self.json_config)
        self.general_conf = general_config.GeneralConfig().build_from_json(self.json_config)
        self.spark_conf = spark_config.SparkConfig().build_from_json(self.json_config)
        self.var_conf = var_config.VariableConfig().build_from_json(self.json_config)
        self.log = self._setup_log()
        self.spark = self._setup_contexts()
        self.log.info('Log statement of etl_driver')

    def _load_json(self, config_file):

        self.config_file = config_file

        with open(config_file, 'r') as infile:
            self.json_config = json.load(infile)

    def _setup_log(self):

        return logs_driver.get_log(self)

    def _setup_contexts(self):

        self.log.info("Setting up spark context")


        conf = config_builder.build_spark_config(self.spark_conf, self.var_conf, self.log)

        spark = SparkSession.builder.appName(self.general_conf.app_name)\
                                    .config(conf = conf).getOrCreate()

        self.log.info("SparkSession created")

        return spark

    def run(self):
        try:
            self.run_framework()
        except Exception as ex:
            self.log.info('Error encountered: %s' %str(ex))
            self.log.info(str(traceback.format_exc()))
            self.log.info("\n")

    def run_framework(self):
        self.log.info('Running the framework')
        self.log.info("Reading Data")
        frame, header = self._load_data()
        self.log.info("Data read, running transforms")
        for mode in self.general_conf.mode:
            self.log.info("Mode: ", mode)
            frame = self.call_mode(frame, mode)
        self.log.info("Transforms complete")
        if self.io_conf.save_frame:
            self.save_transformed_frame(frame)
        frame.show(2)
        self.log.info('Running complete without problems')

    def _load_data(self):

        extension = os.path.splitext(self.io_conf.input_file)[1]

        if extension == '.csv':
            df = self.spark.read.csv(self.io_conf.input_dir + self.io_conf.input_file, header = True)
            head = list(df)
            return df, head
        elif(extension == '.parquet'):
            df = self.spark.read.load(self.io_conf.input_dir + self.io_conf.input_file)
            head = df.columns
            return df, head

    def call_mode(self, frame, mode):

        self.log.info("Starting mode: %s" % mode )

        if hasattr(self, mode):
            frame = getattr(self,mode)(frame)
        else:
            self.log.info("Unable to identify mode %s" %mode)
            raise AttributeError(mode)
        return frame

    def add_variables(self,frame):

        for module_name, transform_func in self.general_conf.variable_addition_dict.items():

            self.log.info("Module name: %s, Transformation Function: %s" % (module_name, transform_func))

            mod = importlib.import_module(module_name)

            if hasattr(mod, transform_func):
                add_frame_rows = frame.rdd.map(getattr(mod, transform_func))

            if self.io_conf.sampling_ratio:
                frame = self.spark.createDataFrame(add_frame_rows,
                                                   samplingRatio = self.io_conf.sampling_ratio)
            else:
                frame = self.spark.createDataFrame(add_frame_rows)
        return frame

    def save_transformed_frame(self, frame):

        output_path = self.io_conf.output_dir
        self.log.info('Writing frame as csv to path : %s' %output_path)
        if not os.path.isdir(output_path):
            os.makedirs(output_path)
        output_name = self.io_conf.output_file
        frame.write.csv(output_path + output_name, mode = 'overwrite')
        self.log.info('File write done')
        return