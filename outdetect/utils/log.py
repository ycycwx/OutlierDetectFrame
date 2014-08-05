#!/usr/bin/env python3

import logging

class LOG:
    '''
    Log handler in outlier detection
    {
        Console: Level INFO
        LogFile: Level WARNING
    }

    Format example
    {
        [2014-08-03 16:17:39,363] (ERROR) - log.py:49 : error
        [2014-08-03 16:17:39,364] (WARNING) - log.py:52 : warn
        [2014-08-03 16:17:39,364] (INFO) - log.py:55 : info
    }
    '''
    def __init__(self, \
            logfile = 'out.log', \
            format  = '[%(asctime)s] (%(levelname)s) - %(filename)s:%(lineno)d : %(message)s', \
            name    = '' \
            ):
  
        log = logging.getLogger(name)

        log_formatter = logging.Formatter(format)

        # comment this to suppress console output
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_formatter)
        stream_handler.setLevel(logging.INFO)
        log.addHandler(stream_handler)

        file_handler_info = logging.FileHandler(logfile, mode='a')
        file_handler_info.setFormatter(log_formatter)
        file_handler_info.setLevel(logging.WARNING)
        log.addHandler(file_handler_info)

        # file_handler_error = logging.FileHandler(LOG_FILE_ERROR, mode='w')
        # file_handler_error.setFormatter(log_formatter)
        # file_handler_error.setLevel(logging.ERROR)
        # log.addHandler(file_handler_error)

        log.setLevel(logging.INFO)

    def critical(self, msg):
        logging.critical(msg)

    def error(self, msg):
        logging.error(msg)

    def warn(self, msg):
        logging.warn(msg)

    def info(self, msg):
        logging.info(msg)

    def debug(self, msg):
        logging.debug(msg)

def main():
    log = LOG()
    log.error('error')
    log.warn('warn')
    log.info('info')
    log.debug('debug')

if __name__ == '__main__':
    main()
