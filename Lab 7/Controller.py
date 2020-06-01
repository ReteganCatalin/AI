# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:12:48 2020

@author: Catalin
"""
import numpy as np
class Controller():
    def __init__(self,filename):
        self.data=self.loadData(filename)
        self.normalisedData=self.normaliseData()
        self.splitData()
        
    def loadData(self, filename):
        data = np.loadtxt(filename, dtype=np.float32)
        return data
    
    def normaliseData(self):
        return (self.data - self.data.mean())/self.data.std()
    
    def splitData(self):
        self.X = self.normalisedData[:, 0:-1]
        ones = np.ones([self.X.shape[0], 1])
        self.X = np.concatenate((ones, self.X), axis=1)
        self.Y = self.normalisedData[:, [-1]]
        self.theta = np.zeros([1,len(self.normalisedData[0])])
    
    def computeCost(self):
        tosum=np.power(((self.X @ np.transpose(self.theta)) - self.Y), 2)
        return np.sum(tosum) / (2 * len(self.X))

    def gradientDescent(self, noOfIterations, alpha):
        for index in range(noOfIterations):
            self.theta = self.theta - (alpha/len(self.X)) * np.sum(self.X * (self.X @ np.transpose(self.theta) - self.Y), axis=0)

    def results(self, noOfIterations,alpha):
        self.splitData()
        self.gradientDescent(noOfIterations, alpha)
        finalCost = self.computeCost()
        return finalCost
