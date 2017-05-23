#add functionality to quiet the stdout and send logs to a file given in commandline
from optparse import OptionParser
import sys
import os
import utils.etl_driver as etl_driver
from configs.spark_config import SparkConfig
from configs.io_config import IOConfig


class PysparkDriver(etl_driver.ETLdriver):

    def __init__(self, config_file):

        super().__init__(config_file)

def parse_commandline_args():

    opt = OptionParser()
    opt.add_option('-c', '--config', dest = 'config', help = 'path to the config file to be used')
    return opt.parse_args()

if __name__ == '__main__':

    options, args = parse_commandline_args()

    print("<<<<<<<<<<<<<<<<<Starting the framework>>>>>>>>>>>>")
    print("<<<<With the following command line parameters>>>>>")
    print('Options:', options)
    print('Args:', args)

    if options.config:
        driver = PysparkDriver(options.config)
        attr = vars(driver)
        driver.run()

