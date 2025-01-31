# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:32:55 2020

@author: Catalin
"""
import math
import copy
import numpy
import csv
def check_function(sudoku,value):
    i=0
    line=[]
    columns=[[] for j in range(value)]
    square=[[]for i in range(math.sqrt(value))]
    while i<value*value:
        if i%(value*math.sqrt(value))==0:
            for i in range(int(math.sqrt(value))):
                square[i].clear()
        if i%value==0:
            line.clear()
        val=sudoku[i]
        if val in line:
            #print("Line")
            #print (line,val)
            return False
        
        elif val in columns[i%value]:
            #print("columns")
            #print(columns,val)
            return False
            
        else:
            which_square=0
            if value==4:
                if i%value>=2:
                    which_square=1
            else:
                if i%value>=6:
                    which_square=2
                else:
                    if i%value>=3:
                        which_square=1
            if val in square[which_square]:
                #print("Square ",which_square,i)
                #print(square[which_square],val)
                return False
            else:
            
                line.append(val)
                columns[i%value].append(val)
                square[which_square].append(val)
                i=i+1
    return True


def complete_sudoku(pick):
    
    print("Choose the hard-coded sudoku yes or no")
    choice=input()
    if choice=="yes":
        initial_sudoku=read_input(pick)
    else:
        print("Give ",pick*pick-1," values:")
        initial_sudoku=[]
        for i in range(0,pick*pick):
            initial_sudoku.insert(i,int(input()))
    ok=False
    print("Choose number of attempts")
    attempts=int(input())
    trials=0
    while trials<attempts:
        sudoku=copy.deepcopy(initial_sudoku)
        #print(sudoku9)
        i=0
        while i<=pick*pick-1:
            if sudoku[i]==0:
                num=numpy.random.randint(1,pick+1)
                sudoku[i]=num
            i=i+1
        ok=check_function(sudoku,pick)
        if ok==True:
            print("In trial: ",trials)
            for i in range(0,pick*pick):
                if i%pick==0:
                    print()
                print(sudoku[i],end=",")
            print()
            return 
        trials+=1
    if ok==False:
        print("No solution in ",attempts," trials")
        return
    
def read_input(value):
    array=[]
    with open("C:\\Users\\Catalin\\Desktop\\Faculty\\AI\\sudoku"+str(value)+".txt") as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        for row in csv_reader:
            #print(row)
            i=0
            prod=value*value
            while i<prod:
                array.append(int(row[i]))
                i=i+1

    print(array)
    return array
def SudokuStart():             
    numpy.random.seed()
    print("Pick 4 or 9")
    pick=int(input())
    complete_sudoku(pick)

        