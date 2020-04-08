# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 08:01:50 2020

@author: Catalin
"""

from Controller import Controller 
from numpy import random
from Plot import Plot

class LoadProblem():
    def __init__(self):
        self.loadFromFile()
        self.__Controller=Controller(self.__noAnts,self.__n,self.__alpha,self.__beta,self.__q0,self.__rho,self.__noOfEpochs)
        
    def loadFromFile(self):
        with open('C:\\Users\\Catalin\\Desktop\\Faculty\\AI\\Lab 5\\parameters.txt', 'r') as file:
            
            line = file.readline().strip()
            self.__n = int(line.replace("permutation size:", ""))
            
            line = file.readline().strip()
            self.__noOfEpochs = int(line.replace("number of epoch:", ""))

            line = file.readline().strip()
            self.__noAnts = int(line.replace("number of ants:", ""))

            line = file.readline().strip()
            self.__alpha = float(line.replace("alpha:", ""))

            line = file.readline().strip()
            self.__beta = float(line.replace("beta:", ""))

            line = file.readline().strip()
            self.__rho = float(line.replace("rho:", ""))

            line = file.readline().strip()
            self.__q0 = float(line.replace("q0:", ""))
        
    def run(self):
        f=self.__Controller.RunAlg()
        print("Print the minimum fitness from each epoch [minimum, ant that got that minimum]:\n",f)
        fMin=self.__Controller.getMinFitness()
        print("The minimum fitness in the whole run: ",fMin )
    def main(self):
        while(True):
            print("1-run,2-validate")
            choice=input()
            if choice=="1":
                self.run()
            elif choice=="2":
                Plot()
            else:
                return
        
random.seed()        
UI=LoadProblem()
UI.main()