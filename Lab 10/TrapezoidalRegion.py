# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:10:15 2020

@author: Catalin
"""

class TrapezoidalRegion:
    def __init__(self, a, b, c, d, name):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__name = name
        
    def getRegionName(self):
        return self.__name
    
    def computeFunction(self, x):
        computed_ret = 1
        if (self.__b - self.__a != 0):
            computed = (x - self.__a) / (self.__b - self.__a)
            if computed_ret > computed:
                computed_ret = computed
        if (self.__d - self.__c != 0):
            computed = (self.__d - x) / (self.__d - self.__c)
            if computed_ret > computed:
                computed_ret = computed
        if computed_ret < 0:
            return 0
        else:
            return computed_ret
        