# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:57:12 2020

@author: Catalin
"""

class Rule:
    def __init__(self,temperature, capacity, power):
        self.__value = 0
        self.__temperature = temperature
        self.__capacity = capacity
        self.__power = power
        
    def addToValue(self, val):
        self.__value += val 
        
    def setValue(self, val):
        if val > self.__value:
            self.__value = val
        
    def getValue(self):
        return self.__value
    
    def getTemperature(self):
        return self.__temperature
    
    def getCapacity(self):
        return self.__capacity
    
    def getPower(self):
        return self.__power
    
    
    def __str__(self):
        return self.__temperature + " " + self.__capacity + " " + self.__power + " " + str(self.__value); 
