# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:57:14 2020

@author: Catalin
"""


class Controller:
    def __init__(self, problem):
        self.__temperatureRegions = problem.getTemperatureRegions()
        self.__capacityRegions = problem.getCapacityRegions()
        self.__powerRegions = problem.getPowerRegions()
        self.__rules = problem.getRules()
        
    def getTemperatureRegion(self, name):
        for region in self.__temperatureRegions:
            if region.getRegionName() == name:
                return region
            
    def getCapacityRegion(self, name):
        for region in self.__capacityRegions:
            if region.getRegionName() == name:
                return region 
    def getPowerRegion(self, name):
        for region in self.__powerRegions:
            if region.getRegionName() == name:
                return region
            
    def getRulesResults(self):
        resultSmall = 0
        resultHigh = 0
        resultMedium = 0
        for rule in self.__rules:
            if  rule.getPower() == "small" and rule.getValue() > resultSmall:
                resultSmall = rule.getValue()
            if rule.getPower() == "high" and rule.getValue() > resultHigh:
                resultHigh = rule.getValue()
            if rule.getPower() == "medium" and rule.getValue() > resultMedium:
                resultMedium = rule.getValue()
                
        return resultSmall, resultHigh, resultMedium
    

    def Fuzzify(self,Temp,Cap):
        #Mamdani method
        self.__temperatureResults = {}
        self.__capacityResults = {}              
        for rule in self.__rules:
            if rule.getTemperature() not in self.__temperatureResults:
                resultTemp = self.getTemperatureRegion(rule.getTemperature()).computeFunction(Temp)
                self.__temperatureResults[rule.getTemperature()] = resultTemp
            else:
                resultTemp = self.__temperatureResults[rule.getTemperature()]
            if rule.getCapacity() not in self.__capacityResults:
                resultCap = self.getCapacityRegion(rule.getCapacity()).computeFunction(Cap)
                self.__capacityResults[rule.getCapacity()] = resultCap
            else:
                resultCap = self.__capacityResults[rule.getCapacity()]       
            result = min(resultTemp, resultCap)
            rule.setValue(result)
        return self.getRulesResults()
    
    def Defuzzify(self,resultSmall, resultHigh, resultMedium):
        #Centroid Area method
        partialResult = 0
        denominator = 0
        for index in range(0, 21):
            Small=min(self.getPowerRegion("small").computeFunction(index),resultSmall)
            Medium=min(self.getPowerRegion("medium").computeFunction(index),resultMedium)
            High=min(self.getPowerRegion("high").computeFunction(index),resultHigh)
            partialResult += (index * max(Small, Medium,High))
            denominator += max(Small, Medium,High)
        if denominator > 0:
            partialResult = partialResult / denominator
        return partialResult
    
    def OutPut(self,Temp,Cap,partialResult):
        f = open("output.out", "a")
        string = "For temperature " + str(Temp) + " and capacity " + str(Cap) + ", we obtain power = " + str(partialResult)
        f.write(string + "\n")
        f.close()    
        print(string)
        
    def solve(self,Temp,Cap):
        resultSmall, resultHigh, resultMedium=self.Fuzzify(Temp,Cap)
        partialResult=self.Defuzzify(resultSmall, resultHigh, resultMedium)
        self.OutPut(Temp,Cap,partialResult)
            
       

                