#!/usr/bin/env python3

from ..datamodel.data import Data
from ..algorithm.OutlierBasic import OutlierBasic
from ..utils.distance import Distance
from ..utils.log import LOG
import numpy as np

class HourDetect(OutlierBasic):
    def __init__(self, data):
        OutlierBasic.__init__(self, data)

    def set_conf(self, conf):
        """
        Set Configurations

        Properties in conf:
            target      =>  string
            dist        =>  euclidean or other measures in utils/distance.py
            norm_range  =>  float between 0.0-1.0
            threshold   =>  float between 0.0-1.0
        """
        self._target     = conf.get('target', None)
        # self._distance   = getattr(outdetect.utils.distance, conf.get('dist', 'euclidean'))
        self._distance   = getattr(Distance, conf.get('dist', 'euclidean'))
        self._norm_range = conf.get('norm_range', 0.5)
        self._threshold  = conf.get('threshold', 0.25)

    # Calculate similarity
    def _cal_sim(self):
        data = sorted(self._data.get().items())
        data = [ x[1] for x in data ]
        result = np.zeros((len(data), len(data)))

        for i in range(len(data)):
            for j in range(len(data)):
                result[i][j] = self._distance(data[i], data[j])

        return result

    # Sort the matrix and pick up outlier curves
    def get_normal_flag(self):
        # Append sum value into sum_list
        min_var = 100000000000000
        min_index = 0
        sum_list = []
        matrix = self._matrix
        for i in range(matrix[0].size):
            sum_list.append(sum(matrix[i]))

        # Set threshold in order to detect normal series
        threshold = (max(sum_list) - min(sum_list)) * self._norm_range + min(sum_list)

        # Create initial normal list
        normal_flag = [ 0 for i in range(len(sum_list)) ]

        # Make a normal list flag
        for i in range(len(sum_list)):
            if sum_list[i] > threshold:
                pass
            else:
                normal_flag[i] = 1

        self._normal_flag = normal_flag

    # Outlier test phase
    def _daily_outlier_test(self, daily_series, normal_series):
        for i in range(len(daily_series)):
            dist = self._distance([daily_series[i]], [normal_series[i]])
            if dist >= self._threshold:
                return False 
        return True

    # Get normal days
    def _get_normal_series(self):
        '''
         --- norm_flag ---
        |   0:  outlier   |
        |   1:  normal    |
         -----------------
        '''
        norm_series = []
        norm_data = sorted(self._data)
        
        for i in range(len(norm_data)):
            if self._normal_flag[i] == 1:
                norm_series.append(self._data[norm_data[i]])

        # Get every normal day's value and calculating means of them
        norm   = list(map(sum, zip(*norm_series)))
        normal = list(map(lambda x: x / len(norm_series), norm))

        return normal

    def run(self):
        try:
            assert self._target is not None
        except AssertionError:
            print('AssertionError: Target has not been set')
            print('Please use set_conf function to set target')
            print('...SYSTEM EXIT')
            sys.exit()

        self._matrix = self._cal_sim()
        self.get_normal_flag()
        normal = self._get_normal_series()

        self.anormal = []

        cnt = 0
        for day in self._data:
            cnt += 1
            if not self._daily_outlier_test(self._data[day], normal):
                self.anormal.append(day)

        print(self.anormal)
        return self.anormal

    def outlier_detection(self):
        return self.run()

if __name__=='__main__':
    data = Data({'20130721': [2.1, 2.4, 2.2, 2.1],
                 '20130722': [0.5, 2.1, 2.3, 3.1],
                 '20130723': [0.7, 2.4, 2.0, 0.1]})
    data.normalize()

    od = HourDetect(data)
    conf = {'target':'visitUser', 'dist':'euclidean', 'norm_range':0.5}
    od.set_conf(conf)
    od.run()
    # od.save()
