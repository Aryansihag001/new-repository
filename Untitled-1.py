import webbrowser
from EdithUi import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QTime,QDate
from PyQt5.uic import loadUiType
import Edith
import os
import sys


class Mainthread(QThread):
    def _init_(self):
        super(Mainthread,self).__init__()
    def run(self):
        Edith.Task_gui()


class Gui_Start(Ui_MainWindow):
    def __init__(self):
        super()._init_()
        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)
    
    def chrome_app(self):
        os.startfile("chrome app")

    def yt_app(self):
        webbrowser.open("https://www.youtube.com/")


GuiApp=QApplication(sys.argv)
EdithUi=Gui_Start()
EdithUi.show()
exit(GuiApp.exec_())
    


