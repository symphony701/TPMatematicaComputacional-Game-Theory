
import sys
import equilibrios
from PyQt5 import uic
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QDialog,QGridLayout,QGroupBox,QVBoxLayout,QFormLayout,QLabel
import math
import random
import numpy as np

class Ventana(QDialog):
    def __init__(self,matrizProcesada,conjuntoSolucion=[],mixtas=True,resultadoMixtas=""):
        QDialog.__init__(self)
        uic.loadUi("equilibrios.ui",self)
        self.matriz = matrizProcesada
        self.conjuntoSolucion = conjuntoSolucion
        self.pushButton.clicked.connect(self.close)
        if mixtas==True:
            
            impresion = "Conjunto Solucion = { "
            for i in range(len(self.conjuntoSolucion)):
                #Cambiar aqui si no funcionan las demas xd
                elemento = str(self.conjuntoSolucion[i])
                impresion += elemento
                impresion += " "
                
            impresion += "}"
        
        elif mixtas==False:
            impresion = "Conjunto Solucion = { "
            impresion += resultadoMixtas
            impresion += "}"
        
        self.label.setText(impresion)
            
    def pintarMatriz(self,dimensionx,dimensiony):
        for i in range(dimensionx):
            for j in range(dimensiony):
                csm = QtWidgets.QLabel(str(self.matriz[i,j]))
                csm.setStyleSheet("color:black;border-radius:4px;border-color: white;background-color:#d1d8e0;")
                csm.setAlignment(QtCore.Qt.AlignCenter)
                self.gridLayout.addWidget(csm,i,j)
                
