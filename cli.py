#!/usr/bin/env python3

import argparse
import subprocess
import sys
import os

from outdetect.utils.log import LOG

class CommandLine:
    '''
    Command line to control outlier detection framework.

        usage: cli.py [-h] [-n NEW_ALGORITHM] [-c]

        optional arguments:
          -h, --help            show this help message and exit
          -n NEW_ALGORITHM, --new NEW_ALGORITHM
                                create a new algorithm for outlier detecting
          -c, --clear           WARNING!!!: clear all log files
    '''
    def __init__(self):
        self.log = LOG(logfile='log/CommandLine.log')

        parser = argparse.ArgumentParser()

        # parser.add_argument('-t', '--top', dest='top', type=int, default=10, help="top number for feedback")
        # parser.add_argument('-f', '--file', dest='file', nargs='*', help="feedback file or files")

        parser.add_argument('-n', '--new', dest='new_algorithm', help="create a new algorithm for outlier detecting")
        parser.add_argument('-c', '--clear', dest='clear', action="store_true", default=False, help="WARNING!!!: clear all log files")
        self.args = parser.parse_args()

        if self.args.clear:
            self.clear()

        if self.args.new_algorithm is not None:
            self.new()

    def clear(self):
        proc = subprocess.call('rm log/*', shell=True)
        try:
            assert proc is 0
        except AssertionError:
            self.log.error('Fail to clear all log files in document log/*')
            sys.exit()

    def new(self):
        self.log.info('Start creating algorithm template')
        name = ''.join(list(map(lambda x: x.capitalize(), self.args.new_algorithm.strip().split())))
        try:
            assert not os.path.isfile('outdetect/algorithm/' + name + '.py')
        except AssertionError:
            self.log.error('File ' + name + '.py has already existed')
            sys.exit()

        shell = 'sed "s/\${ProjectName}/' + name + '/g" outdetect/template/algorithm.py.tmpl > outdetect/algorithm/' + name + '.py'
        proc = subprocess.call(shell, shell=True)
        try:
            assert proc is 0
        except AssertionError:
            self.log.error('Create template process error')
            sys.exit()

        self.log.info('Successful in creating outdetect/algorithm/' + name + '.py')

if __name__ == '__main__':
    cmd = CommandLine()
