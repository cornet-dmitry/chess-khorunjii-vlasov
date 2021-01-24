import sqlite3
import sys
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget
from PyQt5.QtCore import QDate
from PyQt5 import QtCore, QtGui, QtWidgets


class Start(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui', self)
        self.con = sqlite3.connect("chess.sqlite")
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run2)

    def run(self):
        password = self.lineEdit_2.text()
        name = self.lineEdit.text()
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM Users WHERE Name=?",
                             (name,)).fetchall()
        print(result)
        if not result:
            self.er_name = Error_Name()
            self.er_name.show()
        else:
            result1 = cur.execute("SELECT * FROM Users WHERE Name=? AND Password=?",
                                 (name, password)).fetchall()
            if not result1:
                self.er_pas = Error_Password()
                self.er_pas.show()
            else:
                self.menu = Menu()
                self.menu.show()
                self.con.close()
                self.close()

    def run2(self):
        password = self.lineEdit_2.text()
        name = self.lineEdit.text()
        self.con.close()
        self.close()
        self.conf = Confirm(password, name)
        self.conf.show()



class Error_Name(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('error-nouser.ui', self)


class Error_Password(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('error-password.ui', self)


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.pushButton.clicked.connect(self.runGame)
        self.pushButton_4.clicked.connect(self.back)

    def runGame(self):
        self.close()
        os.system('python ChessMain.py')

    def back(self):
        self.close()
        self.start = Start()
        self.start.show()


class Confirm(QMainWindow):
    def __init__(self, password, name):
        super().__init__()
        uic.loadUi('confirm.ui', self)
        self.prev_pas = password
        self.name = name
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.con = sqlite3.connect("chess.sqlite")
        self.pas = self.lineEdit.text()
        if self.pas == self.prev_pas:
            cur = self.con.cursor()
            print(self.name, self.pas)
            cur.execute("""Insert into Users(Name, Password) values("{}", "{}")""".format(self.name, self.pas))
            self.con.commit()
            self.con.close()
            self.close()
            self.menu = Menu()
            self.menu.show()
        else:
            self.nomatch = NoMatch()
            self.nomatch.show()


class NoMatch(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('error-nomatch.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start()
    ex.show()
    sys.exit(app.exec_())
