# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:57:40 2020

@author: Catalin
"""

from numpy import random
from Individual import Individuals,crossover
from copy import deepcopy
class State():
    def __init__(self,n,population):
        self.__n=n
        self.__individuals=list()
        for i in range(0,population):
            self.__individuals.append(Individuals(n))
            
    def getState(self):
        return State
    
    def getMinFitness(self):
        min_fitness=self.__individuals[0].fitness()
        for index in range(1,len(self.__individuals)):
            if self.__individuals[index].fitness()<min_fitness:
                min_fitness=self.__individuals[index].fitness()
        return min_fitness
    
    
    def iteration(self, pM):
        i1=random.randint(0,len(self.__individuals)-1)
        i2=random.randint(0,len(self.__individuals)-1)
        if (i1!=i2):
            c=crossover(self.__individuals[i1],self.__individuals[i2])
            c.setIndividual(c.mutate(pM))
            f1=self.__individuals[i1].fitness()
            f2=self.__individuals[i2].fitness()
            fc=c.fitness()
            if(f1>f2) and (f1>fc):
                #print(str(f1)+">"+str(fc))
                self.__individuals[i1]=deepcopy(c)
            if(f2>f1) and (f2>fc):
                #print(str(f2)+">"+str(fc))
                self.__individuals[i2]=deepcopy(c)
        return deepcopy(self)
    
    def PSOiteration(self,cognitiveLearning,socialLearning,inertia):
        return 
    
    def climb(self):
        copy=deepcopy(self)
        copy.__individuals[0]=self.__individuals[0].climb()
        return copy


class PSOState():
    def __init__(self,n,population):
        self.__n=n
        self.__particles=list()
        for i in range(0,population):
            self.__particles.append(Particles(n))
            
    def getState(self):
        return State
    
    def getMinFitness(self):
        min_fitness=self.__particles[0].fitness()
        for index in range(1,len(self.__particles)):
            if self.__particles[index].fitness()<min_fitness:
                min_fitness=self.__particles[index].fitness()
        return min_fitness
    
    
    def iteration(self,cognitiveLearning,socialLearning,inertia):
        return 
    
    

