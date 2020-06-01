# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:50:50 2020

@author: Catalin
"""

from CNN import CNN

class UI:
    def __init__(self):
        self.CNN=CNN()
        
    def Start(self):
        
        while(True):
            choice=input("1-Run,2-Exit\n")
            if(choice=='1'):
                self.CNN.ReInitCNN()
                epochNo=int(input("Number of epochs(try 12)\n"))
                batchSize=int(input("Batch size\n"))
                score=self.CNN.ModelStart(epochNo,batchSize)
                print('loss=', score[0]) 
                print('accuracy=', score[1])
            else:
                return
            
UI=UI()
UI.Start()