import sqlite3
import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets

from Chess import ChessMain

firstUserID = 0
secondUserID = 0

activeID = []


class Confirm(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(515, 197)
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 181, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 50, 331, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 100, 181, 23))
        self.pushButton.setObjectName("pushButton")
        Register.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Register)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 21))
        self.menubar.setObjectName("menubar")
        Register.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Register)
        self.statusbar.setObjectName("statusbar")
        Register.setStatusBar(self.statusbar)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "MainWindow"))
        self.label.setText(_translate("Register", "<html><head/><body><p><span style=\" font-size:12pt;\">Confirm your password</span></p></body></html>"))
        self.pushButton.setText(_translate("Register", "Register"))


class Error_nomatch(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(275, 83)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 275, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Error: passwords didn\'t match</span></p></body></html>"))



class Error_nouser(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(185, 75)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 185, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Error: no such user</span></p></body></html>"))



class Error_password(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(214, 84)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 214, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">Error: wrong password</span></p></body></html>"))


class Start_ui(object):
    def setupUi(self, Chess):
        Chess.setObjectName("Chess")
        Chess.resize(531, 337)
        self.centralwidget = QtWidgets.QWidget(Chess)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 171, 31))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 60, 351, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(100, 200, 351, 54))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 70, 60, 71))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        Chess.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Chess)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        Chess.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Chess)
        self.statusbar.setObjectName("statusbar")
        Chess.setStatusBar(self.statusbar)

        self.retranslateUi(Chess)
        QtCore.QMetaObject.connectSlotsByName(Chess)

    def retranslateUi(self, Chess):
        _translate = QtCore.QCoreApplication.translate
        Chess.setWindowTitle(_translate("Chess", "MainWindow"))
        self.label.setText(_translate("Chess", "<html><head/><body><p><span style=\" font-size:14pt;\">Sign in or register</span></p></body></html>"))
        self.pushButton.setText(_translate("Chess", "Sign in"))
        self.pushButton_2.setText(_translate("Chess", "Sign up"))
        self.label_2.setText(_translate("Chess", "<html><head/><body><p><span style=\" font-size:10pt;\">Username</span></p></body></html>"))
        self.label_3.setText(_translate("Chess", "<html><head/><body><p><span style=\" font-size:10pt;\">Password</span></p></body></html>"))


class Statistic_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(270, 480, 281, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 430, 331, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 480, 41, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 480, 41, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 181, 61))
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(390, 90, 321, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout.addWidget(self.lcdNumber)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout.addWidget(self.lcdNumber_2)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout.addWidget(self.lcdNumber_3)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.layoutWidget)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.verticalLayout.addWidget(self.lcdNumber_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 90, 321, 281))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 520, 111, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:14pt;\">For every 25 wins, your level increases</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">Lvl1</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:12pt;\">Lvl2</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:36pt;\">Statistic</span></p><p><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:28pt;\">Wins:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:28pt;\">Defeats:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:28pt;\">Taken pieces:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:28pt;\">Given away pieces:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Back"))



class Register2_Ui(object):
    def setupUi(self, Chess):
        Chess.setObjectName("Chess")
        Chess.resize(531, 337)
        self.centralwidget = QtWidgets.QWidget(Chess)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 281, 31))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 60, 351, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 200, 351, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 70, 60, 71))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        Chess.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Chess)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 21))
        self.menubar.setObjectName("menubar")
        Chess.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Chess)
        self.statusbar.setObjectName("statusbar")
        Chess.setStatusBar(self.statusbar)

        self.retranslateUi(Chess)
        QtCore.QMetaObject.connectSlotsByName(Chess)

    def retranslateUi(self, Chess):
        _translate = QtCore.QCoreApplication.translate
        Chess.setWindowTitle(_translate("Chess", "MainWindow"))
        self.label.setText(_translate("Chess", "<html><head/><body><p><span style=\" font-size:14pt;\">Sign in or register the 2nd player</span></p></body></html>"))
        self.pushButton.setText(_translate("Chess", "Sign in"))
        self.pushButton_2.setText(_translate("Chess", "Sign up"))
        self.label_2.setText(_translate("Chess", "<html><head/><body><p><span style=\" font-size:10pt;\">Username</span></p></body></html>"))
        self.label_3.setText(_translate("Chess", "<html><head/><body><p><span style=\" font-size:10pt;\">Password</span></p></body></html>"))


class Menu_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 140, 231, 101))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 241, 121))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 290, 351, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 410, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 21))
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
        self.pushButton.setText(_translate("MainWindow", "Play One-on-one"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:36pt;\">Let\'s play!</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Statistics"))
        self.pushButton_4.setText(_translate("MainWindow", "Back"))


