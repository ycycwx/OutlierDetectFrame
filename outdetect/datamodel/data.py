#/usr/bin/env python3

from collections import defaultdict
import numpy as np

class Data:
    def __init__(self, data):
        """
        Sets data to the dataset
        ================================================================
        dictionary:
            KEY    =>  string,  make sure that KEY will be sorted
            VALUE  =>  list,    list  =>  float
        ================================================================
        EXAMPLE: {'20130721': [2.1, 2.4, ...],
                  '20130722': [0.5, 2,1, ...],
                  '........': [..., ..., ...],
                  '20130730': [0.7, 2.4, ...]}
        """
        self._data = data

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self.get())

    def __iter__(self):
        return iter(self.get())

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def set(self, data, update=False):
        """
        Sets data or update data
        ================================================================
        format:
            the same as self._data
        if update value is True:
            update the self._data with data
        """
        if update:
            self._data.update(data)
        else:
            self._data = data

    def get(self):
        return self._data

    def clear(self):
        self._data = {}

    def normalize(self):
        lst = np.array([ value for value in self._data.values() ], dtype='float_')

        maximum = lst.max(1)
        minimum = lst.min(1)

        tile_min  = np.tile(minimum, (len(lst[0]), 1)).transpose()
        tile_base = np.tile((maximum - minimum), (len(lst[0]), 1)).transpose()

        normalize = (lst - tile_min) / tile_base
        normalize[normalize == -np.inf] = 0.5

        cnt = 0
        for dat in self._data:
            self._data[dat] = list(normalize[cnt])
            cnt += 1

if __name__=='__main__':
    # d = [('20130721_05', 6), ('20130721_02', 2), ('20130721_01', 3)]
    d = {'20130723': [0.1,1,1,3], '20130721': [2,0,1,3], '20130722': [3,2,1,5.1]}
    a = Data(d)
    a.normalize()
    print(a)
    # print(len(a))
