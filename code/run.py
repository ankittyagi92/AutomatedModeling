#add functionality to quiet the stdout and send logs to a file given in commandline
from optparse import OptionParser
import sys
import os
import utils.etl_driver as etl_driver

class PysparkDriver(etl_driver.ETLdriver):
    def __init__(self, config_file):
        super().__init__(self, config_file)
        print(config_file)
        self.log.info('log statement of pysparkdriver')

def parse_commandline_args():
    opt = OptionParser()
    opt.add_option('-c', '--config', dest = 'config', help = 'path to the config file to be used')
    return opt.parse_args()

if __name__ == '__main__':
    options, args = parse_commandline_args()
    '''if options.config:
        driver = PysparkDriver(options.config)
        driver.run()
    '''
    print(options)
    print(args)

