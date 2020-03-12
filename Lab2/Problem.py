# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:58:22 2020

@author: Catalin
"""
from State import State,HeuristicComputation
class Problem():
    
    def __init__(self):
        self.InitialState=State()
        self.ProgressingStates=list()
        self.FinalStates=list()
        return
    
    def ResizeAndRestart(self,size):
        self.InitialState.Clear(size)
        self.ProgressingStates.clear()
        self.ProgressingStates.append(self.InitialState)
        self.FinalStates.clear()
        
    def Expand(self):
        First_State=self.ProgressingStates.pop(0)
        Next_States=First_State.NextStates()
        for New_State in Next_States:
            self.ProgressingStates.insert(0,New_State)
            
    def IsEmpty(self):
        return len(self.ProgressingStates)==0
    
    def IsFinalState(self):
        if self.ProgressingStates[0].IsFull()==True:
            Final_State=self.ProgressingStates.pop(0)
            
            if Final_State.CheckCorrectState()==True:
                
                self.FinalStates.append(Final_State)
            return True
        else:
            return False
    def IsGreedyEnd(self):
        return self.ProgressingStates[0].IsFull()
    
            
    def ReturnFinalStates(self):
        return self.FinalStates
            
    
    def Heuristic(self):
        First_State=self.ProgressingStates.pop(0)
        Next_States=First_State.NextStatesGreedy()
        #print(Next_States)
        MostPowerfulState=Next_States[0]
        for New_State in Next_States:
            if HeuristicComputation(New_State)>HeuristicComputation(MostPowerfulState):
                MostPowerfulState.setStateValues(New_State.getStateValues())
        self.ProgressingStates.append(MostPowerfulState)
        
    def ReturnProgress(self):
        return self.ProgressingStates
            
                