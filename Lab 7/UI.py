# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:07:14 2020

@author: Catalin
"""
from Controller import Controller

class UI:
    def __init__(self):
        self.Controller=Controller("data.txt")
        

    def run(self):
        while True:
            print("0-exit")
            print("1-run")
            choice = int(input())
            if choice == 1:
                print("Give alpha(You can try 0.01)")
                alpha =float(input())
                print("Give noOfIterations(You can try 1000)")
                noOfIterations = int(input())
                finalCost = self.Controller.results(noOfIterations,alpha)
                print("the cost is: ", finalCost)           
            else:
                return
        
UI=UI()
UI.run()        