# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:03:52 2020

@author: Catalin
"""


from numpy import random


def convert(list): 
    return tuple(list)


class Particle():
    def __init__(self,n):
        self.__n=n
        self.__particle=list()
        self.__velocity=list()
        for i in range(0,2*self.__n):
            self.__particle.append(self.create_permutation())
            self.__velocity.append(0)
        self.__fitness=self.fitness()
        
        self.__BestPosition=self.__particle
        self.__BestFitness=self.__fitness
  
    def getManhattanDistance(self,index,neighbour):
        self_perm=self.__particle[index]
        neighbour_perm=neighbour.__particle[index]
        sum=0
        for number in range(self.__n):
            sum+=abs(self_perm[number]-neighbour_perm[number])
        return sum
    
    def getBestPositionManhattanDistance(self,index):
        self_perm=self.__particle[index]
        best_perm=self.__BestPosition[index]
        sum=0
        for number in range(self.__n):
            sum+=abs(self_perm[number]-best_perm[number])
        return sum
    
    def create_permutation(self):
        return random.permutation(self.__n)
     
    def getVelocity(self):
        return self.__velocity
    
    def setaVelocity(self,index,new_velocity):
        self.__velocity[index]=new_velocity
    
  
    def fitness(self):
        pairs=dict()
        f=0;
        for position in range(0,self.__n):
            complete_perm=dict()
            for row in range(0,self.__n):
                if self.__particle[row][position] in complete_perm.keys():
                    f+=1
                else:
                    complete_perm[self.__particle[row][position]]=0
        for position in range(0,self.__n):
            complete_perm=dict()
            for row in range(self.__n,2*self.__n):
                if self.__particle[row][position] in complete_perm.keys():
                    f+=1
                else:
                    complete_perm[self.__particle[row][position]]=0
                                              
        for pair in range(0,self.__n*self.__n):
            x=self.__particle[pair//self.__n][pair%self.__n]
            y=self.__particle[self.__n+pair//self.__n][pair%self.__n]
            if x*self.__n+y in pairs.keys():
                f=f+1
            else:
                pairs[x*self.__n+y]=0
        return f

    def getParticle(self):
        return self.__particle
    
    def getBestPosition(self):
        return self.__BestPosition
    
    def getBestFitness(self):
        return self.__BestFitness
    
    def recompute(self):
        
        # automatic evaluation of particle's fitness
        self.__fitness=self.fitness()
        
        # automatic update of particle's memory
        if (self.__fitness<self.__BestFitness):
            #print(str(self.__fitness)+"<"+str(self.__BestFitness))
            self.__BestPosition = self.__particle
            self.__BestFitness  = self.__fitness
        
      
    def setPermutation(self,index,permutation):
        self.__particle[index]=permutation
    def getPermutation(self,index):
        return self.__particle[index]
    
    
        
    
      