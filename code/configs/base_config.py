class BaseConfig(object):

    def __init__(self):

        self.app_name = ''
        self.logname = ''
        self.config_outname = 'BaseConfig'

    def build_from_json(self,json_config):
        config_section = json_config[self.config_outname]
        for key,value in config_section.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self