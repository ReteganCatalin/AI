# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:57:23 2020

@author: Catalin
"""

from Repository import PSORepository,Repository

class Controller():
    def __init__(self,n,population,nrOfIterations,pM ):
        self.__Repository=Repository(n,population,nrOfIterations,pM)
        
    def NextIteration(self):
        self.__Repository.NextIteration()
        
    def getNumberOfIterations(self):
        return self.__Repository.getNumberOfIterations()
            
    def getMinFitness(self):
        return self.__Repository.getFitnessMinimForEachState()
    
    def getLastFitness(self):
        allFitnesses=self.__Repository.getFitnessMinimForEachState()
        if allFitnesses[len(allFitnesses)-1]>=allFitnesses[len(allFitnesses)-2]:
            return allFitnesses[len(allFitnesses)-2]
        return allFitnesses[len(allFitnesses)-1]
        
    def NextClimb(self):
        return self.__Repository.NextClimb()

class PSOController():
    def __init__(self,n,population,nrOfIterations,cognitiveLearn,socialLearn,inertia):
        self.__Repository=PSORepository(n,population,nrOfIterations,cognitiveLearn,socialLearn,inertia)
        
    def getNumberOfIterations(self):
        return self.__Repository.getNumberOfIterations()
    
    def getMinFitness(self):
        return self.__Repository.getFitnessMinimForEachState()
    
    def NextIteration(self):
        self.__Repository.NextIteration()
    
    
    
    
    
    
    