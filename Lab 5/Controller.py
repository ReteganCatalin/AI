# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 08:02:30 2020

@author: Catalin
"""
from Ant import Ant
class Controller():
    def __init__(self,antPopulation,n,alpha,beta,q0,rho,noOfEpoch):
        self.__antSet=[Ant(n) for i in range(antPopulation)]
        self.__antPopulation=antPopulation
        self.__n=n
        self.__alpha=alpha
        self.__beta=beta
        self.__q0=q0
        self.__rho=rho
        self.__noOfEpoch=noOfEpoch
        self.__trace_matrices=[[[0 for z in range(n)] for j in range(n)] for i in range(2*n)]
        
    def epoch(self):
        for i in range(self.__antPopulation):
            self.__antSet[i].clear()
        for i in range(2*self.__n*self.__n):
            # numarul maxim de iteratii intr-o epoca este lungimea solutiei
            for x in self.__antSet:
                x.NextMove(self.__trace_matrices[i//self.__n],self.__alpha, self.__beta,self.__q0)
        # actualizam trace-ul cu feromonii lasati de toate furnicile
        antFitnessTrace=[ 1.0 / self.__antSet[i].fitness() for i in range(len(self.__antSet))]
       
        for i in range(2*self.__n):
            for j in range(self.__n):
                for z in range (self.__n):
                    self.__trace_matrices[i][j][z] = (1 - self.__rho) * self.__trace_matrices[i][j][z]
        for antIndex in range(self.__antPopulation):
            for permutation in range(2*self.__n):
                Path = self.__antSet[antIndex].getPermutation(permutation)
                firstNode=Path[0]
                for second in range(1,self.__n-1):
                    secondNode=Path[second]
                    self.__trace_matrices[permutation][firstNode][secondNode] = self.__trace_matrices[permutation][firstNode][secondNode] + antFitnessTrace[antIndex]
                    firstNode=secondNode
                    
        # return best ant path
        f=[ [self.__antSet[i].fitness()-1, i] for i in range(self.__antPopulation)]
        f=min(f)
        return f
    
    def RunAlg(self):
        self.f=list()
        for i in range(0,self.__noOfEpoch):
            self.f.append(self.epoch())
        return self.f
    
    def getMinFitness(self):
        return min(self.f)[0]