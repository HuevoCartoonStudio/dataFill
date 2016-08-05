import sys
from PySide.QtCore import *
from PySide.QtGui import *

#sys.path.insert(0, './test/model/mongodbtest2/')

#from Users import Users

class FillTable:
	def __init__(self, is_labels = False):
		self.__table = None
		self.__data = None
		self.__tokens = []
		self.__labels = []
		self.__is_labels = is_labels
	
	def setTable(self, table):
		self.__table = table
	
	def setData(self, data):
		self.__data = data

	def addToken(self, token):
		self.__tokens.append(token)
		
	def addLabel(self, label):
		self.__labels.append(label)
		
	def addField(self, token, label):
		self.__tokens.append(token)
		self.__labels.append(label)
		
	def fill(self):
		if (len(self.__tokens) is 0):
			print('hello')
		else:
			print('bye')
		self.__table.setRowCount(len(self.__data))
		#self.__table.setColumnCount(len(self.__data[0].getData()))
		self.__table.setColumnCount(len(self.__tokens))
		
		#for i in range(len(self.__tokens)):
			#print('Hola')
			
		for i in range(len(self.__data)):
			for j in range(len(self.__tokens)):
				print(self.__tokens[j])
				# print(self.__data[i].getField(self.__tokens[j]))
				if (self.__tokens[j] is 'Id'):
					self.__table.setItem(i, j, QTableWidgetItem((str(self.__data[i].getId()))))
				else:
					self.__table.setItem(i, j, QTableWidgetItem((str(self.__data[i].getField(self.__tokens[j])))))
				
		#self.__table.setHorizontalHeaderLabels(QString("H1;H2;").split(";"))
		self.__table.setHorizontalHeaderLabels(self.__labels)
 
		#table.setItem(0,0, QTableWidgetItem("Item (1,1)"))
		#table.setItem(0,1, QTableWidgetItem("Item (1,2)"))
		#table.setItem(1,0, QTableWidgetItem("Item (2,1)"))
		#table.setItem(1,1, QTableWidgetItem("Item (2,2)"))
		#table.setItem(2,0, QTableWidgetItem("Item (3,1)"))
		#table.setItem(2,1, QTableWidgetItem("Item (3,2)"))
		#table.setItem(3,0, QTableWidgetItem("Item (4,1)"))
		#table.setItem(3,1, QTableWidgetItem("Item (4,2)"))