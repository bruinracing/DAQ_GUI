from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QFileDialog


from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import numpy as np


import csv_reader
import math

class Graph_Page:

	def __init__(self, data_tab):
		self.data_tab = data_tab
		self.figure = Figure()
		self.canvas = FigureCanvas(self.figure)
		self.toolbar = NavigationToolbar(self.canvas, data_tab)
		self.data = list()
		self.titles = list()
		self.check_box_list = list()
		self.checked_list = list()
		self.datum_num = 0
		ts = np.array([])
		self.np_data = list()
		self.prev_ax = list()

		self.layout_two = QtGui.QVBoxLayout()
		self.file_select_button = QtGui.QPushButton("select_file")
		self.update_button = QtGui.QPushButton("update")
		self.button_2 = QtGui.QPushButton("button_2")
		self.layout_two.addWidget(self.file_select_button)
		self.layout_two.addWidget(self.update_button)
		self.file_select_button.clicked.connect(self.select_file)
		self.update_button.clicked.connect(self.update_display)
		self.button_2.clicked.connect(self.action_2)

		self.layout_two.addWidget(self.canvas)
		self.layout_two.addWidget(self.toolbar)


		data_tab.setLayout(self.layout_two)





	def action_1():
		print("pressed button_1")
	def action_2():
		print("pressed button_2")
	def select_file(self):
		filename = QFileDialog.getOpenFileName(self.data_tab, 'Open File', 'C:/')
		if (filename == ""):
			#valid_file = 0
			ax = figure.add_subplot(111)
			ax.clear()
			ax.set_title("NO FILE SELECTED")
		else:
			#valid_file = 1
			csv_tup = csv_reader.read_csv_file(filename)
			self.data = csv_tup[1]
			self.titles = csv_tup[0]
			print("data: "+str(self.data))
			print("titles: "+str(self.titles))
			print("ts: " +str(self.data[0]))
			for i in range(0, len(self.data)):  #creates list of np_arrays
				self.np_data.append(np.array(self.data[i]))
			self.ts = self.np_data[0] #timestamp list
			self.datum_num = len(self.data) -1 # -1 to compensate for ts data
			print("datum_num: "+str(self.datum_num))
			edge = math.ceil(math.sqrt(self.datum_num))
			plot_val = edge*100 + edge*10

			#make graphs
			for i in range(1, self.datum_num+1):
			#x = np.arange(0, np_data[i].size, 1)
				x = self.ts
				y = self.np_data[i]
				ax = self.figure.add_subplot(plot_val + i)
				ax.clear()
				ax.set_title(self.titles[i])
				#ax.scatter(x,y)
				ax.plot(x, y)
				self.prev_ax.append(ax)
			self.canvas.draw()

		print("remove checkboxes")
		#remove old checkboxes
		for checkbox in self.check_box_list:
			self.layout_two.removeWidget(checkbox)
		self.check_box_list.clear() 
		self.checked_list = [0]

		print("make checkboxes")
		#make checkboxes
		for i in range(1, self.datum_num+1):
			check = QtGui.QCheckBox(self.titles[i])
			check.setChecked(True)
			self.layout_two.addWidget(check)
			self.check_box_list.append(check)
			self.checked_list.append(1)

		print("select datum_num: "+str(self.datum_num))

	def update_display(self):
		print("datum_num2: "+str(self.datum_num))
		print("update display")
		self.checked_list = [0]
		#read checkboxes
		for checkbox in self.check_box_list:
			if checkbox.isChecked():
				self.checked_list.append(1)
			else:
				self.checked_list.append(0)
		print("checked_list: "+str(self.checked_list))
		#redraw graphs
		check_count = self.checked_list.count(1)
		e = math.ceil(math.sqrt(check_count))
		pl_v = e*100+e*10
		j = 1

		print("titles: "+str(self.titles))
		print("datum_num"+str(self.datum_num))
		for ax in self.prev_ax:
			ax.cla()
		self.figure.clear()
		for i in range(1, self.datum_num+1):
			if(self.checked_list[i]):
				x = self.ts
				y = self.np_data[i]
				ax = self.figure.add_subplot(pl_v + j)
				j = j+1
				ax.clear()
				ax.set_title(self.titles[i])
				ax.plot(x, y)
				print("redraw: "+str(self.titles[i]))
		self.canvas.draw()









	