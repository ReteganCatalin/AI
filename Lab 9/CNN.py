# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:51:11 2020

@author: Catalin
"""


import matplotlib as mpl
import keras  
from keras.datasets import mnist 
from keras.models import Model 
from keras.layers import Dense, Input
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten 
from keras import backend as k 


class CNN:
    
    def __init__(self):
        return
        
    
    def ReInitCNN(self):        
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data() 
        self.img_rows, self.img_cols=28, 28
        self.Reshaping()
        self.Categories()
        self.CNNModel()
        
    def Reshaping(self):
        if k.image_data_format() == 'channels_first': 
           self.x_train = self.x_train.reshape(self.x_train.shape[0], 1, self.img_rows, self.img_cols) 
           self.x_test = self.x_test.reshape(self.x_test.shape[0], 1, self.img_rows, self.img_cols) 
           self.inpx = (1, self.img_rows, self.img_cols)          
        else: 
           self.x_train = self.x_train.reshape(self.x_train.shape[0], self.img_rows, self.img_cols, 1) 
           self.x_test = self.x_test.reshape(self.x_test.shape[0], self.img_rows, self.img_cols, 1) 
           self.inpx = (self.img_rows, self.img_cols, 1) 
          
        self.x_train = self.x_train.astype('float32') 
        self.x_test = self.x_test.astype('float32') 
        self.x_train /= 255
        self.x_test /= 255
        
    def Categories(self):   
        self.y_train = keras.utils.to_categorical(self.y_train)
        self.y_test = keras.utils.to_categorical(self.y_test)
        
    def CNNModel(self):
        self.inpx = Input(shape=self.inpx) 
        self.layer1 = Conv2D(32, kernel_size=(3, 3), activation='relu')(self.inpx) 
        self.layer2 = Conv2D(64, (3, 3), activation='relu')(self.layer1) 
        self.layer3 = MaxPooling2D(pool_size=(3, 3))(self.layer2) 
        self.layer4 = Dropout(0.5)(self.layer3) 
        self.layer5 = Flatten()(self.layer4) 
        self.layer6 = Dense(250, activation='sigmoid')(self.layer5) 
        self.layer7 = Dense(10, activation='softmax')(self.layer6) 
        
    def ModelStart(self,epochNo,batchSize):
        self.model = Model([self.inpx], self.layer7) 
        self.model.compile(optimizer=keras.optimizers.Adadelta(), 
              loss=keras.losses.categorical_crossentropy, 
              metrics=['accuracy']) 
  
        history=self.model.fit(self.x_train, self.y_train, epochs=epochNo, batch_size=batchSize) 
        self.epochIter=[]
        for i in range(0,self.epochNo):
            self.epochIter.append(i)
        mpl.pyplot.plot(self.epochIter, history.history["loss"], label='loss value vs epoch')
        mpl.pyplot.xlabel('Epoch')
        mpl.pyplot.ylabel('loss function')
        mpl.pyplot.legend()
        mpl.pyplot.show()
        return self.model.evaluate(self.x_test, self.y_test, verbose=0) 
        
        
        


        
    


    

