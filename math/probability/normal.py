#!/usr/bin/env python3
'''
    Normal distribution
'''


class Normal:
    '''
        Class Normal that represents
        a normal distribution
    '''

    def __init__(self, data=None, mean=0., stddev=1.):
        '''
            Class constructor
        '''
        if data is None:
            if stddev < 1:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
                self.mean = float(mean)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                mean = float(sum(data) / len(data))
                self.mean = mean
                summation = 0
                for x in data:
                    summation += ((x - mean) ** 2)
                stddev = (summation / len(data)) ** (1 / 2)
                self.stddev = stddev

    def z_score(self, x):
        '''
            Calculates the z-score of a given x-value
        '''
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        '''
            Calculates the x-value of a given z-score
        '''
        return (z * self.stddev) + self.mean
