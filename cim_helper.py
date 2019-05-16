# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helper.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import threading
import time

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QPixmap, QWidget
from PyQt5.QtWebEngineWidgets import *
import pyHook
import pyperclip


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.copy_paste = QtWidgets.QTabWidget(self.centralwidget)
        self.copy_paste.setObjectName("copy_paste")
        self.Copy = QtWidgets.QWidget()
        self.Copy.setObjectName("Copy")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Copy)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_browser = QtWidgets.QGridLayout()
        self.gridLayout_browser.setObjectName("gridLayout_browser")
        self.gridLayout_2.addLayout(self.gridLayout_browser, 1, 0, 1, 1)
        self.gridLayout_side = QtWidgets.QGridLayout()
        self.gridLayout_side.setObjectName("gridLayout_side")
        self.gridLayout_2.addLayout(self.gridLayout_side, 1, 1, 1, 1)
        self.gridLayout0 = QtWidgets.QGridLayout()
        self.gridLayout0.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.Copy)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backIco = QPixmap('icons/arrow.png') 
        self.backIco = self.backIco.scaled(20, 20)
        self.backIco = QtGui.QIcon(self.backIco)
        self.backButton = QtWidgets.QPushButton()
        self.backButton.setIcon(self.backIco)
        self.forwIco = Image.open('icons\\arrow.png')
        self.forwIco = self.forwIco.rotate(180)
        self.forwIco = self.forwIco.convert('RGBA')
        self.forwIco = ImageQt(self.forwIco) 
        self.forwIco = QPixmap.fromImage(self.forwIco)
        self.forwIco = self.forwIco.scaled(20, 20)
        self.forwIco = QtGui.QIcon(self.forwIco)
        self.forwButton = QtWidgets.QPushButton()
        self.forwButton.setIcon(self.forwIco)
        stylesheet = """
            
            QPushButton{
                background-color:transparent;
            }
        
        """
        self.forwButton.setStyleSheet(stylesheet)
        self.backButton.setStyleSheet(stylesheet)
        self.horizontalLayout.addWidget(self.backButton)
        self.horizontalLayout.addWidget(self.forwButton)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.loadingIco = QtGui.QMovie("icons/loading.gif")
        self.loadingLabel = QtWidgets.QLabel()
        self.loadingLabel.setMovie(self.loadingIco)
        self.loadingIco.setScaledSize(QtCore.QSize(25, 25))
        self.horizontalLayout.addWidget(self.loadingLabel)
        self.loadingLabel.hide()
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout0.addWidget(self.widget, 0, 0)
        self.gridLayout_2.addLayout(self.gridLayout0, 0, 0, 1, 1)
        self.copy_paste.addTab(self.Copy, "")
        self.Paste = QtWidgets.QWidget()
        self.Paste.setObjectName("Paste")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Paste)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.copy_paste.addTab(self.Paste, "")
        self.gridLayout.addWidget(self.copy_paste, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1244, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.menuHelp.addAction(self.actionInfo)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.pushButton.clicked.connect(self.open_url)
        self.backButton.clicked.connect(lambda: self.web.back())
        self.forwButton.clicked.connect(lambda: self.web.forward())
        
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.widget.setSizePolicy(sizePolicy)
        
        self.retranslateUi(MainWindow)
        self.copy_paste.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CIM Helper"))
        self.pushButton.setText(_translate("MainWindow", "Go"))
        self.copy_paste.setTabText(self.copy_paste.indexOf(self.Copy), _translate("MainWindow", "Copy"))
        self.copy_paste.setTabText(self.copy_paste.indexOf(self.Paste), _translate("MainWindow", "Paste"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))

    def browser(self):
        self.web = QWebEngineView(self.centralwidget)
        self.gridLayout_browser.addWidget(self.web)
        self.web.load(QtCore.QUrl("https://google.com"))
        

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.textList = []
        self.labelsList = []
        self.labelsList2 = []
        self.keyList = []
        self.setupUi(self)
        self.browser()
        self.hook_mgr()

    def hook_mgr(self):
        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self.OnKeyboardEvent
        self.hm.HookKeyboard()
        
    def OnKeyboardEvent(self, event):
        self.keyList.append(event.Key)
        if len(self.keyList) >= 3:
            self.keyList.pop(0)
        if self.keyList[0] == 'Lcontrol' and self.keyList[1] == 'V':
            self.set_clipboard()
            self.remove_paste()
        return True
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_C:
            self.textList.append(self.web.selectedText())
            self.populate_paste()
            self.create_side_container()
            
    def open_url(self):
        self.loadingLabel.show()
        self.loadingIco.start()
        url = self.lineEdit.text()
        if url[:7] != "http://" and url[:8] != "https://":
            url = "https://" + url
        self.web.setUrl(QtCore.QUrl(url))
        
        self.web.loadFinished.connect(lambda: self.loadingLabel.hide() and self.loadingIco.stop())
    
    def create_side_container(self):
        label = QtWidgets.QLabel()
        self.labelsList2.append(label)
        text = self.web.selectedText()[0:13]
        if len(self.web.selectedText()) > 13:
            if text[-1] == ' ':
                text[-1] = ""
            text = text + '...'
        label.setText(text)
        self.gridLayout_side.addWidget(label, (len(self.textList) - 1), 0)
#         self.gridLayout_2.setColumnStretch(0,(len(self.textList) - 1))
            
    def populate_paste(self):
        label = QtWidgets.QLabel()
        label.setWordWrap(True)
        label.setText(self.textList[-1])
        self.labelsList.append(label)
        self.gridLayout_3.addWidget(label, (len(self.textList) - 1), 0)
        
    def remove_paste(self):
        self.labelsList[0].hide()
        self.labelsList.pop(0)
        self.textList.pop(0)
        self.labelsList2[0].hide()
        self.labelsList2.pop(0)
        
    def set_clipboard(self):
        pyperclip.copy(self.textList[0])

    
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys
#     sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
