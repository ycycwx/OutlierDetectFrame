#!/usr/bin/env python3

from ..datamodel.data import Data

class OutlierBasic:
    '''
    Base class for outlier-detect. All programs must inherit from this class.
    '''
    def __init__(self, data):
        '''
        Data Format: An instance of Data => Data()
            [($key, $value), ($key, $value), ... , ($key, $value)]
            key    =>  string
            value  =>  float
        '''
        self._data = data

    def set_conf(self, conf):
        '''
        Set configurations

        Overwrite set_conf(conf) function in child-class
        '''
        raise NotImplementedError('Overwrite "set_conf(conf)" function in child-class')

    def get_data(self):
        '''
        Get data in OutlierBasic
        '''
        return self._data

    def run(self):
        '''
        Run Outlier-Detect Program

        Overwrite run() function in child-class
        '''
        raise NotImplementedError('Overwrite "run()" function in child-class')

    def outlier_detection(self):
        '''
        The same as run()

        Return result in self.run()
        '''
        return self.run()
