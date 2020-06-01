# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:26:28 2020

@author: Catalin
"""

from DT import DT
class Controller:
    def __init__(self,nrOfRuns):
        self.nrOfRuns=nrOfRuns
        self.DT=DT()
    
    def RunAlg(self):
        average=0
        maximum=0
        for i in range(self.nrOfRuns):
            new_accuracy=self.DT.startRun()
            average+=new_accuracy
            if maximum<new_accuracy:
                maximum=new_accuracy
        return average/self.nrOfRuns,maximum  