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

    def setStateValues(self, values):
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
                    New_State=self.NewState(point)
                    if IncreasingOrder(New_State):
                        next_states.append(New_State)
        return next_states
    
    def NextStatesGreedy(self):
        next_states=list()
        for index_row in range(0,self.__size):
            for index_column in range(0,self.__size):
                point=(index_row,index_column)
                if point not in self.__values:
                    New_State=self.NewState(point)
                    next_states.append(New_State)
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
            return True

    def NewState(self, point):
        new_state=State()
        Copy=copy.deepcopy(self.__values)
        Copy.append(point)
        new_state.setStateValues(Copy)
        new_state.setSize(self.__size)
        return new_state
    
def IncreasingOrder(State):
    values=State.getStateValues()
    length=len(values)
    for index in range(0,length):
        point=values[index]
        for index2 in range(index+1,length):
            #print(point)
            #print(values[index2])
            if point[0]>values[index2][0]:
                return False
            if point[0]==values[index2][0]:
                if point[1]>values[index2][1]:
                    return False
    return True


def HeuristicComputation(State):
   
    size=State.getSize()
    lines=[0 for i in range(size)]
    columns=[0 for i in range(size)]
    matrix=[[0 for i in range(size)] for j in range(size)]
    power=0
    values=State.getStateValues()
    length=len(values)
    for index in range(0,length):
        point=values[index]
        for pos in range(size):
            matrix[point[0]][pos]=1
            matrix[pos][point[1]]=1
            if point[1]+pos<size and point[0]-pos>-1:
                matrix[point[0]-pos][point[1]+pos]=1
            if point[1]-pos>-1 and point[0]-pos>-1:
                matrix[point[0]-pos][point[1]-pos]=1
            if point[1]-pos>-1 and point[0]+pos<size:
                matrix[point[0]+pos][point[1]-pos]=1
            if point[1]+pos<size and point[0]+pos<size:
                matrix[point[0]+pos][point[1]+pos]=1
    for row in range(size):
        for column in range(size):
            if matrix[row][column]==0:
                power+=50
    for index in range(0,length):
        point=values[index]
        lines[point[0]]+=1
        columns[point[1]]+=1
        if columns[point[1]]!=1 or lines[point[0]]!=1:
            power-=1000
        else:
            for index2 in range(index+1,length):
                if (abs(point[0]-values[index2][0])- abs(point[1]-values[index2][1]))==0:
                    power-=2000
    return power
    