import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

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

class first_main(QDialog):
	def __init__(self):
		super(first_main,self).__init__()
		loadUi('practice1.ui',self)
		self.setWindowTitle('List Reports Sheet')

		global list_reports_sheet
		list_reports_sheet = pd.DataFrame(columns={'fact_code','report_name','format'})

		self.saveButton.clicked.connect(self.on_saveButton_clicked)
		self.doneButton.clicked.connect(self.on_doneButton_clicked)
	@pyqtSlot()
	def on_saveButton_clicked(self):
		list_reports_sheet.loc[len(list_reports_sheet),'fact_code'] = self.fact_code_input.text()
		list_reports_sheet.loc[len(list_reports_sheet)-1,'report_name'] = self.report_name_input.text()
		list_reports_sheet.loc[len(list_reports_sheet)-1,'format'] = self.format_input.text()

	def on_doneButton_clicked(self):
		file_name = 'List Reports Sheet'+str(list_reports_sheet.fact_code.unique()[0])+'.csv'
		list_reports_sheet[['fact_code','report_name','format']].to_csv(file_name,index=False)

app = QApplication(sys.argv)
widget = first_main()
widget.show()
sys.exit(app.exec_())		

