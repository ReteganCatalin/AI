# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:58:09 2020

@author: Catalin
"""
from Problem import Problem

class Controller():
    def __init__(self):
        self.Problem=Problem()
        return
    
    def ResizeAndRestart(self,new_size):
        self.Problem.ResizeAndRestart(new_size)
        
        
    def DFS(self):
        while self.Problem.IsEmpty()!=True:
            if self.Problem.IsFinalState()!=True:
                self.Problem.Expand()
        return self.Problem.ReturnFinalStates()
                
    
    def Greedy(self):
        while self.Problem.IsGreedyEnd()!=True:
            self.Problem.ExpandGreedy()
            self.Problem.Heuristic()
        return self.Problem.ReturnProgress()
    
    
        
    