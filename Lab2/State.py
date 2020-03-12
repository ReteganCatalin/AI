# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 12:58:34 2020

@author: Catalin
"""
import copy


class State:
    

    def __init__(self):
        self.__size=0
        self.__values = []
        
    def Clear(self,new_size):
        self.__size=new_size
        self.__values.clear()

    def setValues(self, values):
        self.__values = values[:]
        
    def getSize(self):
        return self.__size
    
    def setSize(self,new_size):
        self.__size=new_size
        
    def getStateValues(self):
        return self.__values[:]

    def __str__(self):
        s = 'Queens on positions: '
        for point in self.__values:
            s+=str(point)+","
        return s
    
    def IsFull(self):
        if len(self.__values)!=self.__size:
            return False
        return True
        
    def NextStates(self):
        next_states=list()
        for index_row in range(0,self.__size):
            for index_column in range(0,self.__size):
                point=(index_row,index_column)
                if point not in self.__values:
                    next_states.append(self.NewState(point))
        return next_states
    
    def CheckCorrectState(self):
        line=[0 for i in range(0,self.__size)]
        column=[0 for i in range(0,self.__size)]
        
        if len(self.__values)!=self.__size:
            return False
        else:
            length=len(self.__values)
            for index in range(0,length):
                point=self.__values[index]
                line[point[0]]+=1
                column[point[1]]+=1
                if column[point[1]]!=1 or line[point[0]]!=1:
                    return False
                else:
                    for index2 in range(index+1,length):
                        if (abs(point[0]-self.__values[index2][0])- abs(point[1]-self.__values[index2][1]))==0:
                            return False
                        if point[0]>self.__values[index2][0]:
                            return False
            return True

    def NewState(self, point):
        new_state=State()
        Copy=copy.deepcopy(self.__values)
        Copy.append(point)
        new_state.setValues(Copy)
        new_state.setSize(self.__size)
        return new_state