# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:24:47 2020

@author: Catalin
"""
import numpy as np
import matplotlib as mpl
from copy import deepcopy
class ANN():
        
    def __init__(self,filename):
        self.loadData(filename)
        self.data=self.normaliseData()
        self.learning_rate=0.0001
        np.random.seed(1)
        self.weights1   = np.random.rand(self.data.shape[1]-1,6) 
        self.weights2   = np.random.rand(6,1)
        self.loss=[]
  
    def loadData(self, filename):
        self.data = np.loadtxt(filename, dtype=np.float32)
          
    def normaliseData(self):
        return (self.data - self.data.min())/(self.data.max()-self.data.min())

    def linearFunction(self, X):
        return X

    def linearFunctionDerivative(self,X):
        return 1
        
    def reset(self):
        self.weights1   = np.random.rand(self.data.shape[1]-1,6) 
        self.weights2   = np.random.rand(6,1)
        self.loss=[]
    
    def splitData(self):
        self.X = deepcopy(self.data[:, 0:-1])
        self.Y = deepcopy(self.data[:, [-1]])

    def feedforward(self):
        self.hidden_layer = self.linearFunction(np.dot(self.X, self.weights1))
        self.output = self.linearFunction(np.dot(self.hidden_layer, self.weights2))
    
    def backPropagation(self):
        d_weights2 = np.dot(self.hidden_layer.T, (2*(self.Y - self.output) *
                            self.linearFunctionDerivative(self.output)))
           
        d_weights1 = np.dot(self.X.T,  (np.dot(2*(self.Y -
                        self.output) * self.linearFunctionDerivative(self.output),
                        self.weights2.T) *
                        self.linearFunctionDerivative(self.hidden_layer)))
        # update the weights with the derivative (slope) of the loss function
        
        self.weights1 += self.learning_rate * d_weights1
        self.weights2 += self.learning_rate * d_weights2
        suming=0
        for i in range(len(self.output)):
            suming+=(self.Y[i] - self.output[i])**2
        self.loss.append(suming/len(self.Y))
    def train(self, training_iterations):
        """
        We train the model through trial and error, adjusting the
        synaptic weights each time to get a better result
        """
        self.splitData()
        self.reset()
        self.iterations=[]
        for iteration in range(training_iterations):
            self.feedforward()
            self.backPropagation()
            self.iterations.append(iteration)
        self.plot()
    
    def plot(self):
        for i in range(len(self.output)):
            print("Actual value:"+str(self.Y[i])+"Predicted Value:"+str(self.output[i]))
        print(self.loss)
        mpl.pyplot.plot(self.iterations, self.loss, label='loss value vs iteration')
        mpl.pyplot.xlabel('Iterations')
        mpl.pyplot.ylabel('loss function')
        mpl.pyplot.legend()
        mpl.pyplot.show()
    
            

    
    