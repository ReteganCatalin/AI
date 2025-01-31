# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:59:35 2020

@author: Catalin
"""

import numpy as np
from random import randint
from math import sin, cos
from numpy.random.mtrand import choice
from Classifier import Classifier


from Node import Node

DEPTH_MAX = 7

class Chromosome():
    def __init__(self, d=DEPTH_MAX):
        self.fitness = 0
        self.root = Node()
        self.root.init(d)

    def evaluate(self, inputTraining, outputTraining):
        self.fitness = 0
        exp = str(self.root)
        count=0
        for (x, y) in zip(inputTraining, outputTraining):
            for index in range(len(x)):
                from Controller import HEADER
                exec("{} = {}".format(HEADER[index], x[index]))
            res = eval(exp)
            if Classifier.classify(res) == y:
                count += 1
        self.fitness = float(count / len(inputTraining) * 100)
        if self.fitness==100:
            for (x, y) in zip(inputTraining, outputTraining):
                for index in range(len(x)):
                    #from Controller import HEADER
                    exec("{} = {}".format(HEADER[index], x[index]))
                res = eval(exp)
                print(Classifier.classify(res)+"=="+y)
                if Classifier.classify(res) == y:
                    count += 1
        return self.fitness
    
    def predict(self, inputData):
        exp = str(self.root)
        for i in range(len(inputData)):
            from Controller import HEADER
            exec("{} = {}".format(HEADER[i], inputData[i]))
        return eval(exp)


    def crossover(ch1, ch2, crossoverProbability):
        if crossoverProbability>np.random.rand():
            node1 = choice(ch1.root.getNodes())
            node2 = choice(ch2.root.getNodes())
            c = Chromosome()
            if ch1.root == node1:  # if we must change the whole tree
                c.root = node2.deepcopy()
            else:
                c.root = Node()
                c.root.change(ch1.root, node1, node2)
            return c
        return ch1

    def mutate(self, mutationProbability):
        if mutationProbability>np.random.rand():
            pos = randint(1, self.root.size)
            self.root.mutate(pos,DEPTH_MAX)
