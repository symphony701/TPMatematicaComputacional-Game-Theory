import sys
import mainwindow
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication,QPushButton,QDialog,QGridLayout,QGroupBox,QVBoxLayout
from ventanaPrincipal import Main

    
if __name__ == "__main__":
    a=QtWidgets.QApplication(sys.argv)
    app=Main()
    app.show()
    a.exec_()
        