import cv2, socket, pickle, struct
from PyQt5.QtCore import pyqtSignal, QThread, Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
import numpy as np

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    caller = None
    label = None
    IP = None
    connection = None
    disconnection = None
    process = None
    logText = None
    HOST = None
    PORT = None
    width = None
    height = None

    def __init__(self, caller, label, IP, connection, disconnection, process, logText, HOST, PORT, frame=None):
        super().__init__()
        self._run_flag = True
        self.caller = caller
        self.label = label
        self.IP = IP
        self.connection = connection
        self.disconnection = disconnection
        self.process = process
        self.logText = logText
        self.HOST = HOST
        self.PORT = PORT
        self.frame = frame

    def run(self):
        try:
            cap = cv2.VideoCapture("http://" + self.HOST + ":" + self.PORT + "/stream.mjpg")
            if not cap.isOpened():

                _translate = QtCore.QCoreApplication.translate
                self.label.setText(_translate("MainWindow", "<font color=\"white\">BAD CONNECTION"))
                #print("Caller : "+ self.caller)
                if self.caller == "irVideo":
                    self.logText.insertPlainText("[INFO] IR Video has a bad connection\n")
                elif self.caller == "thermalVideo":
                    self.logText.insertPlainText("[INFO] Thermal Video has a bad connection\n")
                elif self.caller == "rgbVideo":
                    self.logText.insertPlainText("[INFO] RGB Video has a bad connection\n")
                
                self.connection.setEnabled(True)
                self.IP.setEnabled(True)

                raise ConnectionRefusedError
            
        except ConnectionRefusedError as e:
            return

        if self.caller == "irVideo":
            self.logText.insertPlainText("[INFO] IR Video connected to " + self.HOST + ":" + str(self.PORT) + "\n")
        elif self.caller == "thermalVideo":
            self.logText.insertPlainText("[INFO] Thermal Video connected to " + self.HOST + ":" + str(self.PORT) + "\n")
        elif self.caller == "rgbVideo":
            self.logText.insertPlainText("[INFO] RGB Video connected to " + self.HOST + ":" + str(self.PORT) + "\n")

        self.disconnection.setEnabled(True)
        self.process.setEnabled(True)


        while(self._run_flag and cap.isOpened()):
            ret, self.frame = cap.read()
            if ret:
                self.change_pixmap_signal.emit(self.frame)
            else:
                break

    def stop(self):
        self._run_flag = False
        self.wait()

    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        #rgb_image = cv2.flip(rgb_image, 1)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio)
        
        return QPixmap.fromImage(p)