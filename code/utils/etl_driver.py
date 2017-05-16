import os
import json
import logging
import utils.logs_driver as logs_driver

import configs.base_config as base_config


class ETLdriver(object):
    def __init__(self, config_file):
        #self.log.info('log statement of etl_driver')

        self._load_json(config_file)
        self._build_config()

    def _load_json(self, config_file):
        print("Reading config file")
        self.config_file = config_file

        with open(config_file, 'r') as infile:
            self.json_config = json.load(infile)

    def _build_config(self):
        print("Setting attributes from json_conifg")
        return base_config.BaseConfig().build_from_json(self.json_config)


    def _setup_log(self,json_config):

        log_dir = logs_driver.get_log_dir()
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        log_name = log_dir + 'run_' + self.app_name + '.log'

        logging.basicConfig(filename = log_name,
                            filemode = 'w',
                            level = logging.INFO)
        self.log = logging

