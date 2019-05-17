# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helper.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1244, 894)
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

        self.retranslateUi(MainWindow)
        self.copy_paste.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.web = QWebEngineView(self.centralwidget)
        self.gridLayout_2.addWidget(self.web)
        self.web.load(QtCore.QUrl("https://further-reading.net"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.copy_paste.setTabText(self.copy_paste.indexOf(self.Copy), _translate("MainWindow", "Tab 1"))
        self.copy_paste.setTabText(self.copy_paste.indexOf(self.Paste), _translate("MainWindow", "Tab 2"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

