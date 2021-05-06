# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 717)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background:Coral;\n"
"}\n"
"\n"
"QWidget{\n"
"    background:#25252A;\n"
"}\n"
"QPushButton{\n"
"\n"
"    color:white;\n"
"    background-color:rgb(255,0,68);\n"
"    font:57 11pt \"Ubuntu\";\n"
"    border-radius:4px;\n"
"    letter-spacing: 2px;\n"
"    font-size:18px;\n"
"\n"
"    font-weight: bold\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color:#25252A;\n"
"    border-color: #2d98da;\n"
"    border-width : 2px;\n"
"    border-style:inset;\n"
"    \n"
"}\n"
"QLabel{\n"
"    color:white;\n"
"}\n"
"QSpinBox{\n"
"    color:white;\n"
"    border-color:white;\n"
"    background:#4b6584;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 451, 311))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 70, 211, 71))
        self.pushButton.setStyleSheet(".pushButton_2{\n"
"    background-color:blue;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 380, 211, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(110, 380, 44, 26))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 350, 67, 17))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 350, 101, 17))
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(260, 380, 44, 26))
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(770, 70, 211, 71))
        self.pushButton_3.setStyleSheet(".pushButton_2{\n"
"    background-color:blue;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 220, 211, 71))
        self.pushButton_4.setStyleSheet(".pushButton_2{\n"
"    background-color:blue;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 440, 281, 91))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(690, 590, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Eliminar Dominadas"))
        self.pushButton_2.setText(_translate("MainWindow", "Reiniciar Matriz"))
        self.label.setText(_translate("MainWindow", "Filas:"))
        self.label_2.setText(_translate("MainWindow", "Columnas:"))
        self.pushButton_3.setText(_translate("MainWindow", "ENSP"))
        self.pushButton_4.setText(_translate("MainWindow", "Estrategias Mixtas"))
        self.pushButton_5.setText(_translate("MainWindow", "Agregar Filas y Columnas"))
        self.pushButton_6.setText(_translate("MainWindow", "About Us"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())