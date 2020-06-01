# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:06:23 2020

@author: Catalin
"""

class TriangularRegion:
    def __init__(self, a, b, c, name):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__name = name
        
    def getRegionName(self):
        return self.__name
    
    def computeFunction(self, x):
        computed_ret = 1
        if (self.__b - self.__a != 0):
            computed= (x - self.__a) / (self.__b - self.__a)
            if computed_ret > computed:
                computed_ret = computed
        if (self.__c - self.__b != 0):
            computed = (self.__c - x) / (self.__c - self.__b)
            if computed_ret > computed:
                computed_ret = computed          
        if computed_ret < 0:
            return 0
        else:
            return computed_ret
        
    def __str__(self):
        return str(self.__a) + " " + str(self.__b) + " " + str(self.__c) + " " + self.__name; 