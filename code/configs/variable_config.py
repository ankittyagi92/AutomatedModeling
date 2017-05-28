from configs.base_config import BaseConfig

class VariableConfig(BaseConfig):
    def __init__(self):
        super().__init__()

        self.variable_file = 'code/variables.json'
        self.config_outname = 'VariableConfig'
