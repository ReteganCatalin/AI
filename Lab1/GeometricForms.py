# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:13:04 2020

@author: Catalin
"""

import numpy
import csv
import copy


class GeometricForm:
    def __init__(self,rows,columns,formNum):
        self.__schema=[[0 for j in range(columns)] for i in range(rows)]
        self.__rows=rows
        self.__columns=columns
        self.__size=0
        self.__formNum=formNum
        self.__read()
        
    def __read(self):
        with open("C:\\Users\\Catalin\\Desktop\\Faculty\\AI\\geometricForm"+str(self.__formNum)+".txt") as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=' ')
            i=0
            j=0
            for row in csv_reader:
                j=0
                for digit in row:
                    self.__schema[i][j]+=int(digit)*self.__formNum
                    if digit=="1":
                        self.__size+=1
                    j+=1
                i+=1
    def print(self):
        print(self.__schema)
        
    def formSize(self):
        return self.__size
        
    def add(self,other_matrix,row_pos,column_pos):
        #print(row_pos,column_pos)
        for index in range(len(other_matrix)):
            for column in range(len(other_matrix[index])):
                if index+row_pos<self.__rows and column+column_pos<self.__columns:
                    other_matrix[index+row_pos][column+column_pos]+=self.__schema[index][column]
        return other_matrix
            
        
class Board:
    
    def __init__(self):
        self.attempts=int(input("Number of attempts:"))
        self.__rows=0
        self.__columns=0
        self.__read()
        self.__schema=[[0 for j in range(self.__columns)] for i in range(self.__rows)]
        self.GeometricForms=list()
        for i in range(1,6):    
            self.GeometricForms.append(GeometricForm(self.__rows,self.__columns,i))
        self.__solve()
        
    def __read(self):
        with open("C:\\Users\\Catalin\\Desktop\\Faculty\\AI\\geometricForm.txt") as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                self.__rows=int(row[0])
                self.__columns=int(row[1])
    def __solve(self):
        numpy.random.seed()
        ok=False
        trials=0
        size=0
        print(self.__rows)
        print(self.__columns)
        for i in range(5):
            size+=self.GeometricForms[i].formSize()
            #self.GeometricForms[i].print()
        while trials<self.attempts and ok==False:
            matrix=copy.deepcopy(self.__schema)
            for i in range(5):
                matrix=self.GeometricForms[i].add(matrix,numpy.random.randint(0,self.__rows),numpy.random.randint(0,self.__columns))
            filled=0
            for index in range(len(matrix)):
                for column in range(len(matrix[index])):
                    if matrix[index][column]!=0:
                        filled+=1
            if size==filled:
                ok=True
                for row in matrix:
                    print(row)
                print("After trials number:",trials)
            trials+=1
            #print(matrix)
        if ok==False:
            print("Fail")
            
#SBoard(100000)
                    
            