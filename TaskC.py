# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:22:51 2020

@author: Catalin
"""
import CrypthArithmetic
import GeometricForms
import SudokuGame
def menu():
    while True:
        print("Choose 1-Sudoku game,2-CrypthArithmetic Game,3-Geometric Forms,Exit-Leave")
        pick=input()
        if pick=='2':
            CrypthArithmetic.CrypthArithmeticStart()
        elif pick=='1':
            SudokuGame.SudokuStart()
        elif pick=='3':
            GeometricForms.Board()
        else:
            return
menu()