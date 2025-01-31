# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:48:16 2020

@author: Catalin
"""

from Controller import Controller
class UI:
    def __init__(self):
        self.__controller = Controller("training.in", "input.in", "output.out")
        
    def run(self):
        while True:
            print("1-Run, 2-Exit")
            choice =input("Choice: ")
            if choice == '1':
                nrOfIndividuals = int(input("Number of individuals:")) 
                iterations = int(input("Iterations per epoch:"))
                trainingSize = int(input("Training size(<4000):"))
                testingSize = int(input("Testing size(<1457):"))
                mutationProbability = float(input("Mutation probability:"))
                crossoverProbability = float(input("Crossover probability:"))
                epsilon = float(input("Epsilon: "))
                self.__controller.run(nrOfIndividuals, iterations, trainingSize, testingSize, mutationProbability, crossoverProbability, epsilon)
            else:
                return

UI=UI()
UI.run()