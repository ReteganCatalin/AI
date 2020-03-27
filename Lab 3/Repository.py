# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:01:14 2020

@author: Catalin
"""
from State import State,PSOState
class Repository():
    def __init__(self,n,population,nrOfIterations,pM):
        self.__nrOfIterations=nrOfIterations
        self.__states=list()
        self.__pM=pM
        self.__initial_state=State(n,population)
        self.__states.append(self.__initial_state)
    
    def NextIteration(self):
        length=len(self.__states)
        self.__states.append(self.__states[length-1].iteration(self.__pM))
     
    
    def NextClimb(self):
        length=len(self.__states)
        nextState=self.__states[length-1].climb()
        self.__states.append(nextState)
        if nextState.getMinFitness()<self.__states[length-1].getMinFitness():
            return True
        return False
    
    def getNumberOfIterations(self):
        return self.__nrOfIterations
    
    def getFitnessMinimForEachState(self):
        length=len(self.__states)
        min_fitness=list()
        for index in range(0,length):
            min_fitness.append(self.__states[index].getMinFitness())
        return min_fitness
    
    
class PSORepository():
    def __init__(self,n,population,nrOfIterations,neighbours,cognitiveLearning,socialLearning,inertia):
        self.__nrOfIterations=nrOfIterations
        self.__states=list()
        self.__cognitiveLearning=cognitiveLearning
        self.__socialLearning=socialLearning
        self.__inertia=inertia
        self.__initial_state=PSOState(n,population,neighbours)
        self.__states.append(self.__initial_state)
        return 
    
    
    def recomputeInertiaCoefficient(self,index):
        self.__inertia=self.__inertia/(index+1)
    def NextIteration(self):
        length=len(self.__states)
        self.__states.append(self.__states[length-1].iteration(self.__inertia,self.__cognitiveLearning,self.__socialLearning))
     
    
    def getNumberOfIterations(self):
        return self.__nrOfIterations
    
    def getFitnessMinimForEachState(self):
        
        length=len(self.__states)
        min_fitness=list()
        for index in range(0,length):
            min_fitness.append(self.__states[index].getMinFitness())
        return min_fitness