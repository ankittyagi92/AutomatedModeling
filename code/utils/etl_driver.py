import os
import json
import pandas as pd
import traceback
import logging
import utils.logs_driver as logs_driver

import configs.general_config as general_config
import configs.io_config as io_config


class ETLdriver(object):
    def __init__(self, config_file):

        self._load_json(config_file)

        #base conf needs to be setup before other confs
        self.general_conf = self._build_config()
        self.log = self._setup_log()
        self.log.info('Log statement of etl_driver')

    def _load_json(self, config_file):

        self.config_file = config_file

        with open(config_file, 'r') as infile:
            self.json_config = json.load(infile)

    def _build_config(self):

        #self.log.info("Setting attributes from json_conifg")
        return general_config.GeneralConfig().build_from_json(self.json_config)

    def _setup_log(self):

        return logs_driver.get_log(self)

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
            print("Mode: ", mode)
            frame = self.call_mode(frame, mode)
        self.log.info("Transforms complete")
        if self.general_conf.save_frame:
            self.save_transformed_frame(frame)
        print(frame)
        print(header)
        self.log.info('Running complete without problems')

    def _load_data(self):
        io_conf = io_config.IOConfig().build_from_json(self.json_config)
        extension = os.path.splitext(io_conf.input_file)[1]

        if extension == '.csv':
            #df = spark.read.csv(io_conf.input_dir + io_conf.input_file)
            #head = colnames(df)
            df = pd.read_csv(io_conf.input_dir + io_conf.input_file)
            head = list(df)
            return df, head
        else:
            print("Currently only local csv enabled")
            return None, None

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
            print(module_name, transform_func)
        return frame

    def save_transformed_frame(self, frame):
        pass