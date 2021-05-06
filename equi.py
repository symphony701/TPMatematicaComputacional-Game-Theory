
import sys
import equilibrios
from PyQt5 import uic
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QDialog,QGridLayout,QGroupBox,QVBoxLayout,QFormLayout,QLabel
import math
import random

class Ventana(QDialog):
    def __init__(self,matrizProcesada,conjuntoSolucion):
        QDialog.__init__(self)
        uic.loadUi("equilibrios.ui",self)
        self.matriz = matrizProcesada
        self.conjuntoSolucion = conjuntoSolucion
        impresion = "Conjunto Solucion = { "
        for i in range(len(self.conjuntoSolucion)):
            elemento = str(self.conjuntoSolucion[i][0])
            impresion += elemento
            impresion += " "
            
        impresion += "}"
        
        self.label.setText(impresion)
            

