import sys
import mainwindow
from PyQt5 import uic
from equi import Ventana
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QDialog,QGridLayout,QGroupBox,QVBoxLayout
from programa import Nash
from errorMess import Error
from integrante import Nosotrosuwu
import math
import random
import numpy as np


class Main(QtWidgets.QMainWindow,mainwindow.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        
        self.diagrama = self.gridLayoutWidget
        self.pushButton_5.clicked.connect(self.agregarDimensiones)
        self.pushButton.clicked.connect(self.eliminarDominadas)
        self.pushButton_2.clicked.connect(self.reiniciarMatriz)
        self.pushButton_3.clicked.connect(self.ensp)
        self.pushButton_4.clicked.connect(self.extrategiasMixtas)
        self.pushButton_6.clicked.connect(self.aboutUs)
        self.spinBox.setMinimum(1)
        self.spinBox_2.setMinimum(1)
        
        
        
    def agregarDimensiones(self):
        
        self.arreglo=[]
        
        for i in range(self.spinBox.value()):
            for j in range(self.spinBox_2.value()):
                csm = QtWidgets.QLineEdit("")
                csm.setStyleSheet("color:black;border-radius:4px;border-color: white;background-color:#d1d8e0;")
                self.gridLayout.addWidget(csm, i, j)
                self.arreglo.append(csm)
                
        
    def procesar(self):
        self.arr2 = []
        
        for i in self.arreglo:
            numero=""
            for j in str(i.text()):
                if j==',' or j=='.':
                    self.arr2.append(int(numero))
                    numero=""
                else:
                    numero +=j
            self.arr2.append(int(numero))
          
        
            
       
    def ensp(self):
        self.procesar()
        
        nash = Nash(self.spinBox.value(),self.spinBox_2.value(),self.arr2)
        matrizProcesada,conjuntoSolucion = nash.justpuras()
        dimensionx = self.spinBox.value()
        dimensiony = self.spinBox_2.value()
        self.vent=Ventana(matrizProcesada,conjuntoSolucion)
        self.vent.pintarMatriz(dimensionx,dimensiony)
        self.vent.exec_()
            
        
    def eliminarDominadas(self):
        self.procesar()
        
        
        try:
            nash = Nash(self.spinBox.value(),self.spinBox_2.value(),self.arr2)
            matrizProcesada,conjuntoSolucion,dimensionx,dimensiony = nash.eliminarDominadas()
            self.vent=Ventana(matrizProcesada,conjuntoSolucion)
            self.vent.pintarMatriz(dimensionx,dimensiony)
            self.vent.exec_()
        except Exception as ex:
            print(ex)
            self.error = Error()
            self.error.exec_()
        
        
        
        
    def extrategiasMixtas(self):
        self.procesar()
        
        try:
            nash = Nash(self.spinBox.value(),self.spinBox_2.value(),self.arr2)
            matrizProcesada,resultado,dimensionx,dimensiony = nash.mixtas()
            print(matrizProcesada)
            self.vent=Ventana(matrizProcesada,[],False,resultado)
            self.vent.pintarMatriz(dimensionx,dimensiony)
            self.vent.exec_()
            
        except Exception as ex:
            self.error = Error()
            self.error.exec_()
        
        
    def reiniciarMatriz(self):
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.spinBox.setValue(1)
        self.spinBox_2.setValue(1)
    def aboutUs(self):
        self.nosotros = Nosotrosuwu()
        self.nosotros.exec_()
        