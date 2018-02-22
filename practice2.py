# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M:\RMGPP Side projects\qt\practice1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fact_code_input = QtWidgets.QLineEdit(self.centralwidget)
        self.fact_code_input.setGeometry(QtCore.QRect(110, 60, 113, 22))
        self.fact_code_input.setObjectName("fact_code_input")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(100, 220, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(34, 60, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 91, 21))
        self.label_2.setObjectName("label_2")
        self.report_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.report_name_input.setGeometry(QtCore.QRect(120, 130, 113, 22))
        self.report_name_input.setObjectName("report_name_input")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 130, 91, 21))
        self.label_3.setObjectName("label_3")
        self.format_input = QtWidgets.QLineEdit(self.centralwidget)
        self.format_input.setGeometry(QtCore.QRect(360, 130, 113, 22))
        self.format_input.setObjectName("format_input")
        self.doneButton = QtWidgets.QPushButton(self.centralwidget)
        self.doneButton.setGeometry(QtCore.QRect(340, 220, 93, 31))
        self.doneButton.setObjectName("doneButton")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 310, 451, 261))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 31))
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
        self.saveButton.setText(_translate("MainWindow", "save"))
        self.label.setText(_translate("MainWindow", "fact code: "))
        self.label_2.setText(_translate("MainWindow", "report name"))
        self.label_3.setText(_translate("MainWindow", "format"))
        self.doneButton.setText(_translate("MainWindow", "done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

