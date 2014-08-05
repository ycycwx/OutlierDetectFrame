#!/usr/bin/env python

# print client.getTableNames()
# print client.getRow('shmcc_stat_hour', 'stat_corrected_2013-07-01_00', None)
# print client.getRowWithColumns('shmcc_stat_hour', 'stat_corrected_2013-07-01_00', 'stat_cf:ratio', None)
# print client.get('shmcc_stat_hour', 'stat_corrected_2013-07-01_00', 'stat_cf:ratio', None)
# print client.get('shmcc_stat_hour', 'stat_avgSessionDuring_2013-07-31_17', 'stat_cf:during', None)
# print client.get('shmcc_stat_hour', '', 'stat_cf:during', None)
# print client.get('test', 'A', 'cf:question', None)

import sys
sys.path.append('/home/hdfs117/xiaoi/py')
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import * 
from datetime import datetime, timedelta, date

def getHbase(end_time, target, column, table=None, length=None):
    '''
        end_time    = '2013-07-30'
        target      = 'stat_avgSessionDuring'
        column      = 'stat_cf:during'
        table       = 'shmcc_stat_hour'
        length      = 1
    '''

    end = datetime.strptime(end_time, '%Y-%m-%d')

    # month = '2013-07'
    if table is None: table = 'shmcc_stat_hour'
    if length is None: length = 1
    # target = 'stat_avgSessionDuring'
    # column = 'stat_cf:during'
    # write_file = month + '_' + target

    transport = TSocket.TSocket('localhost', 9090)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Hbase.Client(protocol)

    transport.open()

    scan = TScan()
    scanner = client.scannerOpenWithScan(table, scan, None)

    # scanner = client.scannerOpen(table, "", column, None)
    
    # for i in range(100):
    #     print client.scannerGetList(scanner, 1)

    dict = {}

    for i in range(length):
        for j in range(24):
            try:
                # date = month
                # date += "-%02d_%02d" %(i, j)
                dateTime = end - timedelta(days=i)
                date = dateTime.strftime('%Y-%m-%d')
                date += '_%02d' %j
                # print(date)
                genTarget = "%s_%s" %(target, date)
                getValue = client.get(table, genTarget, column, None)
                # print(getValue)
                strValue = str(getValue[0]).split("=")[-1].split('\'')[1]
                dict[date] = float(strValue)
                # print '%s:\t%s' %(date, client.get(table, genTarget, 'stat_cf:during', None))
            except:
                dict[date] = 0.0

    # for i in range(1, 32):
    #     for j in range(24):
    #         try:
    #             date = month
    #             date += "-%02d_%02d" %(i, j)
    #             # print(date)
    #             genTarget = "%s_%s" %(target, date)
    #             getValue = client.get(table, genTarget, column, None)
    #             # print getValue
    #             strValue = str(getValue[0]).split("=")[-1].split('\'')[1]
    #             dict[date] = strValue
    #             # print '%s:\t%s' %(date, client.get(table, genTarget, 'stat_cf:during', None))
    #         except:
    #             dict[date] = 0.0

    # for key in dict:
    #     print("%s, %s" %(key, dict[key]))
    
    # file = open(write_file, 'w')
    # for key in dict:
    #     text = "%s,%s\n" %(key, dict[key])
    #     file.write(text)
    # file.close()
    
    # print client.scannerGetList(scanner, 100)
    # print client.scannerOpenWithStop('shmcc_stat_hour', "", "", 'stat_cf:*', None)
    # print client.get('shmcc_stat_hour', 'stat_avgSessionDuring_2013-07-01_00', 'stat_cf:during', None)
    # client.scannerClose(scan)

    transport.close()

    return dict

if __name__ == '__main__':
    now = datetime.now().strftime('%Y-%m-%d')
    # getHbase(now, 'stat_avgSessionDuring', 'stat_cf:during')
    asd = getHbase('2013-07-16', 'stat_avgSessionDuring', 'stat_cf:during', length=4)
    # print(asd)
