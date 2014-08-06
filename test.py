#!/usr/bin/env python3

from collections import defaultdict

from outdetect.datamodel.data import Data
from outdetect.algorithm.HourDetect import HourDetect
from outdetect.utils.log import LOG
from outdetect.utils.excepts import DataFormatError

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
    log.info('Successful in setting config')

    od.run()
    log.info('End running')

def dataTest():
    log = LOG('log/test.log')
    d = {'20130723': [0.1,1,1,3], '20130721': [2,0,1,3], '20130722': [3,2,5.1,2]}
    try:
        a = Data(d)
        a.set({'20130712': [0,1,1,2]}, True)
        a.delete('20130723')
        print(a)
    except DataFormatError as e:
        log.error(e)

if __name__ == '__main__':
    main('test/data')
    dataTest()
