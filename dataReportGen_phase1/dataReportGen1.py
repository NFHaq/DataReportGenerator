# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'M:\RMGPP Side projects\qt\dataReportGen1.ui'
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


###################################################################
#####  CLASS FOR MODEL CREATION ( TableView Purpose in UI)
###################################################################

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



####################################################################
###                   MAIN CLASS
####################################################################

class Ui_MainWindow(object):

    ###############################################################################################################################
    ###############################################################################################################################
    ##                                LOGIC CODE
    ###############################################################################################################################
    ###############################################################################################################################
    

    ###############################################################
    ######### COVER TAB LOGIC
    # cover_df = pd.DataFrame(columns={'fact_code','contact_type', 'contact_name','designation','contact_number','email','notes'})
    ###############################################################

    def on_saveButton_clicked_coverTab(self):
        cover_df.loc[len(cover_df),'fact_code'] = self.fact_code_input.text()
        cover_df.loc[len(cover_df)-1,'contact_type'] = self.contact_type_input.text()
        cover_df.loc[len(cover_df)-1,'contact_name'] = self.contact_name_input.text()
        cover_df.loc[len(cover_df)-1,'designation'] = self.designation_input.text()
        cover_df.loc[len(cover_df)-1,'contact_number'] = self.contact_number_input.text()
        cover_df.loc[len(cover_df)-1,'email'] = self.email_input.text()
        cover_df.loc[len(cover_df)-1,'notes'] = self.notes_cover_input.text()

        ## showing DF data in tableView
        model = PandasModel(cover_df)
        self.tableView.setModel(model)

        self.contact_type_input.clear()
        self.contact_name_input.clear()
        self.designation_input.clear()
        self.contact_number_input.clear()
        self.email_input.clear()
        self.notes_cover_input.clear()


    def on_doneButton_clicked_coverTab(self):
        #file_name = 'Cover_'+str(cover_df.fact_code.unique()[0])+'.csv'
        #cover_df[['fact_code','contact_type', 'contact_name','designation','contact_number','email','notes']].to_csv(file_name,index=False)
        self.fact_code_input.clear()
        self.fact_code_label_output.setText(str(cover_df.fact_code.unique()[0]))
           
    ##############################################################################################################################
    #####  VISIT LOG TAB LOGIC
    ##### visit_log_df = pd.DataFrame(columns={'date_of_visit','visit_type','#_reports_requested','#_reports_collected','soft_data_%','absolute_varaibles_coverage_%'})
    ##############################################################################################################################

    def showDate(self, date):
        date = self.date_of_visit_calendarWidget.selectedDate()
        self.date_of_visit_label_output.setText(date.toString())

    def on_saveButton_clicked_visit_logTab(self):
        visit_log_df.loc[len(visit_log_df),'date_of_visit'] = self.date_of_visit_label_output.text()
        visit_log_df.loc[len(visit_log_df)-1,'visit_type'] = self.visit_type_visitlog_input.text()
        visit_log_df.loc[len(visit_log_df)-1,'#_reports_requested'] = self.no_reports_requested_input.text()
        visit_log_df.loc[len(visit_log_df)-1,'#_reports_collected'] = self.no_reports_collected_input.text()
        visit_log_df.loc[len(visit_log_df)-1,'soft_data_%'] = self.soft_data_input.text()
        visit_log_df.loc[len(visit_log_df)-1,'absolute_varaibles_coverage_%'] = self.absolute_varaibles_coverage_input.text()
        

        ## showing DF data in tableView2
        model = PandasModel(visit_log_df)
        self.tableView_2.setModel(model)

        self.date_of_visit_label_output.clear()
        self.visit_type_visitlog_input.clear()
        self.no_reports_requested_input.clear()
        self.no_reports_collected_input.clear()
        self.soft_data_input.clear()
        self.absolute_varaibles_coverage_input.clear()


    def on_doneButton_clicked_visit_logTab(self):
        #file_name = 'Visit_Log_'+str(cover_df.fact_code.unique()[0])+'.csv'
        #visit_log_df[['date_of_visit','visit_type','#_reports_requested','#_reports_collected','soft_data_%','absolute_varaibles_coverage_%']].to_csv(file_name,index=False)
        self.fact_code_label_output.clear()

    ##############################################################################################################################
    #####  LIST REPORTS SHEET TAB LOGIC
    ##### list_reports_sheet_df = pd.DataFrame(columns={'sl_no','report_name','format'})
    ##############################################################################################################################   

    def on_saveButton_clicked_list_reports_sheetTab(self):
        list_reports_sheet_df.loc[len(list_reports_sheet_df),'sl_no'] = len(list_reports_sheet_df)+1
        list_reports_sheet_df.loc[len(list_reports_sheet_df)-1,'report_name'] = self.report_name_input.text()
        list_reports_sheet_df.loc[len(list_reports_sheet_df)-1,'format'] = self.format_input.text()
        
        ## Report name => insert in all ComboBox
        self.report_name_comboBox.addItem(self.report_name_input.text())
        self.report_name_comboBox_2.addItem(self.report_name_input.text())
        self.report_name_comboBox_3.addItem(self.report_name_input.text())

       
        ## showing DF data in tableView2
        model = PandasModel(list_reports_sheet_df)
        self.tableView_3.setModel(model)

        self.report_name_input.clear()
        self.format_input.clear()
        

    def on_doneButton_clicked_list_reports_sheetTab(self):
        #file_name = 'List_Reports_Sheet_'+str(cover_df.fact_code.unique()[0])+'.csv'
        #list_reports_sheet_df[['sl_no','report_name','format']].to_csv(file_name,index=False)

        ## ipa data point => insert ComboBox
        for elem in ipa_data_point:
            self.ipa_data_point_comboBox.addItem(elem)


 

    ##############################################################################################################################
    #####  RECEIVED SHEET TAB LOGIC
    ##### received_sheet_df = pd.DataFrame(columns={'report_name','format','timeline','start_time','end_time','notes'})
    ############################################################################################################################## 

    def showStartTime(self, date):
        date = self.start_time_calendarWidget.selectedDate()
        self.start_time_output.setText(date.toString())

        ### comboBox selection => print into label => format_label_output
        report_nm = self.report_name_comboBox.currentText()
        self.format_label_output.setText(list_reports_sheet_df.loc[list_reports_sheet_df.report_name==report_nm].format.unique()[0])


    def showEndTime(self, date):
        date = self.calendarWidget.selectedDate()
        self.end_time_output.setText(date.toString())

    def on_saveButton_clicked_received_sheetTab(self):

        received_sheet_df.loc[len(received_sheet_df),'report_name'] = self.report_name_comboBox.currentText()
        received_sheet_df.loc[len(received_sheet_df)-1,'format'] = self.format_label_output.text()
        received_sheet_df.loc[len(received_sheet_df)-1,'timeline'] = self.timeline_input.text()
        received_sheet_df.loc[len(received_sheet_df)-1,'start_time'] = self.start_time_output.text()
        received_sheet_df.loc[len(received_sheet_df)-1,'end_time'] = self.end_time_output.text()
        received_sheet_df.loc[len(received_sheet_df)-1,'notes'] = self.notes_received_sheet_input.text()
        
       
        ## showing DF data in tableView2
        model = PandasModel(received_sheet_df)
        self.tableView_4.setModel(model)

        self.format_label_output.clear()
        self.timeline_input.clear()
        self.start_time_output.clear()
        self.end_time_output.clear()
        self.notes_received_sheet_input.clear()
        

    def on_doneButton_clicked_received_sheetTab(self):
        #file_name = 'Received_Sheet_'+str(cover_df.fact_code.unique()[0])+'.csv'
        #received_sheet_df[['report_name','format','timeline','start_time','end_time','notes']].to_csv(file_name,index=False)
        print("recieved_sheet DONE")


    ##############################################################################################################################
    #####  DATA INPUT TAB LOGIC
    ##### data_input_df = pd.DataFrame(columns={'report_name','format','sub_sheet','fac_data_point','ipa_data_point','data_availability',
    #####                                        'notes'})
    ############################################################################################################################## 


    def on_saveButton_clicked_data_inputTab(self):

        report_nm = self.report_name_comboBox_2.currentText()
        self.format_label_output_2.setText(list_reports_sheet_df.loc[list_reports_sheet_df.report_name==report_nm].format.unique()[0])

        data_input_df.loc[len(data_input_df),'report_name'] = self.report_name_comboBox_2.currentText()
        data_input_df.loc[len(data_input_df)-1,'format'] = self.format_label_output_2.text()
        data_input_df.loc[len(data_input_df)-1,'sub_sheet'] = self.sub_sheet_input.text()
        data_input_df.loc[len(data_input_df)-1,'ipa_data_point'] = self.ipa_data_point_comboBox.currentText()
        data_input_df.loc[len(data_input_df)-1,'fac_data_point'] = self.fac_data_point_input.text()
        data_input_df.loc[len(data_input_df)-1,'data_availability'] = self.data_avial_comboBox.currentText()
        data_input_df.loc[len(data_input_df)-1,'notes'] = self.notes_datainput_input.text()
        
       
        ## showing DF data in tableView2
        model = PandasModel(data_input_df)
        self.tableView_5.setModel(model)

        self.format_label_output_2.clear()
        self.sub_sheet_input.clear()
        self.fac_data_point_input.clear()
        self.notes_datainput_input.clear()
        

    def on_doneButton_clicked_data_inputTab(self):
        #file_name = 'Data_Input_'+str(cover_df.fact_code.unique()[0])+'.csv'
        #data_input_df[['report_name','format','sub_sheet','fac_data_point','ipa_data_point','data_availability','notes']].to_csv(file_name,index=False)    
        print("data_input DONE")


    ##############################################################################################################################
    #####  REQUEST SHEET TAB LOGIC
    #####  request_sheet_df = pd.DataFrame(columns={'visit_type','report_name','format','data_need_from','untill','breadth','notes'})
    ############################################################################################################################## 


    def on_saveButton_clicked_request_sheetTab(self):

        report_nm = self.report_name_comboBox_3.currentText()
        self.format_label_output_3.setText(list_reports_sheet_df.loc[list_reports_sheet_df.report_name==report_nm].format.unique()[0])

        request_sheet_df.loc[len(request_sheet_df),'visit_type'] = self.visit_type_requestsheet_input.text()
        request_sheet_df.loc[len(request_sheet_df)-1,'report_name'] = self.report_name_comboBox_3.currentText()
        request_sheet_df.loc[len(request_sheet_df)-1,'format'] = self.format_label_output_3.text()


        end_dt = received_sheet_df.loc[(received_sheet_df.report_name==report_nm)].end_time.unique()[0]
        end_dt = end_dt.replace(end_dt.split(' ')[0],'').strip()

        nxt_dt = datetime.strptime(end_dt,"%b %d %Y").date() + timedelta(1)
        nxt_dt = nxt_dt.strftime("%b %d %Y")
        self.data_need_from_label.setText(str(nxt_dt))



        request_sheet_df.loc[len(request_sheet_df)-1,'data_need_from'] = self.data_need_from_label.text()
        
        request_sheet_df.loc[len(request_sheet_df)-1,'untill'] = self.untill_input.text()
        request_sheet_df.loc[len(request_sheet_df)-1,'breadth'] = self.breadth_input.text()
        request_sheet_df.loc[len(request_sheet_df)-1,'notes'] = self.notes_reques_sheet_input.text()
        
       
        ## showing DF data in tableView2
        model = PandasModel(request_sheet_df)
        self.tableView_6.setModel(model)

        self.visit_type_requestsheet_input.clear()
        self.untill_input.clear()
        self.breadth_input.clear()
        self.notes_reques_sheet_input.clear()
        

    def on_doneButton_clicked_request_sheetTab(self):
        #file_name = 'Request_Sheet_'+str(cover_df.fact_code.unique()[0])+'.csv'
        #request_sheet_df[['visit_type','report_name','format','data_need_from','untill','breadth','notes']].to_csv(file_name,index=False) 
        #cover_df = pd.DataFrame(columns={'fact_code','contact_type', 'contact_name','designation','contact_number','email','notes'})
        #visit_log_df = pd.DataFrame(columns={'date_of_visit','visit_type','#_reports_requested','#_reports_collected','soft_data_%','absolute_varaibles_coverage_%'})
        #list_reports_sheet_df = pd.DataFrame(columns={'sl_no','report_name','format'})
        #received_sheet_df = pd.DataFrame(columns={'report_name','format','timeline','start_time','end_time','notes'})
        #data_input_df = pd.DataFrame(columns={'report_name','format','sub_sheet','fac_data_point','ipa_data_point','data_availability',
        #'notes'})
        #request_sheet_df = pd.DataFrame(columns={'visit_type','report_name','format','data_need_from','untill','breadth','notes'})



        file_name = 'Data_Report_'+str(cover_df.fact_code.unique()[0])+'.xlsx'
        #initialze the excel writer
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

        #store your dataframes in a  dict, where the key is the sheet name you want
        #global cover_df, visit_log_df, list_reports_sheet_df, received_sheet_df, data_input_df, request_sheet_df

        frames = {'cover': cover_df[['fact_code','contact_type', 'contact_name','designation','contact_number','email','notes']], 
        'visit_log': visit_log_df[['date_of_visit','visit_type','#_reports_requested','#_reports_collected','soft_data_%','absolute_varaibles_coverage_%']],
        'list_reports_sheet': list_reports_sheet_df[['sl_no','report_name','format']] , 
        'received_sheet':received_sheet_df[['report_name','format','timeline','start_time','end_time','notes']],
        'data_input':data_input_df[['report_name','format','sub_sheet','fac_data_point','ipa_data_point','data_availability','notes']], 
        'request_sheet':request_sheet_df[['visit_type','report_name','format','data_need_from','untill','breadth','notes']]}

        #now loop through and put each on a specific sheet
        for sheet, frame in  frames.items(): # .use .items for python 3.X
            frame.to_excel(writer, sheet_name = sheet)

        #critical last step
        writer.save()   



    ##############################################################################################################################
    ##############################################################################################################################
    ################# UI DESIGN
    ###############################################################################################################################
    ###############################################################################################################################
    ###############################################################################################################################

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 841)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1081, 801))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(10)
        
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")

    ##################################################################################
    ########                     1. COVER TAB
    ##################################################################################

        self.cover_tab = QtWidgets.QWidget()
        self.cover_tab.setObjectName("cover_tab")
        
        self.label = QtWidgets.QLabel(self.cover_tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 51))
        self.label.setObjectName("label")
        
        self.fact_code_input = QtWidgets.QLineEdit(self.cover_tab)
        self.fact_code_input.setGeometry(QtCore.QRect(150, 20, 141, 31))
        self.fact_code_input.setObjectName("fact_code_input")
        
        self.label_2 = QtWidgets.QLabel(self.cover_tab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 121, 51))
        self.label_2.setObjectName("label_2")
        
        self.contact_type_input = QtWidgets.QLineEdit(self.cover_tab)
        self.contact_type_input.setGeometry(QtCore.QRect(150, 80, 391, 71))
        self.contact_type_input.setObjectName("contact_type_input")
        
        self.label_3 = QtWidgets.QLabel(self.cover_tab)
        self.label_3.setGeometry(QtCore.QRect(560, 70, 121, 51))
        self.label_3.setObjectName("label_3")
        
        self.contact_name_input = QtWidgets.QLineEdit(self.cover_tab)
        self.contact_name_input.setGeometry(QtCore.QRect(690, 80, 371, 81))
        self.contact_name_input.setObjectName("contact_name_input")
        
        self.label_4 = QtWidgets.QLabel(self.cover_tab)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 121, 51))
        self.label_4.setObjectName("label_4")
        
        self.designation_input = QtWidgets.QLineEdit(self.cover_tab)
        self.designation_input.setGeometry(QtCore.QRect(150, 180, 391, 71))
        self.designation_input.setObjectName("designation_input")
        
        self.label_5 = QtWidgets.QLabel(self.cover_tab)
        self.label_5.setGeometry(QtCore.QRect(550, 180, 141, 51))
        self.label_5.setObjectName("label_5")
        
        self.contact_number_input = QtWidgets.QLineEdit(self.cover_tab)
        self.contact_number_input.setGeometry(QtCore.QRect(690, 190, 371, 31))
        self.contact_number_input.setObjectName("contact_number_input")
        
        self.label_6 = QtWidgets.QLabel(self.cover_tab)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 61, 51))
        self.label_6.setObjectName("label_6")
        
        self.email_input = QtWidgets.QLineEdit(self.cover_tab)
        self.email_input.setGeometry(QtCore.QRect(150, 270, 391, 31))
        self.email_input.setObjectName("email_input")
        
        self.saveButton = QtWidgets.QPushButton(self.cover_tab)
        self.saveButton.setGeometry(QtCore.QRect(150, 340, 131, 41))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.on_saveButton_clicked_coverTab) ## call on_saveButton_clicked_coverTab
        
        self.doneButton = QtWidgets.QPushButton(self.cover_tab)
        self.doneButton.setGeometry(QtCore.QRect(410, 340, 131, 41))
        self.doneButton.setObjectName("doneButton")
        self.doneButton.clicked.connect(self.on_doneButton_clicked_coverTab) ## call on_doneButton_clicked_coverTab
        
        self.tableView = QtWidgets.QTableView(self.cover_tab)
        self.tableView.setGeometry(QtCore.QRect(30, 400, 1001, 321))
        self.tableView.setObjectName("tableView")
        
        self.label_34 = QtWidgets.QLabel(self.cover_tab)
        self.label_34.setGeometry(QtCore.QRect(550, 260, 61, 51))
        self.label_34.setObjectName("label_34")
        
        self.notes_cover_input = QtWidgets.QLineEdit(self.cover_tab)
        self.notes_cover_input.setGeometry(QtCore.QRect(610, 270, 451, 31))
        self.notes_cover_input.setObjectName("notes_cover_input")
        
        self.tabWidget.addTab(self.cover_tab, "")
    
    #######################################################################################
    #########            2. VISIT LOG TAB
    #######################################################################################

        self.visit_log_tab = QtWidgets.QWidget()
        self.visit_log_tab.setObjectName("visit_log_tab")
        
        self.label_7 = QtWidgets.QLabel(self.visit_log_tab)
        self.label_7.setGeometry(QtCore.QRect(40, 40, 121, 51))
        self.label_7.setObjectName("label_7")
        
        self.fact_code_label_output = QtWidgets.QLabel(self.visit_log_tab)
        self.fact_code_label_output.setGeometry(QtCore.QRect(170, 40, 171, 51))
        self.fact_code_label_output.setText("")
        self.fact_code_label_output.setObjectName("fact_code_label_output")
        
        self.label_8 = QtWidgets.QLabel(self.visit_log_tab)
        self.label_8.setGeometry(QtCore.QRect(340, 40, 121, 51))
        self.label_8.setObjectName("label_8")
            
        self.date_of_visit_calendarWidget = QtWidgets.QCalendarWidget(self.visit_log_tab)
        self.date_of_visit_calendarWidget.setGeometry(QtCore.QRect(700, 40, 331, 241))
        self.date_of_visit_calendarWidget.setObjectName("date_of_visit_calendarWidget")

        # calenderWidget connect while selecting a date
        self.date_of_visit_calendarWidget.clicked[QtCore.QDate].connect(self.showDate)
        

        self.date_of_visit_label_output = QtWidgets.QLabel(self.visit_log_tab)
        self.date_of_visit_label_output.setGeometry(QtCore.QRect(460, 50, 171, 31))
        self.date_of_visit_label_output.setText("")
        self.date_of_visit_label_output.setObjectName("date_of_visit_label_output")
        
        self.label_9 = QtWidgets.QLabel(self.visit_log_tab)
        self.label_9.setGeometry(QtCore.QRect(40, 100, 121, 51))
        self.label_9.setObjectName("label_9")
        
        self.visit_type_visitlog_input = QtWidgets.QLineEdit(self.visit_log_tab)
        self.visit_type_visitlog_input.setGeometry(QtCore.QRect(150, 110, 291, 31))
        self.visit_type_visitlog_input.setObjectName("visit_type_visitlog_input")
        
        self.label_10 = QtWidgets.QLabel(self.visit_log_tab)
        self.label_10.setGeometry(QtCore.QRect(30, 180, 181, 51))
        self.label_10.setObjectName("label_10")
        
        self.no_reports_requested_input = QtWidgets.QLineEdit(self.visit_log_tab)
        self.no_reports_requested_input.setGeometry(QtCore.QRect(220, 190, 141, 31))
        self.no_reports_requested_input.setObjectName("no_reports_requested_input")
        
        self.label_11 = QtWidgets.QLabel(self.visit_log_tab)
        self.label_11.setGeometry(QtCore.QRect(30, 230, 171, 51))
        self.label_11.setObjectName("label_11")
        
        self.no_reports_collected_input = QtWidgets.QLineEdit(self.visit_log_tab)
        self.no_reports_collected_input.setGeometry(QtCore.QRect(220, 240, 141, 31))
        self.no_reports_collected_input.setObjectName("no_reports_collected_input")
        
        self.label_12 = QtWidgets.QLabel(self.visit_log_tab)
        self.label_12.setGeometry(QtCore.QRect(30, 290, 101, 51))
        self.label_12.setObjectName("label_12")
        
        self.soft_data_input = QtWidgets.QLineEdit(self.visit_log_tab)
        self.soft_data_input.setGeometry(QtCore.QRect(130, 300, 131, 31))
        self.soft_data_input.setObjectName("soft_data_input")
        
        self.label_13 = QtWidgets.QLabel(self.visit_log_tab)
        self.label_13.setGeometry(QtCore.QRect(310, 290, 251, 51))
        self.label_13.setObjectName("label_13")
        
        self.absolute_varaibles_coverage_input = QtWidgets.QLineEdit(self.visit_log_tab)
        self.absolute_varaibles_coverage_input.setGeometry(QtCore.QRect(560, 300, 131, 31))
        self.absolute_varaibles_coverage_input.setObjectName("absolute_varaibles_coverage_input")
        
        self.saveButton_2 = QtWidgets.QPushButton(self.visit_log_tab)
        self.saveButton_2.setGeometry(QtCore.QRect(90, 360, 111, 41))
        self.saveButton_2.setObjectName("saveButton_2")
        self.saveButton_2.clicked.connect(self.on_saveButton_clicked_visit_logTab) ## call on_saveButton_clicked_visit_logTab
        
        self.doneButton_2 = QtWidgets.QPushButton(self.visit_log_tab)
        self.doneButton_2.setGeometry(QtCore.QRect(340, 360, 101, 41))
        self.doneButton_2.setObjectName("doneButton_2")
        self.doneButton_2.clicked.connect(self.on_doneButton_clicked_visit_logTab) ## call on_doneButton_clicked_visit_logTab
        
        self.tableView_2 = QtWidgets.QTableView(self.visit_log_tab)
        self.tableView_2.setGeometry(QtCore.QRect(50, 420, 961, 291))
        self.tableView_2.setObjectName("tableView_2")
        
        self.tabWidget.addTab(self.visit_log_tab, "")
        
    ################################################################################################################
    ###########      3. LIST REPORTS SHEET
    ################################################################################################################

        self.list_reports_sheet_tab = QtWidgets.QWidget()
        self.list_reports_sheet_tab.setObjectName("list_reports_sheet_tab")
        
        self.label_15 = QtWidgets.QLabel(self.list_reports_sheet_tab)
        self.label_15.setGeometry(QtCore.QRect(80, 50, 121, 51))
        self.label_15.setObjectName("label_15")
        
        self.report_name_input = QtWidgets.QLineEdit(self.list_reports_sheet_tab)
        self.report_name_input.setGeometry(QtCore.QRect(230, 60, 581, 41))
        self.report_name_input.setObjectName("report_name_input")
        
        self.label_16 = QtWidgets.QLabel(self.list_reports_sheet_tab)
        self.label_16.setGeometry(QtCore.QRect(80, 120, 121, 51))
        self.label_16.setObjectName("label_16")
        
        self.format_input = QtWidgets.QLineEdit(self.list_reports_sheet_tab)
        self.format_input.setGeometry(QtCore.QRect(230, 130, 241, 41))
        self.format_input.setObjectName("format_input")
        
        self.saveButton_3 = QtWidgets.QPushButton(self.list_reports_sheet_tab)
        self.saveButton_3.setGeometry(QtCore.QRect(230, 210, 131, 41))
        self.saveButton_3.setObjectName("saveButton_3")
        self.saveButton_3.clicked.connect(self.on_saveButton_clicked_list_reports_sheetTab) ## call on_saveButton_clicked_list_reports_sheetTab
        
        self.doneButton_3 = QtWidgets.QPushButton(self.list_reports_sheet_tab)
        self.doneButton_3.setGeometry(QtCore.QRect(440, 210, 131, 41))
        self.doneButton_3.setObjectName("doneButton_3")
        self.doneButton_3.clicked.connect(self.on_doneButton_clicked_list_reports_sheetTab) ## call on_doneButton_clicked_list_reports_sheetTab
        
        self.tableView_3 = QtWidgets.QTableView(self.list_reports_sheet_tab)
        self.tableView_3.setGeometry(QtCore.QRect(70, 280, 941, 361))
        self.tableView_3.setObjectName("tableView_3")
        
        self.tabWidget.addTab(self.list_reports_sheet_tab, "")

    ##################################################################################################    
    ######          4. RECEIVED SHEET TAB
    ##################################################################################################

        self.received_sheet_tab = QtWidgets.QWidget()
        self.received_sheet_tab.setObjectName("received_sheet_tab")
        
        self.label_14 = QtWidgets.QLabel(self.received_sheet_tab)
        self.label_14.setGeometry(QtCore.QRect(40, 30, 111, 41))
        self.label_14.setObjectName("label_14")
        
        self.report_name_comboBox = QtWidgets.QComboBox(self.received_sheet_tab)
        self.report_name_comboBox.setGeometry(QtCore.QRect(180, 30, 181, 41))
        self.report_name_comboBox.setObjectName("report_name_comboBox")


        self.label_17 = QtWidgets.QLabel(self.received_sheet_tab)
        self.label_17.setGeometry(QtCore.QRect(400, 30, 111, 41))
        self.label_17.setObjectName("label_17")
        
        self.format_label_output = QtWidgets.QLabel(self.received_sheet_tab)
        self.format_label_output.setGeometry(QtCore.QRect(470, 30, 141, 41))
        self.format_label_output.setText("")
        self.format_label_output.setObjectName("format_label_output")

        ###
        ### ComboBox Code edit
        ###
        
        ###
        ###
        ###
        
        self.label_18 = QtWidgets.QLabel(self.received_sheet_tab)
        self.label_18.setGeometry(QtCore.QRect(630, 30, 111, 41))
        self.label_18.setObjectName("label_18")
        
        self.timeline_input = QtWidgets.QLineEdit(self.received_sheet_tab)
        self.timeline_input.setGeometry(QtCore.QRect(730, 40, 251, 41))
        self.timeline_input.setObjectName("timeline_input")
        
        self.label_19 = QtWidgets.QLabel(self.received_sheet_tab)
        self.label_19.setGeometry(QtCore.QRect(30, 90, 111, 41))
        self.label_19.setObjectName("label_19")
        
        self.start_time_output = QtWidgets.QLabel(self.received_sheet_tab)
        self.start_time_output.setGeometry(QtCore.QRect(10, 130, 131, 31))
        self.start_time_output.setText("")
        self.start_time_output.setObjectName("start_time_output")
        
        self.start_time_calendarWidget = QtWidgets.QCalendarWidget(self.received_sheet_tab)
        self.start_time_calendarWidget.setGeometry(QtCore.QRect(150, 100, 311, 211))
        self.start_time_calendarWidget.setObjectName("start_time_calendarWidget")

        # calenderWidget connect while selecting a date=> start time
        self.start_time_calendarWidget.clicked[QtCore.QDate].connect(self.showStartTime)
        

        self.label_20 = QtWidgets.QLabel(self.received_sheet_tab)
        self.label_20.setGeometry(QtCore.QRect(550, 100, 111, 41))
        self.label_20.setObjectName("label_20")
        
        self.end_time_output = QtWidgets.QLabel(self.received_sheet_tab)
        self.end_time_output.setGeometry(QtCore.QRect(550, 140, 121, 31))
        self.end_time_output.setText("")
        self.end_time_output.setObjectName("end_time_output")
        
        self.calendarWidget = QtWidgets.QCalendarWidget(self.received_sheet_tab)
        self.calendarWidget.setGeometry(QtCore.QRect(680, 100, 311, 211))
        self.calendarWidget.setObjectName("calendarWidget")

        # calenderWidget connect while selecting a date=> end time
        self.calendarWidget.clicked[QtCore.QDate].connect(self.showEndTime)
        
        self.tableView_4 = QtWidgets.QTableView(self.received_sheet_tab)
        self.tableView_4.setGeometry(QtCore.QRect(30, 490, 991, 261))
        self.tableView_4.setObjectName("tableView_4")
        
        self.saveButton_4 = QtWidgets.QPushButton(self.received_sheet_tab)
        self.saveButton_4.setGeometry(QtCore.QRect(270, 420, 121, 41))
        self.saveButton_4.setObjectName("saveButton_4")
        self.saveButton_4.clicked.connect(self.on_saveButton_clicked_received_sheetTab) ## call on_saveButton_clicked_data_inputTab
        
        self.doneButton_4 = QtWidgets.QPushButton(self.received_sheet_tab)
        self.doneButton_4.setGeometry(QtCore.QRect(520, 420, 121, 41))
        self.doneButton_4.setObjectName("doneButton_4")
        self.doneButton_4.clicked.connect(self.on_doneButton_clicked_received_sheetTab) ## call on_doneButton_clicked_received_sheetTab
        
        self.label_35 = QtWidgets.QLabel(self.received_sheet_tab)
        self.label_35.setGeometry(QtCore.QRect(30, 330, 111, 41))
        self.label_35.setObjectName("label_35")
        
        self.notes_received_sheet_input = QtWidgets.QLineEdit(self.received_sheet_tab)
        self.notes_received_sheet_input.setGeometry(QtCore.QRect(150, 340, 841, 41))
        self.notes_received_sheet_input.setObjectName("notes_received_sheet_input")
        
        
        self.tabWidget.addTab(self.received_sheet_tab, "")

     ############################################################################################################### 
     ########       5. DATA INPUT TAB
     ###############################################################################################################

        self.data_input_tab = QtWidgets.QWidget()
        self.data_input_tab.setObjectName("data_input_tab")
        
        self.label_21 = QtWidgets.QLabel(self.data_input_tab)
        self.label_21.setGeometry(QtCore.QRect(50, 30, 111, 41))
        self.label_21.setObjectName("label_21")
        
        self.report_name_comboBox_2 = QtWidgets.QComboBox(self.data_input_tab)
        self.report_name_comboBox_2.setGeometry(QtCore.QRect(170, 40, 201, 31))
        self.report_name_comboBox_2.setObjectName("report_name_comboBox_2")
        
        self.label_22 = QtWidgets.QLabel(self.data_input_tab)
        self.label_22.setGeometry(QtCore.QRect(410, 40, 101, 31))
        self.label_22.setObjectName("label_22")
        
        self.format_label_output_2 = QtWidgets.QLabel(self.data_input_tab)
        self.format_label_output_2.setGeometry(QtCore.QRect(490, 40, 141, 41))
        self.format_label_output_2.setText("")
        self.format_label_output_2.setObjectName("format_label_output_2")
        
        self.label_23 = QtWidgets.QLabel(self.data_input_tab)
        self.label_23.setGeometry(QtCore.QRect(650, 40, 101, 31))
        self.label_23.setObjectName("label_23")
        
        self.sub_sheet_input = QtWidgets.QLineEdit(self.data_input_tab)
        self.sub_sheet_input.setGeometry(QtCore.QRect(740, 40, 251, 31))
        self.sub_sheet_input.setObjectName("sub_sheet_input")
        
        self.label_24 = QtWidgets.QLabel(self.data_input_tab)
        self.label_24.setGeometry(QtCore.QRect(600, 100, 131, 31))
        self.label_24.setObjectName("label_24")
        
        self.fac_data_point_input = QtWidgets.QLineEdit(self.data_input_tab)
        self.fac_data_point_input.setGeometry(QtCore.QRect(740, 100, 251, 31))
        self.fac_data_point_input.setObjectName("fac_data_point_input")
        
        self.label_25 = QtWidgets.QLabel(self.data_input_tab)
        self.label_25.setGeometry(QtCore.QRect(40, 100, 131, 31))
        self.label_25.setObjectName("label_25")
        
        self.ipa_data_point_comboBox = QtWidgets.QComboBox(self.data_input_tab)
        self.ipa_data_point_comboBox.setGeometry(QtCore.QRect(170, 100, 201, 31))
        self.ipa_data_point_comboBox.setObjectName("ipa_data_point_comboBox")
        
        self.label_26 = QtWidgets.QLabel(self.data_input_tab)
        self.label_26.setGeometry(QtCore.QRect(40, 160, 131, 31))
        self.label_26.setObjectName("label_26")
        
        self.data_avial_comboBox = QtWidgets.QComboBox(self.data_input_tab)
        self.data_avial_comboBox.setGeometry(QtCore.QRect(180, 160, 201, 31))
        self.data_avial_comboBox.setObjectName("data_avial_comboBox")
        self.data_avial_comboBox.addItem("")
        self.data_avial_comboBox.addItem("")
        self.data_avial_comboBox.addItem("")
        
        self.label_27 = QtWidgets.QLabel(self.data_input_tab)
        self.label_27.setGeometry(QtCore.QRect(410, 160, 101, 31))
        self.label_27.setObjectName("label_27")
        
        self.notes_datainput_input = QtWidgets.QLineEdit(self.data_input_tab)
        self.notes_datainput_input.setGeometry(QtCore.QRect(490, 160, 531, 31))
        self.notes_datainput_input.setObjectName("notes_datainput_input")
        
        self.tableView_5 = QtWidgets.QTableView(self.data_input_tab)
        self.tableView_5.setGeometry(QtCore.QRect(40, 300, 991, 441))
        self.tableView_5.setObjectName("tableView_5")
        
        self.saveButton_5 = QtWidgets.QPushButton(self.data_input_tab)
        self.saveButton_5.setGeometry(QtCore.QRect(230, 230, 121, 41))
        self.saveButton_5.setObjectName("saveButton_5")
        self.saveButton_5.clicked.connect(self.on_saveButton_clicked_data_inputTab) ## call on_saveButton_clicked_data_inputTab
        
        self.doneButton_5 = QtWidgets.QPushButton(self.data_input_tab)
        self.doneButton_5.setGeometry(QtCore.QRect(480, 230, 121, 41))
        self.doneButton_5.setObjectName("doneButton_5")
        self.doneButton_5.clicked.connect(self.on_doneButton_clicked_data_inputTab) ## call on_doneButton_clicked_data_inputTab
        
        self.tabWidget.addTab(self.data_input_tab, "")
        
    ###################################################################################   
    ############      6. REQUEST SHEET TAB
    ####################################################################################

        self.request_sheet_tab = QtWidgets.QWidget()
        self.request_sheet_tab.setObjectName("request_sheet_tab")
        
        self.label_28 = QtWidgets.QLabel(self.request_sheet_tab)
        self.label_28.setGeometry(QtCore.QRect(40, 40, 101, 41))
        self.label_28.setObjectName("label_28")
        
        self.visit_type_requestsheet_input = QtWidgets.QLineEdit(self.request_sheet_tab)
        self.visit_type_requestsheet_input.setGeometry(QtCore.QRect(160, 40, 261, 41))
        self.visit_type_requestsheet_input.setObjectName("visit_type_requestsheet_input")
        
        self.label_29 = QtWidgets.QLabel(self.request_sheet_tab)
        self.label_29.setGeometry(QtCore.QRect(480, 40, 111, 41))
        self.label_29.setObjectName("label_29")
        
        self.report_name_comboBox_3 = QtWidgets.QComboBox(self.request_sheet_tab)
        self.report_name_comboBox_3.setGeometry(QtCore.QRect(610, 40, 261, 31))
        self.report_name_comboBox_3.setObjectName("report_name_comboBox_3")
        
        self.label_30 = QtWidgets.QLabel(self.request_sheet_tab)
        self.label_30.setGeometry(QtCore.QRect(40, 110, 81, 31))
        self.label_30.setObjectName("label_30")
        
        self.format_label_output_3 = QtWidgets.QLabel(self.request_sheet_tab)
        self.format_label_output_3.setGeometry(QtCore.QRect(160, 100, 141, 41))
        self.format_label_output_3.setText("")
        self.format_label_output_3.setObjectName("format_label_output_3")
        
        self.label_31 = QtWidgets.QLabel(self.request_sheet_tab)
        self.label_31.setGeometry(QtCore.QRect(480, 110, 131, 41))
        self.label_31.setObjectName("label_31")
        
        self.data_need_from_label = QtWidgets.QLabel(self.request_sheet_tab)
        self.data_need_from_label.setGeometry(QtCore.QRect(620, 110, 191, 41))
        self.data_need_from_label.setText("")
        self.data_need_from_label.setObjectName("data_need_from_label")
        
        self.label_32 = QtWidgets.QLabel(self.request_sheet_tab)
        self.label_32.setGeometry(QtCore.QRect(40, 170, 81, 31))
        self.label_32.setObjectName("label_32")
        
        self.untill_input = QtWidgets.QLineEdit(self.request_sheet_tab)
        self.untill_input.setGeometry(QtCore.QRect(150, 160, 261, 41))
        self.untill_input.setObjectName("untill_input")
        
        self.label_33 = QtWidgets.QLabel(self.request_sheet_tab)
        self.label_33.setGeometry(QtCore.QRect(480, 160, 81, 31))
        self.label_33.setObjectName("label_33")
        
        self.breadth_input = QtWidgets.QLineEdit(self.request_sheet_tab)
        self.breadth_input.setGeometry(QtCore.QRect(570, 160, 261, 41))
        self.breadth_input.setObjectName("breadth_input")
        
        self.saveButton_6 = QtWidgets.QPushButton(self.request_sheet_tab)
        self.saveButton_6.setGeometry(QtCore.QRect(210, 340, 121, 41))
        self.saveButton_6.setObjectName("saveButton_6")
        self.saveButton_6.clicked.connect(self.on_saveButton_clicked_request_sheetTab) ## call on_saveButton_clicked_request_sheetTab
        
        self.doneButton_6 = QtWidgets.QPushButton(self.request_sheet_tab)
        self.doneButton_6.setGeometry(QtCore.QRect(440, 340, 121, 41))
        self.doneButton_6.setObjectName("doneButton_6")
        self.doneButton_6.clicked.connect(self.on_doneButton_clicked_request_sheetTab) ## call on_saveButton_clicked_request_sheetTab
        
        self.tableView_6 = QtWidgets.QTableView(self.request_sheet_tab)
        self.tableView_6.setGeometry(QtCore.QRect(20, 420, 1021, 331))
        self.tableView_6.setObjectName("tableView_6")
        
        self.label_36 = QtWidgets.QLabel(self.request_sheet_tab)
        self.label_36.setGeometry(QtCore.QRect(40, 250, 81, 31))
        self.label_36.setObjectName("label_36")
        
        self.notes_reques_sheet_input = QtWidgets.QLineEdit(self.request_sheet_tab)
        self.notes_reques_sheet_input.setGeometry(QtCore.QRect(150, 240, 851, 41))
        self.notes_reques_sheet_input.setObjectName("notes_reques_sheet_input")
        
        self.tabWidget.addTab(self.request_sheet_tab, "")
        
    ############################################################################################
    ############################################################################################
    ############################################################################################

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Report Generator"))
        self.label.setText(_translate("MainWindow", "Factory Code"))
        self.label_2.setText(_translate("MainWindow", "Contact Type"))
        self.label_3.setText(_translate("MainWindow", "Contact Name"))
        self.label_4.setText(_translate("MainWindow", "Designation"))
        self.label_5.setText(_translate("MainWindow", "Contact Number"))
        self.label_6.setText(_translate("MainWindow", "Email"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.doneButton.setText(_translate("MainWindow", "Done"))
        self.label_34.setText(_translate("MainWindow", "Notes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cover_tab), _translate("MainWindow", "Cover"))
        self.label_7.setText(_translate("MainWindow", "Factory Code"))
        self.label_8.setText(_translate("MainWindow", "Date of Visit"))
        self.label_9.setText(_translate("MainWindow", "Visit Type"))
        self.label_10.setText(_translate("MainWindow", "# Reports Requested"))
        self.label_11.setText(_translate("MainWindow", "# Reports Collected"))
        self.label_12.setText(_translate("MainWindow", "Soft data %"))
        self.label_13.setText(_translate("MainWindow", "Absolute Variables Coverage %"))
        self.saveButton_2.setText(_translate("MainWindow", "Save"))
        self.doneButton_2.setText(_translate("MainWindow", "Done"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visit_log_tab), _translate("MainWindow", "Visit Log"))
        self.label_15.setText(_translate("MainWindow", "Report Name"))
        self.label_16.setText(_translate("MainWindow", "Format"))
        self.saveButton_3.setText(_translate("MainWindow", "Save"))
        self.doneButton_3.setText(_translate("MainWindow", "Done"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.list_reports_sheet_tab), _translate("MainWindow", "List Reports Sheet"))
        self.label_14.setText(_translate("MainWindow", "Report Name"))
        self.label_17.setText(_translate("MainWindow", "Format"))
        self.label_18.setText(_translate("MainWindow", "Timeline"))
        self.label_19.setText(_translate("MainWindow", "Start Time"))
        self.label_20.setText(_translate("MainWindow", "End Time"))
        self.saveButton_4.setText(_translate("MainWindow", "Save"))
        self.doneButton_4.setText(_translate("MainWindow", "Done"))
        self.label_35.setText(_translate("MainWindow", "Notes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.received_sheet_tab), _translate("MainWindow", "Received Sheet"))
        self.label_21.setText(_translate("MainWindow", "Report Name"))
        self.label_22.setText(_translate("MainWindow", "Format"))
        self.label_23.setText(_translate("MainWindow", "Sub sheet"))
        self.label_24.setText(_translate("MainWindow", "Fac Data Point"))
        self.label_25.setText(_translate("MainWindow", "IPA Data Point"))
        self.label_26.setText(_translate("MainWindow", "Data Availability"))
        self.data_avial_comboBox.setItemText(0, _translate("MainWindow", "direct"))
        self.data_avial_comboBox.setItemText(1, _translate("MainWindow", "indirect"))
        self.data_avial_comboBox.setItemText(2, _translate("MainWindow", "not available"))
        self.label_27.setText(_translate("MainWindow", "Notes"))
        self.saveButton_5.setText(_translate("MainWindow", "Save"))
        self.doneButton_5.setText(_translate("MainWindow", "Done"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_input_tab), _translate("MainWindow", "Data Input"))
        self.label_28.setText(_translate("MainWindow", "Visit Type"))
        self.label_29.setText(_translate("MainWindow", "Report Name"))
        self.label_30.setText(_translate("MainWindow", "Format"))
        self.label_31.setText(_translate("MainWindow", "Data need from"))
        self.label_32.setText(_translate("MainWindow", "Untill"))
        self.label_33.setText(_translate("MainWindow", "Breadth"))
        self.saveButton_6.setText(_translate("MainWindow", "Save"))
        self.doneButton_6.setText(_translate("MainWindow", "Done"))
        self.label_36.setText(_translate("MainWindow", "Notes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.request_sheet_tab), _translate("MainWindow", "Request Sheet"))

#################################################################################################################################
#################################################################################################################################
####
####               START POINT
#################################################################################################################################
#################################################################################################################################

if __name__ == "__main__":
    import sys

    ### decalring all global varaibales

    global cover_df, visit_log_df, list_reports_sheet_df, received_sheet_df, data_input_df, request_sheet_df, ipa_data_point

    cover_df = pd.DataFrame(columns={'fact_code','contact_type', 'contact_name','designation','contact_number','email','notes'})
    visit_log_df = pd.DataFrame(columns={'date_of_visit','visit_type','#_reports_requested','#_reports_collected','soft_data_%','absolute_varaibles_coverage_%'})
    list_reports_sheet_df = pd.DataFrame(columns={'sl_no','report_name','format'})
    received_sheet_df = pd.DataFrame(columns={'report_name','format','timeline','start_time','end_time','notes'})
    data_input_df = pd.DataFrame(columns={'report_name','format','sub_sheet','fac_data_point','ipa_data_point','data_availability',
        'notes'})
    request_sheet_df = pd.DataFrame(columns={'visit_type','report_name','format','data_need_from','untill','breadth','notes'})

    ipa_data_point_df = pd.read_csv(r"./ipa data point/ipa_data_point.csv")
    ipa_data_point = list(ipa_data_point_df['ipa_data_point'].unique())
    #print(ipa_data_point)


   ########################################################################
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

