from configs.base_config import BaseConfig

class SparkConfig(BaseConfig):
    def __init__(self):
        super().__init__()

        self.executor_memory = '2g'
        self.dynamicAllocation_enabled = False
        self.dynamicAllocation_initialExecutors = 2
        self.dynamicAllocation_executoIdleTimeout = 120
        self.dynamicAllocation_minExecutors = 2
        self.dynamicAllocation_maxExecutors = 10
        self.executor_instances = 2
        self.executor_env = {}
        self.config_outname = 'SparkConfig'
