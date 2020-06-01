# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:12:48 2020

@author: Catalin
"""
import numpy as np
class Controller():
    def __init__(self,filename):
        self.data=self.loadData(filename)
        
    def loadData(self, filename):
        data = np.loadtxt(filename, dtype=np.float32)
        return data