# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:55:55 2020

@author: Catalin
"""

import sys

from PyQt5.QtWidgets import QApplication, QInputDialog
from EAInterface import EAInterface
from HCInterface import HCInterface
from PSOInterface import PSOInterface


class InterfaceChoose(QInputDialog):

    def __init__(self):
        super().__init__()
        self.show()

    def pickInterface(self):
        
        items = ["Evolutionary Algorithm", "Particle Swarm Optimization", "Hill Climbing"]
        
        item, ok = QInputDialog().getItem(self, "Pick your algorithm",
                                          "Algorithms:", items, 0, False)
        if ok:
            return item




if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    chooser = InterfaceChoose()
    userPick = chooser.pickInterface()
    if userPick == "Evolutionary Algorithm":
        ex = EAInterface()
    elif userPick == "Particle Swarm Optimization":
        ex = PSOInterface()
    elif userPick == "Hill Climbing":
        ex = HCInterface()
    sys.exit(app.exec_())