# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:25:42 2020

@author: Catalin
"""
from Problem import Problem
from Controller import Controller
class UI:
    
    def __init__(self):
        self.problem = Problem("temperature.in", "capacity.in", "power.in","rules.in")
        self.controller = Controller(self.problem)

    def StartMenu(self):
        Temp = int(input("Choose the temperature(20,120):\n"))
        Cap = int(input("Choose the capacity(0,10):\n"))
        self.controller.solve(Temp,Cap)
UI=UI()
UI.StartMenu()
