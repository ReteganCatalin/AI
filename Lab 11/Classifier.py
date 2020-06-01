# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:55:19 2020

@author: Catalin
"""

class Classifier:
    def classify(value):
        if value <= -5:
            return 'Slight-Right-Turn'
        elif -5 < value <= 0:
            return 'Sharp-Right-Turn'
        elif 0 < value <= 5:
            return 'Move-Forward'
        else:
            return 'Slight-Left-Turn'