class Start(QMainWindow, Start_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("chess.sqlite")
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run2)

    def run(self):
        self.password = self.lineEdit_2.text()
        self.name = self.lineEdit.text()
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Users WHERE Name=?",
                             (self.name,)).fetchall()
        if not result:
            self.er_name = Error_Name()
            self.er_name.show()
        else:
            result1 = cur.execute("SELECT * FROM Users WHERE Name=? AND Password=?",
                                 (self.name, self.password)).fetchall()
            if not result1:
                self.er_pas = Error_Password()
                self.er_pas.show()
            else:
                firstUserID = result1[-1][0]
                activeID.append(firstUserID)

                self.menu = Menu(self.name, self.password)
                self.menu.show()
                self.con.close()
                self.close()

    def run2(self):
        password = self.lineEdit_2.text()
        name = self.lineEdit.text()
        if name != '' and password != '':
            self.con.close()
            self.close()
            self.conf = Confirm(password, name, False)
            self.conf.show()


class Register2(QMainWindow, Register2_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("chess.sqlite")
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run2)

    def run(self):
        self.password = self.lineEdit_2.text()
        self.name = self.lineEdit.text()
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Users WHERE Name=?",
                             (self.name,)).fetchall()
        if not result:
            self.er_name = Error_Name()
            self.er_name.show()
        else:
            result1 = cur.execute("SELECT * FROM Users WHERE Name=? AND Password=?",
                                 (self.name, self.password)).fetchall()
            if not result1:
                self.er_pas = Error_Password()
                self.er_pas.show()
            else:
                secondUserID = result1[-1][0]
                activeID.append(secondUserID)

                self.con.close()
                self.close()
                gameRunning()

    def run2(self):
        password = self.lineEdit_2.text()
        name = self.lineEdit.text()
        if name != '' and password != '':
            self.con.close()
            self.close()
            self.conf = Confirm(password, name, False)
            self.conf.show()


class Error_Name(QMainWindow, Error_nouser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Error_Password(QMainWindow, Error_password):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Menu(QMainWindow, Menu_ui):
    def __init__(self, name, password):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.password = password
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.statistic)
        self.pushButton.clicked.connect(self.secondPlayer)

    def back(self):
        self.close()
        self.start = Start()
        self.start.show()

    def statistic(self):
        self.close()
        self.stat = Statistic(self.name, self.password)
        self.stat.show()

    def secondPlayer(self):
        self.close()
        self.reg = Register2()
        self.reg.show()


class Confirm(QMainWindow, Confirm):
    def __init__(self, password, name, flag):
        super().__init__()
        self.setupUi(self)
        self.prev_pas = password
        self.name = name
        self.flag = flag
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.con = sqlite3.connect("chess.sqlite")
        self.pas = self.lineEdit.text()
        if self.pas == self.prev_pas:
            cur = self.con.cursor()

            nextIdUser = cur.execute("SELECT ID FROM Users").fetchall()[-1][-1]
            nextIdUser += 1
            cur.execute("""Insert into Users(ID, Name, Password, Wins, Defeats, Given, Taken)
             values("{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(nextIdUser, self.name, self.pas, 0, 0, 0, 0))
            firstUserID = nextIdUser
            activeID.append(firstUserID)
            self.con.commit()
            self.con.close()
            self.close()
            if self.flag == False:
                self.menu = Menu(self.name, self.pas)
                self.menu.show()
            else:
                self.con.close()
                self.close()
                gameRunning()
        else:
            self.nomatch = NoMatch()
            self.nomatch.show()


class NoMatch(QMainWindow, Error_nomatch):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Statistic(QMainWindow, Statistic_ui):
    def __init__(self, name, password):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("chess.sqlite")
        cur = self.con.cursor()
        self.name = name
        self.password = password
        result = cur.execute("SELECT * FROM Users WHERE Name=? AND Password=?",
                             (self.name, self.password)).fetchall()
        id, user, pas, wins, defeats, given, taken = result[0]
        if wins is not None:
            self.lcdNumber.display(int(wins))
        else:
            wins = 0
        if defeats is not None:
            self.lcdNumber_2.display(int(defeats))
        else:
            defeats = 0
        if taken is not None:
            self.lcdNumber_3.display(int(taken))
        else:
            taken = 0
        if given is not None:
            self.lcdNumber_4.display(int(given))
        else:
            given = 0
        left_lvl = (wins // 25) + 1
        right_lvl = (wins // 25) + 2
        self.label_2.setText(f'Lvl{left_lvl}')
        self.label_3.setText(f'Lvl{right_lvl}')
        self.pushButton.clicked.connect(self.run)
        wins = int(wins)
        value = 100 - ((((wins // 25) * 25 + 25) - wins) / 25 * 100)
        self.progressBar.setValue(int(value))

    def run(self):
        self.close()
        self.menu = Menu(self.name, self.password)
        self.menu.show()


def gameRunning():
    ChessMain.main(activeID)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start()
    ex.show()
    sys.exit(app.exec_())