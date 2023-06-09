# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aksh\Downloads\signin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignIn(object):
    def setupUi(self, SignIn):
        SignIn.setObjectName("SignIn")
        SignIn.resize(300, 533)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        SignIn.setFont(font)
        SignIn.setStyleSheet("background-color:#FFFFFF;")
        self.centralwidget = QtWidgets.QWidget(SignIn)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(65, 206.5, 170, 120))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setStyleSheet("border-radius:15px;border: 1px solid rgb(0, 0, 0);padding-top:4%;padding-bottom:4%;")
        self.username.setFrame(True)
        self.username.setCursorPosition(0)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("border-radius:15px;\n"
"border: 1px solid rgb(0, 0, 0);\n"
"padding-top:4%;\n"
"padding-bottom:4%;")
        self.password.setFrame(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setCursorPosition(0)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SignInButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SignInButton.sizePolicy().hasHeightForWidth())
        self.SignInButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.SignInButton.setFont(font)
        self.SignInButton.setStyleSheet("border-radius:15px;border:1px solid rgb(135,206,235); background-color:rgb(135,206,235); padding-top:6%;padding-bottom:6%;\n"
"padding-left:5%;\n"
"padding-right:5%")
        self.SignInButton.setObjectName("SignInButton")
        self.horizontalLayout.addWidget(self.SignInButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        SignIn.setCentralWidget(self.centralwidget)
        self.retranslateUi(SignIn)
        QtCore.QMetaObject.connectSlotsByName(SignIn)

    def retranslateUi(self, SignIn):
        _translate = QtCore.QCoreApplication.translate
        SignIn.setWindowTitle(_translate("SignIn", "MainWindow"))
        self.label.setText(_translate("SignIn", "Sign In"))
        self.username.setPlaceholderText(_translate("SignIn", "Username"))
        self.password.setPlaceholderText(_translate("SignIn", "Password"))
        self.SignInButton.setText(_translate("SignIn", "Sign In"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignIn = QtWidgets.QMainWindow()
    ui = Ui_SignIn()
    ui.setupUi(SignIn)
    SignIn.show()
    sys.exit(app.exec_())

