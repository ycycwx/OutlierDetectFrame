#!/usr/bin/env python3

import sys
import os
from collections import defaultdict

from outdetect.datamodel.data import Data
from outdetect.algorithm.HourDetect import HourDetect
from outdetect.utils.log import LOG

def main(data):
    log = LOG('log/test.log')
    dataSet = defaultdict(list)
    for line in open(data, 'r'):
        dataSet[line.strip().split(',')[0][:-3]].append(line.strip().split(',')[1])

    dat = Data(dataSet)
    dat.normalize()

    log.info('Data normalizing phrase complete')

    od = HourDetect(dat)

    config = {}
    config['target']     = 'visitUser'
    config['dist']       = 'euclidean'
    config['threshold']  = 0.25
    config['norm_range'] = 0.5
    od.set_conf(config)

    od.run()

if __name__ == '__main__':
    main('test/data')
