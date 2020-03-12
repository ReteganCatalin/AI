# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:55:55 2020

@author: Catalin
"""

from Controller import Controller

class Menu():
    def __init__(self):
        self.Controller=Controller()
        
    def MainMenu(self):
        while(True):
            print("Give size of matrix (if 0 the program will stop):")
            size=int(input())
            if size!=0:
                self.Controller.ResizeAndRestart(size)
                print("Type of solution 1- dfs, 2-greedy")
                pick=input()
                if pick=='1':
                    FinalStates=self.Controller.DFS()
                    if len(FinalStates)!=0:
                        print("Correct States:")
                        for State in FinalStates:
                            print(State)
                    else:
                        print("No Solution Found !")
                else:
                    FinalState=self.Controller.Greedy()                
                    if FinalState[0].CheckCorrectState()==True:
                        print("Correct Final State")
                    else:
                        print("Incorrect final state")
                    print(FinalState[0])
            else:
                return 
            