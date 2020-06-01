# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:39:05 2020

@author: Catalin
"""

from ANN import ANN

class UI:
    def __init__(self):
        self.ANN=ANN("data.txt")
        

    def run(self):
        while True:
            print("0-exit")
            print("1-run")
            choice = int(input())
            if choice == 1:
                print("Give noOfIterations(You can try 1000)")
                noOfIterations = int(input())
                self.ANN.train(noOfIterations)
            else:
                return
        
UI=UI()
UI.run() 