from configs.base_config import BaseConfig


class IOConfig(BaseConfig):
    def __init__(self):
        self.parquet = ''
        self.save_output = False
        self.log_name = ''
        self.loglevel = 'ERROR'
        self.config_outname = 'IOConfig'