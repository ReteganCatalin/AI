# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 08:03:00 2020

@author: Catalin
"""
from numpy import random
from random import choice
from copy import deepcopy
class Ant():
    
    def __init__(self,n):
        self.__n=n
        self.__antPath=list()
        self.__currentPerm=list()
        
        
    def PossibleMoves(self):
        not_visited=list()
        for i in range(self.__n):
            if i not in self.__currentPerm:
                not_visited.append(i)
        return not_visited
    
    def getPermutation(self,index):
        return self.__antPath[index]
    
    def clear(self):
        self.__curentPerm=list()
        self.__antPath.clear()
            
    def NextMove(self,trace_matrix,alpha,beta,q0):
        if len(self.__currentPerm)!=0:
            #last position in a permutation tuple no need to do computations there is only one viable path to pick
            if len(self.__currentPerm)==self.__n-1:
                for i in range(0,self.__n):
                    if i not in self.__currentPerm:
                        self.__currentPerm.append(i)
                        self.__antPath.append(deepcopy(self.__currentPerm))
                        self.__currentPerm.clear()
                        return
            else:
                lastNode=self.__currentPerm[len(self.__currentPerm)-1]
                notVisited=self.PossibleMoves()
                length=len(notVisited)
                pheromones=[1 for i in range(length)]
                #we could remove beta**pheromones[i] since we pick 1 for visibility for all paths
                pheromones=[ (pheromones[i]**beta)*(trace_matrix[lastNode][notVisited[i]]**alpha) for i in range(length)]
                if (random.random()<q0):
                    # adaugam cea mai buna dintre mutarile posibile
                    pheromones = [ [i, pheromones[i]] for i in range(length) ]
                    pheromon = max(pheromones, key=lambda a: a[1])
                    self.__currentPerm.append(notVisited[pheromon[0]])
                    return
                else:
                    # adaugam cu o probabilitate un drum posibil (ruleta)
                    s = sum(pheromones)
                    if(s==0):
                        self.__currentPerm.append(choice(notVisited))
                    else:
                        pheromones = [ pheromones[i]/s for i in range(length) ]
                        pheromones = [ sum(pheromones[0:i+1]) for i in range(length) ]
                        r=random.random()
                        i=0
                        while (r > pheromones[i] or length-1>i):
                            i=i+1
                        self.__currentPerm.append(notVisited[i])
                        return
        else:
            #starting position for each permutation is picked always random(from discussion with the teacher)(
            self.__currentPerm.append(random.randint(0,self.__n))
    
        
    
    def fitness(self):
        pairs=dict()
        f=0;
        for position in range(0,self.__n):
            complete_perm=dict()
            for row in range(0,self.__n):
                if self.__antPath[row][position] in complete_perm.keys():
                    f+=1
                else:
                    complete_perm[self.__antPath[row][position]]=0
        for position in range(0,self.__n):
            complete_perm=dict()
            for row in range(self.__n,2*self.__n):
                if self.__antPath[row][position] in complete_perm.keys():
                    f+=1
                else:
                    complete_perm[self.__antPath[row][position]]=0
                                              
        for pair in range(0,self.__n*self.__n):
            x=self.__antPath[pair//self.__n][pair%self.__n]
            y=self.__antPath[self.__n+pair//self.__n][pair%self.__n]
            if x*self.__n+y in pairs.keys():
                f=f+1
            else:
                pairs[x*self.__n+y]=0
        if f==0:
            print("Solution: ",self.__antPath)
        #+1 to dodge division by zero problems
        return f+1
        