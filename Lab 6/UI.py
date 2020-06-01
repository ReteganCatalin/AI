# -*- coding: utf-8 -*-
"""yes
Created on Thu Apr  9 11:25:14 2020

@author: Catalin
"""

from Controller import Controller


class UI:
    def __init__(self):
        self.MainMenu()
        
    def MainMenu(self):
        while(True):
            print("Give the number of runs")
            runs=int(input())
            controller=Controller(runs)
            average,maximum=controller.RunAlg()
            print("Average accuracy: ",average, " Maximum accuracy: ",maximum)
            print("Exit(yes or no)?")
            choice=input()
            if choice=="yes":
                return
            
UI=UI()