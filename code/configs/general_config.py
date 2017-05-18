from configs.base_config import BaseConfig


class GeneralConfig(BaseConfig):
    def __init__(self):

        self.app_name = 'AutomatedModeling'
        self.log_name = ''
        self.loglevel = 'ERROR'

        self.mode = {}
        self.joins = {}
        self.variable_addition_dict = {}
        self.save_frame = False

        self.config_outname = 'GeneralConfig'
