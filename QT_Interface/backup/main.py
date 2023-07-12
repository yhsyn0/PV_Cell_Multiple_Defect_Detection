# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtUi.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import cv2, pickle, socket, struct, signal, sys, os
from QT_Interface.VideoThreadOld import VideoThread
from cv2 import VideoCapture

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Beamero View")
        MainWindow.resize(1848, 1017)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        iconExpand = QtGui.QIcon()
        iconExpand.addPixmap(QtGui.QPixmap("/home/azarakuss/development/QT Interface/assets/icons/expand.png"), 
                            QtGui.QIcon.Normal, QtGui.QIcon.On)
        iconMinimize = QtGui.QIcon()
        iconMinimize.addPixmap(QtGui.QPixmap("/home/azarakuss/development/QT Interface/assets/icons/minimize.png"), 
                            QtGui.QIcon.Normal, QtGui.QIcon.On)

        self.irVideo = QtWidgets.QLabel(self.centralwidget)
        self.irVideo.setGeometry(QtCore.QRect(10, 10, 576, 324))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.irVideo.setFont(font)
        self.irVideo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.irVideo.setAlignment(QtCore.Qt.AlignCenter)
        self.irVideo.setObjectName("irVideo")

        self.rgbVideo = QtWidgets.QLabel(self.centralwidget)
        self.rgbVideo.setGeometry(QtCore.QRect(10, 683, 576, 324))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.rgbVideo.setFont(font)
        self.rgbVideo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.rgbVideo.setAlignment(QtCore.Qt.AlignCenter)
        self.rgbVideo.setObjectName("rgbVideo")

        self.thermalVideo = QtWidgets.QLabel(self.centralwidget)
        self.thermalVideo.setGeometry(QtCore.QRect(10, 347, 576, 324))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.thermalVideo.setFont(font)
        self.thermalVideo.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.thermalVideo.setAlignment(QtCore.Qt.AlignCenter)
        self.thermalVideo.setObjectName("thermalVideo")

        self.logText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.logText.setGeometry(QtCore.QRect(1438, 10, 400, 1001))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.logText.setFont(font)
        self.logText.setUndoRedoEnabled(False)
        self.logText.setReadOnly(True)
        self.logText.setObjectName("logText")

        self.irIP = QtWidgets.QLineEdit(self.centralwidget)
        self.irIP.setGeometry(QtCore.QRect(600, 10, 250, 25))
        self.irIP.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.irIP.setClearButtonEnabled(False)
        self.irIP.setObjectName("irIP")
        self.irIP.setMaxLength(25)
        self.irIP.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9.:/]+")))
        
        self.irConnect = QtWidgets.QPushButton(self.centralwidget)
        self.irConnect.setEnabled(True)
        self.irConnect.setGeometry(QtCore.QRect(600, 40, 100, 25))
        self.irConnect.setObjectName("irConnect")
        self.irConnect.clicked.connect(self.irConnectAction)

        self.irDisconnect = QtWidgets.QPushButton(self.centralwidget)
        self.irDisconnect.setEnabled(False)
        self.irDisconnect.setGeometry(QtCore.QRect(600, 70, 100, 25))
        self.irDisconnect.setObjectName("irDisconnect")
        self.irDisconnect.clicked.connect(self.irDisconnectAction)

        self.irFull = QtWidgets.QPushButton(self.centralwidget)
        self.irFull.setGeometry(QtCore.QRect(600, 304, 30, 30))
        self.irFull.setText("")
        self.irFull.setIcon(iconExpand)
        self.irFull.setObjectName("irFull")
        self.irFull.clicked.connect(self.irFullAction)

        self.thermalFull = QtWidgets.QPushButton(self.centralwidget)
        self.thermalFull.setGeometry(QtCore.QRect(600, 641, 30, 30))
        self.thermalFull.setText("")
        self.thermalFull.setIcon(iconExpand)
        self.thermalFull.setObjectName("thermalFull")
        self.thermalFull.clicked.connect(self.thermalFullAction)

        self.thermalIP = QtWidgets.QLineEdit(self.centralwidget)
        self.thermalIP.setGeometry(QtCore.QRect(600, 347, 250, 25))
        self.thermalIP.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.thermalIP.setClearButtonEnabled(False)
        self.thermalIP.setObjectName("thermalIP")
        self.thermalIP.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9.:/]+")))

        self.thermalDisconnect = QtWidgets.QPushButton(self.centralwidget)
        self.thermalDisconnect.setEnabled(False)
        self.thermalDisconnect.setGeometry(QtCore.QRect(600, 407, 100, 25))
        self.thermalDisconnect.setObjectName("thermalDisconnect")
        self.thermalDisconnect.clicked.connect(self.thermalDisconnectAction)

        self.thermalConnect = QtWidgets.QPushButton(self.centralwidget)
        self.thermalConnect.setGeometry(QtCore.QRect(600, 377, 100, 25))
        self.thermalConnect.setObjectName("thermalConnect")
        self.thermalConnect.clicked.connect(self.thermalConnectAction)

        self.irMinimize = QtWidgets.QPushButton(self.centralwidget)
        self.irMinimize.setEnabled(True)
        self.irMinimize.setGeometry(QtCore.QRect(1810, 980, 30, 30))
        self.irMinimize.setText("")
        self.irMinimize.setIcon(iconMinimize)
        self.irMinimize.setObjectName("irMinimize")
        self.irMinimize.hide()
        self.irMinimize.clicked.connect(self.irMinimizeAction)

        self.thermalMinimize = QtWidgets.QPushButton(self.centralwidget)
        self.thermalMinimize.setEnabled(True)
        self.thermalMinimize.setGeometry(QtCore.QRect(1810, 980, 30, 30))
        self.thermalMinimize.setText("")
        self.thermalMinimize.setIcon(iconMinimize)
        self.thermalMinimize.setObjectName("thermalMinimize")
        self.thermalMinimize.hide()
        self.thermalMinimize.clicked.connect(self.thermalMinimizeAction)

        self.rgbFull = QtWidgets.QPushButton(self.centralwidget)
        self.rgbFull.setGeometry(QtCore.QRect(600, 977, 30, 30))
        self.rgbFull.setText("")
        self.rgbFull.setIcon(iconExpand)
        self.rgbFull.setObjectName("rgbFull")
        self.rgbFull.clicked.connect(self.rgbFullAction)

        self.rgbDisconnect = QtWidgets.QPushButton(self.centralwidget)
        self.rgbDisconnect.setEnabled(False)
        self.rgbDisconnect.setGeometry(QtCore.QRect(600, 743, 100, 25))
        self.rgbDisconnect.setObjectName("rgbDisconnect")
        self.rgbDisconnect.clicked.connect(self.rgbDisconnectAction)

        self.rgbIP = QtWidgets.QLineEdit(self.centralwidget)
        self.rgbIP.setGeometry(QtCore.QRect(600, 683, 250, 25))
        self.rgbIP.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.rgbIP.setClearButtonEnabled(False)
        self.rgbIP.setObjectName("rgbIP")
        self.rgbIP.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9.:/]+")))

        self.rgbConnect = QtWidgets.QPushButton(self.centralwidget)
        self.rgbConnect.setGeometry(QtCore.QRect(600, 713, 100, 25))
        self.rgbConnect.setObjectName("rgbConnect")
        self.rgbConnect.clicked.connect(self.rgbConnectAction)

        self.rgbMinimize = QtWidgets.QPushButton(self.centralwidget)
        self.rgbMinimize.setEnabled(True)
        self.rgbMinimize.setGeometry(QtCore.QRect(1810, 980, 30, 30))
        self.rgbMinimize.setText("")
        self.rgbMinimize.setIcon(iconMinimize)
        self.rgbMinimize.setObjectName("rgbMinimize")
        self.rgbMinimize.hide()
        self.rgbMinimize.clicked.connect(self.rgbMinimizeAction)

        self.irProcess = QtWidgets.QPushButton(self.centralwidget)
        self.irProcess.setGeometry(QtCore.QRect(600, 100, 100, 25))
        self.irProcess.setObjectName("irProcess")
        self.irProcess.clicked.connect(self.irProcessAction)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.irVideo.setText(_translate("MainWindow", "<font color=\"white\">NO VIDEO AVAILABLE"))
        self.rgbVideo.setText(_translate("MainWindow", "<font color=\"white\">NO VIDEO AVAILABLE"))
        self.irConnect.setText(_translate("MainWindow", "Connect"))
        self.irDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.thermalDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.thermalConnect.setText(_translate("MainWindow", "Connect"))
        self.thermalVideo.setText(_translate("MainWindow", "<font color=\"white\">NO VIDEO AVAILABLE"))
        self.rgbDisconnect.setText(_translate("MainWindow", "Disconnect"))
        self.rgbConnect.setText(_translate("MainWindow", "Connect"))
        self.irProcess.setText(_translate("MainWindow", "Process"))

    def irFullAction(self):
        self.irIP.hide()
        self.irConnect.hide()
        self.irDisconnect.hide()
        self.irFull.hide()

        self.thermalVideo.hide()
        self.thermalIP.hide()
        self.thermalConnect.hide()
        self.thermalDisconnect.hide()
        self.thermalFull.hide()

        self.rgbVideo.hide()
        self.rgbIP.hide()
        self.rgbConnect.hide()
        self.rgbDisconnect.hide()
        self.rgbFull.hide()

        self.logText.hide()
        
        self.irMinimize.show()
        self.irVideo.setGeometry(QtCore.QRect(10, 10, 1766, 999))

    def irMinimizeAction(self):
        self.irIP.show()
        self.irConnect.show()
        self.irDisconnect.show()
        self.irFull.show()

        self.thermalVideo.show()
        self.thermalIP.show()
        self.thermalConnect.show()
        self.thermalDisconnect.show()
        self.thermalFull.show()

        self.rgbVideo.show()
        self.rgbIP.show()
        self.rgbConnect.show()
        self.rgbDisconnect.show()
        self.rgbFull.show()

        self.logText.show()
        
        self.irMinimize.hide()
        self.irVideo.setGeometry(QtCore.QRect(10, 10, 576, 324))

    def thermalFullAction(self):
        self.irVideo.hide()
        self.irIP.hide()
        self.irConnect.hide()
        self.irDisconnect.hide()
        self.irFull.hide()

        self.thermalIP.hide()
        self.thermalConnect.hide()
        self.thermalDisconnect.hide()
        self.thermalFull.hide()

        self.rgbVideo.hide()
        self.rgbIP.hide()
        self.rgbConnect.hide()
        self.rgbDisconnect.hide()
        self.rgbFull.hide()

        self.logText.hide()
        
        self.thermalMinimize.show()
        self.thermalVideo.setGeometry(QtCore.QRect(10, 10, 1766, 999))

    def thermalMinimizeAction(self):
        self.irVideo.show()
        self.irIP.show()
        self.irConnect.show()
        self.irDisconnect.show()
        self.irFull.show()

        self.thermalIP.show()
        self.thermalConnect.show()
        self.thermalDisconnect.show()
        self.thermalFull.show()

        self.rgbVideo.show()
        self.rgbIP.show()
        self.rgbConnect.show()
        self.rgbDisconnect.show()
        self.rgbFull.show()

        self.logText.show()
        
        self.thermalMinimize.hide()
        self.thermalVideo.setGeometry(QtCore.QRect(10, 347, 576, 324))

    def rgbFullAction(self):
        self.irVideo.hide()
        self.irIP.hide()
        self.irConnect.hide()
        self.irDisconnect.hide()
        self.irFull.hide()

        self.thermalVideo.hide()
        self.thermalIP.hide()
        self.thermalConnect.hide()
        self.thermalDisconnect.hide()
        self.thermalFull.hide()

        self.rgbIP.hide()
        self.rgbConnect.hide()
        self.rgbDisconnect.hide()
        self.rgbFull.hide()

        self.logText.hide()
        
        self.rgbMinimize.show()
        self.rgbVideo.setGeometry(QtCore.QRect(10, 10, 1766, 999))

    def rgbMinimizeAction(self):
        self.irVideo.show()
        self.irIP.show()
        self.irConnect.show()
        self.irDisconnect.show()
        self.irFull.show()

        self.thermalVideo.show()
        self.thermalIP.show()
        self.thermalConnect.show()
        self.thermalDisconnect.show()
        self.thermalFull.show()

        self.rgbIP.show()
        self.rgbConnect.show()
        self.rgbDisconnect.show()
        self.rgbFull.show()

        self.logText.show()
        
        self.rgbMinimize.hide()
        self.rgbVideo.setGeometry(QtCore.QRect(10, 683, 576, 324))

    def irConnectAction(self):
        connText = self.irIP.text().split(':')
        HOST = connText[0]
        if HOST == "":
            HOST = "127.0.0.1"
        PORT = int(connText[1])

        self.logText.insertPlainText("[INFO] IR Video connecting to " + HOST + ":" + str(PORT) + "\n")

        self.irConnect.setEnabled(False)
        self.irIP.setEnabled(False)

        _translate = QtCore.QCoreApplication.translate
        self.irVideo.setText(_translate("MainWindow", "<font color=\"white\">CONNECTING"))

        self.threadIR = VideoThread("irVideo", self.irVideo, self.irIP, self.irConnect, self.irDisconnect, self.logText, HOST, PORT)
        self.threadIR.change_pixmap_signal.connect(self.threadIR.update_image)        
        self.threadIR.start()    

    def irDisconnectAction(self):
        self.threadIR.change_pixmap_signal.disconnect()
        self.threadIR.stop()

        self.irVideo.clear()
        _translate = QtCore.QCoreApplication.translate
        self.irVideo.setText(_translate("MainWindow", "<font color=\"white\">DISCONNECTED"))
        self.logText.insertPlainText("[INFO] IR Video disconnected\n")

        self.irConnect.setEnabled(True)
        self.irDisconnect.setEnabled(False)
        self.irIP.setEnabled(True)

    def thermalConnectAction(self):
        connText = self.thermalIP.text().split(':')
        HOST = connText[0]
        if HOST == "":
            HOST = "127.0.0.1"
        PORT = int(connText[1])

        self.logText.insertPlainText("[INFO] Thermal Video connecting to " + HOST + ":" + str(PORT) + "\n")

        self.thermalConnect.setEnabled(False)
        self.thermalIP.setEnabled(False)

        _translate = QtCore.QCoreApplication.translate
        self.thermalVideo.setText(_translate("MainWindow", "<font color=\"white\">CONNECTING"))

        self.threadThermal = VideoThread("thermalVideo", self.thermalVideo, self.thermalIP, self.thermalConnect, self.thermalDisconnect, self.logText, HOST, PORT)
        self.threadThermal.change_pixmap_signal.connect(self.threadThermal.update_image)        
        self.threadThermal.start()    

    def thermalDisconnectAction(self):
        self.threadThermal.change_pixmap_signal.disconnect()
        self.threadThermal.stop()

        self.thermalVideo.clear()
        _translate = QtCore.QCoreApplication.translate
        self.thermalVideo.setText(_translate("MainWindow", "<font color=\"white\">DISCONNECTED"))
        self.logText.insertPlainText("[INFO] Thermal Video disconnected\n")

        self.thermalConnect.setEnabled(True)
        self.thermalDisconnect.setEnabled(False)
        self.thermalIP.setEnabled(True)

    def rgbConnectAction(self):
        connText = self.rgbIP.text().split(':')
        HOST = connText[0]
        if HOST == "":
            HOST = "127.0.0.1"
        PORT = int(connText[1])

        self.logText.insertPlainText("[INFO] RGB Video connecting to " + HOST + ":" + str(PORT) + "\n")

        self.rgbConnect.setEnabled(False)
        self.rgbIP.setEnabled(False)

        _translate = QtCore.QCoreApplication.translate
        self.rgbVideo.setText(_translate("MainWindow", "<font color=\"white\">CONNECTING"))

        self.threadRGB = VideoThread("rgbVideo", self.rgbVideo, self.rgbIP, self.rgbConnect, self.rgbDisconnect, self.logText, HOST, PORT)
        self.threadRGB.change_pixmap_signal.connect(self.threadRGB.update_image)        
        self.threadRGB.start()    

    def rgbDisconnectAction(self):
        self.threadRGB.change_pixmap_signal.disconnect()
        self.threadRGB.stop()

        self.rgbVideo.clear()
        _translate = QtCore.QCoreApplication.translate
        self.rgbVideo.setText(_translate("MainWindow", "<font color=\"white\">DISCONNECTED"))
        self.logText.insertPlainText("[INFO] RGB Video disconnected\n")

        self.rgbConnect.setEnabled(True)
        self.rgbDisconnect.setEnabled(False)
        self.rgbIP.setEnabled(True)

    def irProcessAction(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
