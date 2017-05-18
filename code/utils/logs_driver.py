import os
import logging

def get_log(self):
    '''dynamically implement this later
    '''
    #return os.getcwd() + "/logs"


    log_dir = os.getcwd() + "/logs/"
    print(log_dir)
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    if self.general_conf.log_name == '':
        log_name = 'run_' + self.general_conf.app_name + '.log'
    else:
        log_name = self.general_conf.log_name + '.log'

    logging.basicConfig(filename = log_dir + log_name,
                        filemode ='w',
                        format = '%(asctime)s %(message)s')

    log_obj = logging.getLogger(log_name)

    if self.general_conf.loglevel == 'INFO':
        log_obj.setLevel(logging.INFO)
    elif self.general_conf.loglevel == 'DEBUG':
        log_obj.setLevel(logging.DEBUG)
    elif self.general_conf.loglevel == 'ERROR':
        log_obj.setLevel(logging.ERROR)
    elif self.general_conf.loglevel == 'WARNING':
        log_obj.setLevel(logging.WARNING)

    return log_obj