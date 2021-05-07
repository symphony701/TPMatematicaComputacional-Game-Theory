import sys
import errorMessage
from PyQt5 import uic
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QDialog,QGridLayout,QGroupBox,QVBoxLayout,QFormLayout,QLabel

class Nosotrosuwu(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("integrantes.ui",self)
        