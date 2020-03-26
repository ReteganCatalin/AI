# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:42:35 2020

@author: Catalin
"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QFormLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QVBoxLayout)
import pyqtgraph as pq
from Controller import Controller

class EAInterface(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.formGroupBox = QGroupBox("Evolutionary Algorithm Options:")
        layout = QFormLayout()
        
        
        self.permutationLabel = QLabel("The size of the permutation:")
        self.permutationInput = QLineEdit()

        self.populationLabel = QLabel("Population:")
        self.populationInput = QLineEdit()

        self.iterationNumberLabel = QLabel("Number Of Iterations:")
        self.iterationNumberInput = QLineEdit()

        self.mutationProbabilityLabel = QLabel("Mutation Probability")
        self.mutationProbabilityInput = QLineEdit()
        
        layout.addRow(self.permutationLabel, self.permutationInput)
        layout.addRow(self.populationLabel, self.populationInput)
        layout.addRow(self.iterationNumberLabel, self.iterationNumberInput)
        layout.addRow(self.mutationProbabilityLabel, self.mutationProbabilityInput)

        startAlgorithmButton = QPushButton("Start Algorithm")
        startAlgorithmButton.clicked.connect(self.startAlgorithm)

        stopAlgorithmButton = QPushButton("Stop Algorithm")
        stopAlgorithmButton.clicked.connect(self.stopAlgorithm)

        layout.addRow(startAlgorithmButton)
        layout.addRow(stopAlgorithmButton)

        self.formGroupBox.setLayout(layout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Pick stats for EA ")
        self.graphWindow = self.GraphWindow()
        self.show()

    def startAlgorithm(self):
        print("Evolution algorithm starting")
        self.graphWindow.show()
        permutationNumber = int(self.permutationInput.text())
        populationNumber = int(self.populationInput.text())
        iterationNumber = int(self.iterationNumberInput.text())
        probabilityMutation = float(self.mutationProbabilityInput.text())
        self.controller=Controller(permutationNumber,populationNumber, iterationNumber, probabilityMutation)
        
        self.thread = self.WorkerThread(self.controller)
        self.thread.addGenerationSignal.connect(self.displayGraph)
        self.thread.start()

    def stopAlgorithm(self):
        print("Stopping Algorithm")
        self.graphWindow.clearMyGraph()
        if self.thread.isRunning():
            self.thread.stop()
            self.thread.exit()

    def displayGraph(self,first,second):
        self.graphWindow.updateTheGraph(first,second)

    class GraphWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Plotter ")
            layout = QFormLayout()
            self.myPlot = pq.PlotWidget(self)
            self.myPlot.resize(1500,1200)
            
            layout.addRow(self.myPlot)
            self.label = QLabel()
            self.label.resize(200,200)
            layout.addRow(self.label)
            self.setLayout(layout)

        def updateTheGraph(self,bestIndividuals,listOfIndices):
            self.myPlot.plot(listOfIndices,bestIndividuals)
            self.label.setText("Best fitness: "+str(bestIndividuals[len(bestIndividuals)-1]))

        def clearMyGraph(self):
            pass

    class WorkerThread(QThread):

        addGenerationSignal = pyqtSignal(list,list)

        def __init__(self, workerController=None):
            QThread.__init__(self)
            self.workerController = workerController
            self.shouldContinue = True

        def __del__(self):
            self.wait()

        def stop(self):
            self.shouldContinue = False

        def run(self):
            
            bestIndividualsOfEachGeneration = []
            numericalListOfIndividuals = []

            for index in range(self.workerController.getNumberOfIterations()):
                if self.shouldContinue is not True:
                    return
                if index % 100 == 0:
                    #print("Current generation: " + str(index))
                    BestIndividualOfThisGenerations=self.workerController.getMinFitness()
                    bestIndividualsOfEachGeneration.append(BestIndividualOfThisGenerations[len(BestIndividualOfThisGenerations)-1])
                    numericalListOfIndividuals.append(index)
                    self.addGenerationSignal.emit(bestIndividualsOfEachGeneration,numericalListOfIndividuals)
                self.workerController.NextIteration()
                
            BestIndividualOfThisGenerations=self.workerController.getMinFitness()
            bestIndividualsOfEachGeneration.append(BestIndividualOfThisGenerations[len(BestIndividualOfThisGenerations)-1])
            numericalListOfIndividuals.append(self.workerController.getNumberOfIterations())
            self.addGenerationSignal.emit(bestIndividualsOfEachGeneration,numericalListOfIndividuals)
            bestIndividuals =self.workerController.getMinFitness()
            bestIndividual=bestIndividuals[len(bestIndividuals)-1]
            print("The best individual fitness is " + str(bestIndividual))
            print("\n\n\n")
            print(bestIndividualsOfEachGeneration)