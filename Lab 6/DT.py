# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:26:44 2020

@author: Catalin
"""
import csv
from numpy import random

class DT():
    def __init__(self):
        self.data=self.loadData()
        self.length=len(self.data)
        self.testingSize=100
        self.trainingData=list()
        self.testingData=list()
    
    def loadData(self):
        array=[]
        with open("C:\\Users\\Catalin\\Desktop\\Faculty\\AI\\Lab 6\\Data.txt") as csv_file:
            csv_reader=csv.reader(csv_file,delimiter=',')
            for row in csv_reader:
                rowData=list()
                for index in range(5):
                    if index != 0:
                        rowData.append(int(row[index]))
                    else:
                        rowData.append(row[0])
                array.append(rowData)
        return array
    
    def chooseData(self):
        self.trainingData.clear()
        self.testingData.clear()
        random.shuffle(self.data)
        for i in range(self.testingSize):
            self.testingData.append(self.data[i])
        for i in range(self.testingSize,self.length):
            self.trainingData.append(self.data[i])
                
    def startRun(self):
        self.chooseData()
        myTree = buildTree(self.trainingData)
        Correct=0
        Incorrect=0
        for row in self.testingData:
            #we build the solution as a dictionary,
            #since we will always have leaves with only one value predicted
            #if row[0] is in keys it means we predicted with 100% probability B,L or R
            if row[0] in classify(row, myTree).keys():
                Correct+=1
            else:
                Incorrect+=1
        #if Correct/self.testingSize*100<=70:
            #print("Acurracy: "+ str(Correct/self.testingSize*100))
        #if Correct/self.testingSize*100>=85:
            #print("Acurracy: "+ str(Correct/self.testingSize*100))
        return Correct/self.testingSize*100     
                

def classCounts(rows):
    """
    Counts the number of each type of final result in a dataset.
    """
    counts = {} 
    for row in rows:
        label = row[0]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

    
def partition(rows, column,comparingValue):
    """
    Partitions a dataset.
    For each row in the dataset, check if it answers the question or not,
    If it does add it to trueRows, otherwise falseRows.
    """
    trueRows, falseRows = [], []

    for row in rows:
        if comparingValue >= row[column]:
            trueRows.append(row)
        else:
            falseRows.append(row)
    return trueRows, falseRows
    
def gini(rows):
    """
    Calculate the Gini Impurity for a list of rows.
    I used the formula 1-(sum)prob^2
    """
    counts = classCounts(rows)
    impurity = 1
    for label in counts:
        labelProb = counts[label] / float(len(rows))
        impurity -= labelProb**2
    return impurity

def infoGain(left, right, currentUncertainty):
    """
    Information Gain.
    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return currentUncertainty - p * gini(left) - (1 - p) * gini(right)



def findBestSplit(rows):
    """
    Find the best question to ask by iterating over every feature / value
    and calculating the information gain.
    """
    bestGain = 0 
    bestCol = None
    bestVal = None 
    currentUncertainty = gini(rows)
    numFeatures = len(rows[0])  
    for col in range(1,numFeatures):
        values = set([row[col] for row in rows])  
        for val in values:      
            trueRows, falseRows = partition(rows, col, val)
            if len(trueRows) == 0 or len(falseRows) == 0:
                continue
            gain = infoGain(trueRows, falseRows, currentUncertainty)
            if gain > bestGain:
                bestGain, bestCol, bestVal = gain, col, val

    return bestGain, bestCol, bestVal
    
class Leaf:
    """
    A Leaf node classifies data.
    This holds a dictionary of class for example {B:5}
    """

    def __init__(self, rows):
        self.predictions = classCounts(rows)


class DecisionNode:
    """
    A Decision Node splits the data set in two branches based on a question.
    """

    def __init__(self,col,val,trueBranch,falseBranch):
        self.col =col
        self.val =val
        self.trueBranch = trueBranch
        self.falseBranch = falseBranch
    
def buildTree(rows):
    """
    Recursively build a tree by finding the question with the best gain
    And splitiing the tree in two by that question
    """
    gain, col, val = findBestSplit(rows)
    if gain == 0:
        return Leaf(rows)
    trueRows, falseRows = partition(rows, col, val)
    trueBranch = buildTree(trueRows)
    falseBranch = buildTree(falseRows)
    return DecisionNode(col,val, trueBranch, falseBranch)

def classify(row, node):
    """
    Recursively try classifying a row based on the tree build on the training data 
    """
    if isinstance(node, Leaf):
        return node.predictions
    #changing here to node.val>row[node.col] will make the accuracy raise to 88-90%
    #but i don't think it is correct 
    if node.val>=row[node.col]:
        return classify(row, node.trueBranch)
    else:
        return classify(row, node.falseBranch)





