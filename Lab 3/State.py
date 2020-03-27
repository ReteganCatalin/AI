# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:57:40 2020

@author: Catalin
"""

from numpy import random,exp,logaddexp 
import random as ram
from Individual import Individuals,crossover
from copy import deepcopy
from Particle import Particle


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
    def __init__(self,n,population,neighbours):
        random.seed()
        self.__n=n
        self.__particles=list()
        self.__population=population
        self.__neighbour=neighbours
        for i in range(0,population):
            self.__particles.append(Particle(n))
        self.__neighbours=self.selectNeighbors()
    def selectNeighbors(self):
        neighbours=[]
        for i in range(self.__population):
            if (self.__neighbour==self.__population-1):
                #print("no")
                order=random.permutation(self.__population)
                localNeighbour=[]
                for index in order:
                    if index!=i:
                        localNeighbour.append(index)
            else:
    
                localNeighbour=[]
                for j in range(self.__neighbour):
                    x=random.randint(0, self.__population-1)
                    while x in localNeighbour or x==i :
                        x=random.randint(0, self.__population-1)
                    localNeighbour.append(x)
                neighbours.append(localNeighbour.copy())
        #print(neighbours)
        return neighbours
    
    
    def getState(self):
        return State
    
    def getMinFitness(self):
        min_fitness=self.__particles[0].getBestFitness()
        for index in range(1,len(self.__particles)):
            if self.__particles[index].getBestFitness()<min_fitness:
                min_fitness=self.__particles[index].getBestFitness()
        return min_fitness
    
    
    def iteration(self,cognitiveLearning,socialLearning,inertia):
        bestNeighbours=[]
        #determine the best neighbor for each particle
        for i in range(self.__population):
            bestNeighbours.append(self.__neighbours[i][0])
            for j in range(1,len(self.__neighbours[0])):
                if self.__particles[bestNeighbours[i]].fitness()>self.__particles[self.__neighbours[i][j]].fitness():
                    bestNeighbours[i]=self.__neighbours[i][j]
                    
        #update the velocity for each particle
        for i in range(self.__population):
            velocities=self.__particles[i].getVelocity()
            for j in range(len(velocities)):
                if velocities[j]==float("-inf") or velocities[j]==float("inf") or  inertia==float("-inf") or inertia==float("inf"):
                    newVelocity = 0
                else:
                    newVelocity = inertia * velocities[j]
                newVelocity = newVelocity + cognitiveLearning * ram.random() * (self.__particles[bestNeighbours[i]].getManhattanDistance(j,self.__particles[i]))    
                newVelocity = newVelocity + socialLearning*ram.random()*(self.__particles[i].getBestPositionManhattanDistance(j))
                self.__particles[i].setaVelocity(j, newVelocity)
        
        #update the position for each particle
                
        for i in range(self.__population):
            velocities=self.__particles[i].getVelocity()
            for j in range(len(velocities)):
                if ram.random() < self.__sigmoid(velocities[j]):
                    self.__particles[i].setPermutation(j, self.__particles[bestNeighbours[i]].getPermutation(j))
            self.__particles[i].recompute()
        return deepcopy(self)
    
    
    def __sigmoid(self, value):
        return exp(-logaddexp(0, -value)) # math trick to avoid overflow
    
    

