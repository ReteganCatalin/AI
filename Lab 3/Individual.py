# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 14:41:39 2020

@author: Catalin
"""
from copy import deepcopy
from itertools import permutations
from numpy import random


def convert(list): 
    return tuple(list) 

class Individuals():
    def __init__(self,n):
        self.__n=n
        self.__individual=list()
        for i in range(0,2*self.__n):
            self.__individual.append(self.create_permutation())
            
  
    
    def create_permutation(self):
        return convert(random.permutation(self.__n))
     
                  
    def fitness(self):
        #TODO
        pairs=dict()
        f=0;
        for position in range(0,self.__n):
            complete_perm=dict()
            for row in range(0,self.__n):
                if self.__individual[row][position] in complete_perm.keys():
                    f+=1
                else:
                    complete_perm[self.__individual[row][position]]=0
        for position in range(0,self.__n):
            complete_perm=dict()
            for row in range(self.__n,2*self.__n):
                if self.__individual[row][position] in complete_perm.keys():
                    f+=1
                else:
                    complete_perm[self.__individual[row][position]]=0
                                              
        for pair in range(0,self.__n*self.__n):
            x=self.__individual[pair//self.__n][pair%self.__n]
            y=self.__individual[self.__n+pair//self.__n][pair%self.__n]
            if x*self.__n+y in pairs.keys():
                f=f+1
            else:
                pairs[x*self.__n+y]=0
        return f
    
    def mutate(self,pM):  
        if pM > random.random():
                p = random.randint(0,self.__n)
                self.__individual[p] = self.create_permutation() 
                #print(self.individual[p],self.n)
        return self.__individual
    def getIndividual(self):
        return self.__individual
    
    def setIndividual(self,new_individual):
        self.__individual=new_individual
        
    def setPermutation(self,index,permutation):
        self.__individual[index]=permutation
        
    def getNeighbours(self):
        neighbours = []
        for index in range(len(self.__individual)):  
            perms = list(permutations(self.__individual[index]))
            for perm in perms:
                copy = deepcopy(self)
                copy.setPermutation(index, perm)
                neighbours.append(copy)
        return neighbours
    def climb(self):
        neighbours=self.getNeighbours()
        copy = deepcopy(self)
        for neighbour in neighbours:
            if neighbour.fitness()<copy.fitness():
                print("something")
                copy=neighbour
        return copy
        

def crossover(parent1, parent2):
    '''
    crossover between 2 parents
    '''
    individual_parent1=parent1.getIndividual()
    individual_parent2=parent2.getIndividual()
    length=len(individual_parent1)
    child=Individuals(length//2)
    child_individual=child.getIndividual()
    alpha=random.randint(0,length)
    beta=random.randint(alpha,length)
    for x in range(length):
        if x>=alpha and x<beta:
            child_individual[x]=individual_parent2[x]
        else:
            child_individual[x]=individual_parent1[x]
    return child   