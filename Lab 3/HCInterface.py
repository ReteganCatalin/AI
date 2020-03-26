# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:49:42 2020

@author: Catalin
"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QFormLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QVBoxLayout)
import pyqtgraph as pq
from Controller import Controller

class HCInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.formGroupBox = QGroupBox("Hill Climbing Options:")
        layout = QFormLayout()
        
        
        self.permutationLabel = QLabel("The size of the permutation:")
        self.permutationInput = QLineEdit()

        self.iterationNumberLabel = QLabel("Maximum number of iterations(might not get there):")
        self.iterationNumberInput = QLineEdit()

        
        layout.addRow(self.permutationLabel, self.permutationInput)
        layout.addRow(self.iterationNumberLabel, self.iterationNumberInput)

        startClimbingButton = QPushButton("Start Climbing")
        startClimbingButton.clicked.connect(self.startClimbing)

        stopClimbingButton = QPushButton("Stop Climbing")
        stopClimbingButton.clicked.connect(self.stopClimbing)

        layout.addRow(startClimbingButton)
        layout.addRow(stopClimbingButton)

        self.formGroupBox.setLayout(layout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Pick stats for HC ")
        self.graphWindow = self.GraphWindow()
        self.show()

    def startClimbing(self):
        print("Hill Climbing starting")
        self.graphWindow.show()
        permutationNumber = int(self.permutationInput.text())
        population=1
        iterationNumber = int(self.iterationNumberInput.text())
        mutationProbability=0
        self.controller=Controller(permutationNumber,population,iterationNumber,mutationProbability)
        self.thread = self.WorkerThread(self.controller)
        self.thread.addGenerationSignal.connect(self.displayGraph)
        self.thread.start()

    def stopClimbing(self):
        print("Hill climbing stoping")
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

        def updateTheGraph(self,Individual,listOfIndices):
            self.myPlot.plot(listOfIndices,Individual)
            self.label.setText("Last individual fitness: "+str(Individual[len(Individual)-1]))

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
            
            bestIndividualOfEachGeneration = []
            numericalListOfIndividuals = []

            for index in range(self.workerController.getNumberOfIterations()):
                print("Current generation: " + str(index))
                bestIndividualOfEachGeneration.append(self.workerController.getLastFitness())
                numericalListOfIndividuals.append(index)
                self.addGenerationSignal.emit(bestIndividualOfEachGeneration,numericalListOfIndividuals)
                ok=self.workerController.NextClimb()
                if ok==False:
                    bestIndividualFitness =self.workerController.getLastFitness()
                    bestIndividualOfEachGeneration.append(self.workerController.getLastFitness())
                    numericalListOfIndividuals.append(index)
                    self.addGenerationSignal.emit(bestIndividualOfEachGeneration,numericalListOfIndividuals)
                    print("The best at least local minimum " + str(bestIndividualFitness) + " found in iteration number: " + str(index))
                    return
            bestIndividualFitness =self.workerController.getLastFitness()
            print("The best individual fitness found is " + str(bestIndividualFitness))