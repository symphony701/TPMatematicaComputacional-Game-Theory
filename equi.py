
import sys
import equilibrios
from PyQt5 import uic
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QDialog,QGridLayout,QGroupBox,QVBoxLayout,QFormLayout
import math
import random

class Ventana(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("equilibrios.ui",self)

