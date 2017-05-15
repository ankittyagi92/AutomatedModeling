from configs.base_config import BaseConfig

class SparkConfig(BaseConfig):
    def __init__(self):
        super().__init__()

        self.executor_memory = '2g'
        self.dynamicAllocation_enabled = True
        self.config_outname = 'SparkConfig'
