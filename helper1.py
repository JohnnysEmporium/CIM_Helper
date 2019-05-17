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
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.Qt import QPixmap, QWidget
from PyQt5.QtWebEngineWidgets import *
import pyHook
import pyperclip


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 900)
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
        
        
        multiButtonStSheet = """
            QPushButton{
                width: 100px;
            }
        """
        self.multiButton = QtWidgets.QPushButton("Copy multiple times")
        self.gridLayout_side.addWidget(self.multiButton)
        self.gridLayout_side.setAlignment(QtCore.Qt.AlignTop)
        self.multiButton.setStyleSheet(multiButtonStSheet)
        self.multiButton.setCheckable(True)
        self.multiToggled = False
        
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
#         self.proxy = QtNetwork.QNetworkProxy()
#         self.proxy.setType(QtNetwork.QNetworkProxy.HttpProxy)
#         self.proxy.setHostName("poland-bcproxy.geo.corp.hcl.in")
#         self.proxy.setPort(8080)
#         QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
        self.web = QWebEngineView(self.centralwidget)
        self.gridLayout_browser.addWidget(self.web)
        self.web.load(QtCore.QUrl("https://google.com"))
        

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.pause = False
        self.testvar = 0
        self.textList = []
        self.labelsList = []
        self.labelsList2 = []
        self.keyList = [5,]
        self.shallIDelete = False
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
        if self.keyList[1] == 'Insert':
            self.multiButton.toggle()
            self.multiToggled = not(self.multiToggled)
            if self.shallIDelete:
                self.remove_paste()
            self.shallIDelete = not(self.shallIDelete)
        if self.keyList[1] == 'Lcontrol' and self.keyList[1] == 'V' and self.multiToggled == True and self.pause == False:
            self.set_clipboard()
        if self.keyList[0] == 'Lcontrol' and self.keyList[1] == 'V' and self.multiToggled == False and self.pause == False:
            self.set_clipboard()
            self.remove_paste()
        if self.keyList[1] == 'Pause':
            self.restore_clipboard()
        return True
        
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_F1:
            self.textList.append(self.web.selectedText())
            self.populate_paste()
            self.create_side_container(self.web.selectedText())
        if e.key() == QtCore.Qt.Key_F2:
            self.autoCopyInsert()
        if e.key() == QtCore.Qt.Key_Delete:
            self.delete_all()
        if e.key() == QtCore.Qt.Key_Backspace:
            self.remove_paste()
        
    def open_url(self):
        self.store = []
        self.loadingLabel.show()
        self.loadingIco.start()
        url = self.lineEdit.text()
        if url[:7] != "http://" and url[:8] != "https://":
            url = "https://" + url
        self.web.setUrl(QtCore.QUrl(url))
        self.web.loadFinished.connect(lambda: self.loadingLabel.hide() and self.loadingIco.stop())
        self.web.loadFinished.connect(self.autoCopy)
    
    def restore_clipboard(self):
        self.pause = not(self.pause)
        if self.pause:
            global clipboard_old
            pyperclip.copy(clipboard_old)
            self.dim_labels()
        else:
            self.set_clipboard()
            self.undim_labels()
            
    def dim_labels(self):
        stshLabel = """
            *{
                color:rgba(0,0,0,0.3);
            }
        """
        self.multiButton.setText("PAUSE")
        self.multiButton.setDisabled(True)
        
        for i in self.labelsList:
            i.setStyleSheet(stshLabel)
        for i in self.labelsList2:
            i.setStyleSheet(stshLabel)
            
    def undim_labels(self):
        stsh = """
            *{
                color:rgba(0,0,0,1);
            }
        """
        self.multiButton.setText("Copy multiple times")
        self.multiButton.setEnabled(True)
        
        for i in self.labelsList:
            i.setStyleSheet(stsh)
        for i in self.labelsList2:
            i.setStyleSheet(stsh)
    
    def delete_all(self):
        for i in range(len(self.textList)):
            self.remove_paste()
        
    def autoCopy(self):

        js_inc = "document.getElementById('sys_readonly.incident.number').value;"
        js_user = "document.getElementById('sys_display.incident.u_requested_for').value;"
        js_group = "document.getElementById('sys_display.incident.assignment_group').value;"
        js_date = "document.getElementById('sn_form_inline_stream_entries').getElementsByClassName('date-calendar')[0].innerHTML;"
        js_text = "document.getElementById('sn_form_inline_stream_entries').getElementsByClassName('sn-widget-textblock-body sn-widget-textblock-body_formatted')[0].innerHTML;"
        
        self.web.page().runJavaScript(js_inc, self.__callback)
        self.web.page().runJavaScript(js_user, self.__callback)
        self.web.page().runJavaScript(js_group, self.__callback)
        self.web.page().runJavaScript(js_date, self.__callback)
        self.web.page().runJavaScript(js_text, self.__callback)
        
    def __callback(self, response):
        if len(self.store) > 4:
            self.store = []
        if str(response) == '':
            pass
        else:
            self.store.append(str(response))
        
    def autoCopyInsert(self):
#         url = self.store[0]
#         inc = self.store[1] 
#         user = self.store[2]
#         group = self.store[3]
#         date = self.store[4]
#         text = self.store[5]
        for i in self.store:
            self.textList.append(i)
            self.create_side_container(i)
            self.populate_paste()
        self.store = []
        
    def create_side_container(self, txt):
        label = QtWidgets.QLabel()
        self.labelsList2.append(label)
        try:
            text = txt[0:18]
            if len(txt) > 18:
                if text[-1] == ' ':
                    text[-1] = ""
                text = text + '...'
            label.setText(text)
            self.gridLayout_side.addWidget(label, (len(self.textList)), 0)
        except:
            pass
        
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
        if len(self.textList) < 1:
            pass
        else:
            pyperclip.copy(self.textList[0])


    
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

clipboard_old = pyperclip.paste()

if __name__ == "__main__":
    import sys
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    networkProxy = QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(True)
    w = MainWindow()
    w.show()
sys.exit(app.exec_())

