import sqlite3
import sys
from datetime import datetime

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QVBoxLayout, QLabel, QFormLayout, \
    QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QMenuBar, QStatusBar, QComboBox


class Ui_SecondWindow(object):  # окно регистрации/авторизации
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(346, 446)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(Form)
        self.label.setStyleSheet("font: 75 26pt \"Arial\"; margin: 0px 15px; padding: 0px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
                                   "margin: 2px 8px;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)
        self.loginReg = QLineEdit(Form)
        self.loginReg.setStyleSheet("margin: 2px 8px; padding: 2px;")
        self.loginReg.setObjectName("loginReg")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.loginReg)
        self.label_3 = QLabel(Form)
        self.label_3.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
                                   "margin: 2px 8px;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)
        self.emailReg = QLineEdit(Form)
        self.emailReg.setStyleSheet("margin: 2px 8px; padding: 2px;")
        self.emailReg.setObjectName("emailReg")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.emailReg)
        self.label_4 = QLabel(Form)
        self.label_4.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
                                   "margin: 2px 8px;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)
        self.passReg = QLineEdit(Form)
        self.passReg.setStyleSheet("margin: 2px 8px; padding: 2px;")
        self.passReg.setObjectName("passReg")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.passReg)
        self.label_8 = QLabel(Form)
        self.label_8.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
                                   "margin: 2px 8px;")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)
        self.passRepeatReg = QLineEdit(Form)
        self.passRepeatReg.setStyleSheet("margin: 2px 8px; padding: 2px;")
        self.passRepeatReg.setObjectName("passRepeatReg")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.passRepeatReg)
        self.verticalLayout.addLayout(self.formLayout)
        self.btn_reg = QPushButton(Form)
        self.btn_reg.setStyleSheet("font: 14pt \"Arial\";\n"
                                   "margin: 10px 40px;\n"
                                   "padding: 10px;")
        self.btn_reg.setObjectName("btn_reg")
        self.verticalLayout.addWidget(self.btn_reg)
        self.label_5 = QLabel(Form)
        self.label_5.setStyleSheet("font: 75 26pt \"Arial\"; margin: 0px 15px; padding: 0px;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QLabel(Form)
        self.label_7.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
                                   "margin: 2px 8px;")
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)
        self.emailAut = QLineEdit(Form)
        self.emailAut.setStyleSheet("margin: 2px 8px; padding: 2px;")
        self.emailAut.setObjectName("emailAut")
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.emailAut)
        self.label_6 = QLabel(Form)
        self.label_6.setStyleSheet("font: 75 italic 14pt \"Arial\";\n"
                                   "margin: 2px 8px;")
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_6)
        self.pasAut = QLineEdit(Form)
        self.pasAut.setStyleSheet("margin: 2px 8px; padding: 2px;")
        self.pasAut.setObjectName("pasAut")
        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.pasAut)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.btn_log = QPushButton(Form)
        self.btn_log.setStyleSheet("font: 14pt \"Arial\";\n"
                                   "margin: 10px 40px;\n"
                                   "padding: 10px;")
        self.btn_log.setObjectName("btn_log")
        self.verticalLayout.addWidget(self.btn_log)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Registration/Authorization"))
        self.label.setText(_translate("Form", "Registration/Authorization"))
        self.label_2.setText(_translate("Form", "Login:"))
        self.label_3.setText(_translate("Form", "E-mail:"))
        self.label_4.setText(_translate("Form", "Password:"))
        self.label_8.setText(_translate("Form", "Repeat pass:"))
        self.btn_reg.setText(_translate("Form", "Register"))
        self.label_5.setText(_translate("Form", "Authorization"))
        self.label_7.setText(_translate("Form", "E-mail:"))
        self.label_6.setText(_translate("Form", "Pass:"))
        self.btn_log.setText(_translate("Form", "Login"))


"""АВТОРИЗАЦИЯ"""


class Login(QWidget, Ui_SecondWindow):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.userActiveData = []
        self.data = []

        self.setupUi(self)  # загрузка интерфейса

        self.con = sqlite3.connect('mainDB.db')  # подключение базы данных
        self.cur = self.con.cursor()

        for elem in self.cur.execute("""SELECT * FROM users""").fetchall():
            self.data.append(elem)  # получение информации о всех пользователях
            self.countUserRegister = elem[0] + 1  # номер следующего по счёту пользователя, для его регистрации в БД

        self.btn_reg.clicked.connect(self.register)
        self.btn_log.clicked.connect(self.authorization)

    def authorization(self):
        global result, UserActiveID

        emailAut = self.emailAut.text()
        pasAut = self.pasAut.text()

        for i in self.data:  # проходим по всем пользователям и сравниваем с введёнными данными
            if emailAut == i[2] and pasAut == i[3]:
                self.userActiveData = i[:]
                UserActiveID = self.userActiveData[0]
                QMessageBox.critical(self, "Успех! ",
                                     f"Авторизация прошла успешно!", QMessageBox.Ok)
                self.close()  # закрытие окна авторизации
                return True
        QMessageBox.critical(self, "Ошибка ",
                             f"Авторизация не прошла! Убедитесь, что ввели правильные данные.", QMessageBox.Ok)

    def register(self):
        global UserActiveID

        login = self.loginReg.text()
        email = self.emailReg.text()
        passOne = self.passReg.text()
        passTwo = self.passRepeatReg.text()

        if self.email_cheek(email) and self.password_cheek(passOne, passTwo):
            with self.con:
                self.cur.execute("INSERT INTO users "
                                 "VALUES(?, ?, ?, ?)", (self.countUserRegister, login, email, passOne))
                # запись данных о активном аккаунте для дальнейшей работы
                self.userActiveData = [self.countUserRegister, login, email, passOne]
                UserActiveID = self.userActiveData[0]

            QMessageBox.critical(self, "Успех! ",
                                 f"Регистрация прошла успешно! Добро пожаловать в систему, {login}!", QMessageBox.Ok)

            self.close()  # закрытие окна регистрации
            return True

    def password_cheek(self, one, two):
        if one != two:
            QMessageBox.critical(self, "Ошибка регистрации",
                                 "Пароли не совпадают!", QMessageBox.Ok)
            return False
        elif len(one) < 6:
            QMessageBox.critical(self, "Ошибка регистрации",
                                 "Пароль слишком короткий!", QMessageBox.Ok)
            return False
        elif one.isalpha() or one.isdigit():
            QMessageBox.critical(self, "Ошибка регистрации",
                                 "Пароль не надёжный!", QMessageBox.Ok)
        else:
            return True

    def email_cheek(self, email):
        for i in self.data:
            if i == email:
                QMessageBox.critical(self, "Ошибка регистрации",
                                     "Данный E-Mail адресс уже зарегистрирован в системе!", QMessageBox.Ok)
                return False
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())