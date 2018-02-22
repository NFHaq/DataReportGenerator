# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M:\RMGPP Side projects\qt\practice1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import pandas as pd
import os
from IPython.core.display import HTML
import re
from pandas import DataFrame
import numpy as np
from numpy import nan as NA
from IPython.core.display import HTML
from IPython.core.display import Image 
import matplotlib.pylab as pylab
from itertools import chain
import datetime, itertools, os, collections, re
import math
import time
from time import mktime
from datetime import datetime, timedelta
import ExcelExtraction
from time import mktime

class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pd.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.ix[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()

################ Main Class ##############
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
        self.saveButton.clicked.connect(self.on_saveButton_clicked) ## call on_saveButton_clicked
        
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
        self.doneButton.clicked.connect(self.on_doneButton_clicked) ## call on_doneButton_clicked
        
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Report Generator"))
        self.saveButton.setText(_translate("MainWindow", "save"))
        self.label.setText(_translate("MainWindow", "fact code: "))
        self.label_2.setText(_translate("MainWindow", "report name"))
        self.label_3.setText(_translate("MainWindow", "format"))
        self.doneButton.setText(_translate("MainWindow", "done"))

    def on_saveButton_clicked(self):
        list_reports_sheet.loc[len(list_reports_sheet),'fact_code'] = self.fact_code_input.text()
        list_reports_sheet.loc[len(list_reports_sheet)-1,'report_name'] = self.report_name_input.text()
        list_reports_sheet.loc[len(list_reports_sheet)-1,'format'] = self.format_input.text()

        ## showing DF data in tableView
        model = PandasModel(list_reports_sheet)
        self.tableView.setModel(model)

        self.report_name_input.clear()
        self.format_input.clear()

    def on_doneButton_clicked(self):
        file_name = 'List Reports Sheet'+str(list_reports_sheet.fact_code.unique()[0])+'.csv'
        list_reports_sheet[['fact_code','report_name','format']].to_csv(file_name,index=False)
        self.fact_code_input.clear()
    


if __name__ == "__main__":
    import sys
    global list_reports_sheet
    list_reports_sheet = pd.DataFrame(columns={'fact_code','report_name','format'})

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

