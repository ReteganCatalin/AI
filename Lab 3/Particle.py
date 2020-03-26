# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:03:52 2020

@author: Catalin
"""

from copy import deepcopy
from numpy import random


def convert(list): 
    return tuple(list) 

class Particle():
    def __init__(self,n):
        self.__n=n
        self.__particle=list()
        for i in range(0,2*self.__n):
            self.__particle.append(self.create_permutation())
        self.__fitness=self.fitness()
            
  
    
    def create_permutation(self):
        return convert(random.permutation(self.__n))
     
                  
    def fitness(self):
        #TODO
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
    
    def setParticle(self,new_particle):
        self.__particle=new_particle
        
    def setPermutation(self,index,permutation):
        self.__particle[index]=permutation
        
    
      