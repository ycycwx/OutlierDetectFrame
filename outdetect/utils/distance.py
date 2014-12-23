#!/usr/bin/env python3

import math
import numpy as np

class Distance:
    @classmethod
    def cosine(self, item1, item2):
        sum1 = 0.0
        sum2 = 0.0
        for item in item1:
            sum1 += pow(item, 2.0)
        for item in item2:
            sum2 += pow(item, 2.0)
        
        sum = 0.0
        for i in range(len(item1)):
            sum += item1[i] * item2[i]
        
        return sum / math.sqrt(sum1 * sum2)

    @classmethod
    def euclidean(self, item1, item2):
        sum = 0.0
        for i in range(len(item1)):
            sum += pow(item1[i] - item2[i], 2.0)
        return math.sqrt(sum)

    @classmethod
    def cross_correlation(self, item1, item2):
        return np.correlate(item1, item2)[0]

    @classmethod
    def dynamic_time_wraping(self, item1, item2):
        # Define distance function
        dist = lambda a, b : self.euclidean(a, b)
        
        # Define MAX Value
        MAX_COST = 1 << 32
        
        # Create MAX matrix where size is len(item1) * len(item2), value of [0, 0] is 0
        dtw = np.mat([MAX_COST] * (len(item1) * len(item2)), dtype = np.float).reshape(len(item1), len(item2))
        dtw[0, 0] = 0.0
        
        for i in range(len(item1)):
            for j in range(len(item2)):
                if i + j == 0:
                    continue
                pre_route = []
                if i > 0: pre_route.append(dtw[i - 1, j])
                if j > 0: pre_route.append(dtw[i, j - 1])
                if i > 0 and j > 0: pre_route.append(dtw[i - 1, j - 1])
                min_route = min(pre_route)
                cost = dist([item1[i]], [item2[j]])
                # print(i)
                # print(j)
                # print(dtw)
                dtw[i, j] = float(cost) + float(min_route)
        
        return dtw[len(item1) - 1, len(item2) - 1]
