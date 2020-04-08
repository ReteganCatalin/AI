# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 12:07:24 2020

@author: Catalin
"""
from Controller import Controller
import numpy as np
import matplotlib.pyplot as plt
def Plot():
   permutationSize = 4
   ants=15
   epoch=100
   nrOfRuns=30
   alpha=1.9
   beta=0.9
   rho=0.05
   q0=0.5
   #controller = Controller(ants,permutationSize,alpha,beta,q0,rho,epoch) 
    
   fitnesses = []
    
   for i in range(nrOfRuns):
       controller=Controller(ants,permutationSize,alpha,beta,q0,rho,epoch)
       controller.RunAlg()
       sol= controller.getMinFitness()
       print(sol)
       fitnesses.append(sol)
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
   