# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:50:20 2020

@author: Catalin
"""

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QWidget, QFormLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QVBoxLayout)
import pyqtgraph as pq
from Controller import PSOController

class PSOInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.formGroupBox = QGroupBox("Particle Swarm Optimization Options:")
        layout = QFormLayout()
        
        
        self.permutationLabel = QLabel("The size of the permutation:")
        self.permutationInput = QLineEdit()

        self.iterationNumberLabel = QLabel("Maximum number of iterations:")
        self.iterationNumberInput = QLineEdit()
        
        self.populationLabel = QLabel("Population:")
        self.populationInput = QLineEdit()

        self.minimumLabel = QLabel("Minimum boundary:")
        self.minimumInput = QLineEdit()

        self.maximumLabel = QLabel("Maximum boundary:")
        self.maximumInput = QLineEdit()

        self.cognitiveLearningLabel = QLabel("Cognitive learning coefficient")
        self.cognitiveLearningInput = QLineEdit()
        
        self.socialLearningLabel = QLabel("Social learning coefficient")
        self.socialLearningInput = QLineEdit()
        
        self.inertiaLabel = QLabel("Inertia coefficieni")
        self.inertiaInput = QLineEdit()
        
        layout.addRow(self.permutationLabel, self.permutationInput)
        layout.addRow(self.populationLabel, self.populationInput)
        layout.addRow(self.iterationNumberLabel, self.iterationNumberInput)
        layout.addRow(self.cognitiveLearningLabel, self.cognitiveLearningInput)
        layout.addRow(self.socialLearningLabel, self.socialLearningInput)
        layout.addRow(self.inertiaLabel, self.inertiaInput)

        startSwarmingButton = QPushButton("Start Swarming")
        startSwarmingButton.clicked.connect(self.startSwarming)

        stopSwarmingButton = QPushButton("Stop Swarming")
        stopSwarmingButton.clicked.connect(self.stopSwarming)

        layout.addRow(startSwarmingButton)
        layout.addRow(stopSwarmingButton)

        self.formGroupBox.setLayout(layout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Pick stats for PSO ")
        self.graphWindow = self.GraphWindow()
        self.show()

    def startSwarming(self):
        print("Swarming starting")
        self.graphWindow.show()
        permutationNumber = int(self.permutationInput.text())
        population= int(self.permutationInput.text())
        iterationNumber = int(self.iterationNumberInput.text())
        cognitiveLearning = int(self.cognitiveLearningInput.text())
        socialLearning = int(self.socialLearningInput.text())
        inertia= int(self.inertiaInput.text())
        
        self.controller=PSOController(permutationNumber,population,iterationNumber,cognitiveLearning,socialLearning,inertia)
        self.thread = self.WorkerThread(self.controller)
        self.thread.addGenerationSignal.connect(self.displayGraph)
        self.thread.start()

    def stopSwarming(self):
        print("Swarming stoping")
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