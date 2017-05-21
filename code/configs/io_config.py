from configs.base_config import BaseConfig


class IOConfig(BaseConfig):
    def __init__(self):
        self.input_dir = ''
        self.input_file = ''
        self.parquet = False
        self.save_frame = True
        self.output_dir = ''
        self.output_file = ''
        self.log_name = ''
        self.config_outname = 'IOConfig'