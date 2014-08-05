#!/usr/bin/env python3

import sys
import os
from ..datamodel.data import Data

class OutlierBasic:
    """
    Base class for outlier-detect. All programs must inherit from this class.
    """
    def __init__(self, data):
        '''
        Data Format: An instance of Data => Data()
            [($key, $value), ($key, $value), ... , ($key, $value)]
            key    =>  string
            value  =>  float
        '''
        self._data = data

    def set_conf(self, conf):
        """
        Set configurations

        Overwrite set_conf(conf) function in child-class
        """
        raise NotImplementedError('Overwrite "set_conf(conf)" function in child-class')

    def get_data(self):
        return self._data

    def outlier_detection(self):
        return self.run()

    def run(self):
        '''
        Run Outlier-Detect Program

        Overwrite run() function in child-class
        '''
        raise NotImplementedError('Overwrite "run()" function in child-class')

if __name__=='__main__':
    data = Data([('20130101_01',1), ('20130201_03',2)])

    od = OutlierBasic(data)
    conf = {'target':'visitUser', 'dist':'euclidean', 'norm_range':0.5}
    od.set_conf(conf)
    od.run()
