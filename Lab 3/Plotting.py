# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:02:51 2020

@author: Catalin
"""
import numpy as np
from PyQt5.QtCore import QThread
from Controller import Controller,PSOController
import matplotlib.pyplot as plt
class PlottingEAThread(QThread):
    def __init__(self, workerController=None):
        QThread.__init__(self)
        self.shouldContinue = True

    def __del__(self):
        self.wait()

    def stop(self):
        self.shouldContinue = False

    def run(self):
        permutationSize = 4
        population=40
        numberOfIterations=1000
        pM=0.5
        nrOfRuns=30
        controller = Controller(permutationSize,population,numberOfIterations,pM) 
        
        fitnesses = []
        
        for i in range(nrOfRuns):
            controller.reinitializeController(permutationSize,population,numberOfIterations,pM)
            for i in range(numberOfIterations):
                controller.NextIteration()
            sol= controller.getMinFitness()
            print(sol[len(sol)-1])
            fitnesses.append(sol[len(sol)-1])
        m = np.mean(fitnesses, axis=0)
        stddev = np.std(fitnesses, axis=0)
        means = []
        dev = []
        
        for i in range(nrOfRuns):
            means.append(m)
            dev.append(abs(m-fitnesses[i]))
            
        plt.plot(range(nrOfRuns), means)
        plt.plot(range(nrOfRuns), dev)
        print("Standard deviation is: "+str(stddev))
        plt.plot(range(nrOfRuns), fitnesses)
        plt.show()
        self.stop()
        
        
class PlottingPSOThread(QThread):
    def __init__(self, workerController=None):
        QThread.__init__(self)
        self.shouldContinue = True

    def __del__(self):
        self.wait()

    def stop(self):
        self.shouldContinue = False

    def run(self):
        permutationSize = 4
        population=40
        numberOfIterations=150
        neighbours=13
        socialCoeff=1
        cognitiveCoeff=2.5
        inertia=1
        nrOfRuns=30
        controller = PSOController(permutationSize,population,numberOfIterations,neighbours,socialCoeff,cognitiveCoeff,inertia) 
        
        fitnesses = []
        
        for i in range(nrOfRuns):
            controller.reinitializeController(permutationSize,population,numberOfIterations,neighbours,socialCoeff,cognitiveCoeff,inertia) 
            for i in range(numberOfIterations):
                controller.NextIteration()
            sol= controller.getMinFitness()
            print(sol[len(sol)-1])
            fitnesses.append(sol[len(sol)-1])
        m = np.mean(fitnesses, axis=0)
        stddev = np.std(fitnesses, axis=0)
        means = []
        dev = []
        
        for i in range(nrOfRuns):
            means.append(m)
            dev.append(abs(m-fitnesses[i]))
            
        plt.plot(range(nrOfRuns), means)
        plt.plot(range(nrOfRuns), dev)
        print("Standard deviation is: "+str(stddev))
        plt.plot(range(nrOfRuns), fitnesses)
        plt.show()
        self.stop()