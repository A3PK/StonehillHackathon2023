# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Aksh\Downloads\Daily_Checklist.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Checklist(object):
    def setupUi(self, Checklist):
        Checklist.setObjectName("Checklist")
        Checklist.resize(300, 533)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        Checklist.setFont(font)
        Checklist.setStyleSheet("background-color:#FFFFFF;\n"
"")
        self.centralwidget = QtWidgets.QWidget(Checklist)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 220, 30))
        self.label.setStyleSheet("font-family:verdana;font-size:15pt;font-color:rgb(0, 0, 0)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-10, 110, 311, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        Checklist.setCentralWidget(self.centralwidget)

        self.retranslateUi(Checklist)
        QtCore.QMetaObject.connectSlotsByName(Checklist)

    def retranslateUi(self, Checklist):
        _translate = QtCore.QCoreApplication.translate
        Checklist.setWindowTitle(_translate("Checklist", "MainWindow"))
        self.label.setText(_translate("Checklist", "Daily Checklist"))
        self.checkBox_2.setText(_translate("Checklist", "Attend the community function"))
        self.checkBox_3.setText(_translate("Checklist", "Have a full 3 meals"))
        self.checkBox_4.setText(_translate("Checklist", "Take a walk or get some excersise for 20 minutes"))
        self.checkBox.setText(_translate("Checklist", "Ask the drivers to get groceries"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Checklist = QtWidgets.QMainWindow()
    ui = Ui_Checklist()
    ui.setupUi(Checklist)
    Checklist.show()
    sys.exit(app.exec_())
