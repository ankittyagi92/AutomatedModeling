import os
import json
import traceback
import logging
import utils.logs_driver as logs_driver

import configs.base_config as base_config


class ETLdriver(object):
    def __init__(self, config_file):

        self._load_json(config_file)

        #base conf needs to be setup before other confs
        self.base_conf = self._build_config()
        self.log = self._setup_log()
        self.log.info('Log statement of etl_driver')

    def _load_json(self, config_file):

        self.config_file = config_file

        with open(config_file, 'r') as infile:
            self.json_config = json.load(infile)

    def _build_config(self):

        #self.log.info("Setting attributes from json_conifg")
        return base_config.BaseConfig().build_from_json(self.json_config)

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
        #frame, header = self.load_data()
        #header.show()
        #frame.show(2)
        self.log.info('Running complete without problems')
