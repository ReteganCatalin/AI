# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:14:42 2020

@author: Catalin
"""

from TriangularRegion import TriangularRegion
from TrapezoidalRegion import TrapezoidalRegion
from Rule import Rule

class Problem:
    def __init__(self, fileName1, fileName2, fileName3,fileName4):
        self.createTemperatureRegions(fileName1)
        self.createCapacityRegions(fileName2)
        self.createPowerRegions(fileName3)
        self.createRules(fileName4)
        
        
    def createTemperatureRegions(self,fileName):
        file = open(fileName)
        self.__temperatureRegions = []
        trapezoidals = ["cold", "very hot"]
        line = file.readline().strip()
        while (line != ""):
            parameters = line.split(",")
            if parameters[0] in trapezoidals:
                region = TrapezoidalRegion(int(parameters[1]), int(parameters[2]), int(parameters[3]), int(parameters[4]), parameters[0])
                self.__temperatureRegions.append(region)
            else:
                region = TriangularRegion(int(parameters[1]), int(parameters[2]), int(parameters[3]), parameters[0])
                self.__temperatureRegions.append(region)
            line = file.readline().strip()   
        file.close()
            
    def createCapacityRegions(self,fileName):
        file = open(fileName)
        self.__capacityRegions = []
        line = file.readline().strip()
        while (line != ""):
            parameters = line.split(",")
            region = TriangularRegion(int(parameters[1]), int(parameters[2]), int(parameters[3]), parameters[0])
            self.__capacityRegions.append(region)
            line = file.readline().strip()
            
        file.close()
        
    def createPowerRegions(self,fileName):
        file = open(fileName)
        self.__powerRegions = []
        line = file.readline().strip()
        while (line != ""):
            parameters = line.split(",")
            region = TriangularRegion(int(parameters[1]), int(parameters[2]), int(parameters[3]), parameters[0])
            self.__powerRegions.append(region)
            line = file.readline().strip()
            
        file.close()
        
    
            
    def createRules(self,fileName):
        file = open(fileName)
        self.__rules = []
        line = file.readline().strip()
        while (line != ""):
            parameters = line.split(",")
            rule = Rule(parameters[0], parameters[1], parameters[2])
            self.__rules.append(rule)
            line = file.readline().strip()   
        file.close()
            
    def getTemperatureRegions(self):
         return self.__temperatureRegions
     
    def getCapacityRegions(self):
        return self.__capacityRegions
    
    def getPowerRegions(self):
        return self.__powerRegions
    
    def getRules(self):
        return self.__rules