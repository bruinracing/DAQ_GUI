import sys
import math
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QFileDialog

import numpy as np
import matplotlib.pyplot as plt


from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import csv_reader
import graph_page

 
def set_data_log_tab(data_tab):
	filename = ""
	valid_file = 0
	
	figure = Figure()
	canvas = FigureCanvas(figure)
	toolbar = NavigationToolbar(canvas, data_tab)


	data = list()
	titles = list()
	check_box_list = list()
	checked_list = [0]
	datum_num = 0
	ts = np.array([])
	np_data = list()

	layout_two = QtGui.QVBoxLayout()

	def action_1():
		print("pressed button_1")
	def action_2():
		print("pressed button_2")
	def select_file():
		filename = QFileDialog.getOpenFileName(data_tab, 'Open File', 'C:/')
		if (filename == ""):
			valid_file = 0
			ax = figure.add_subplot(111)
			ax.clear()
			ax.set_title("NO FILE SELECTED")
		else:
			valid_file = 1
			csv_tup = csv_reader.read_csv_file(filename)
			data = csv_tup[1]
			titles = csv_tup[0]
			print("data: "+str(data))
			print("titles: "+str(titles))
			print("ts: " +str(data[0]))
			for i in range(0, len(data)):  #creates list of np_arrays
				np_data.append(np.array(data[i]))
			ts = np_data[0] #timestamp list
			datum_num = len(data) -1 # -1 to compensate for ts data
			print("datum_num: "+str(datum_num))
			edge = math.ceil(math.sqrt(datum_num))
			plot_val = edge*100 + edge*10

			#make graphs
			for i in range(1, datum_num+1):
			#x = np.arange(0, np_data[i].size, 1)
				x = ts
				y = np_data[i]
				ax = figure.add_subplot(plot_val + i)
				ax.clear()
				ax.set_title(titles[i])
				#ax.scatter(x,y)
				ax.plot(x, y)
			canvas.draw()

			print("remove checkboxes")
			#remove old checkboxes
			for checkbox in check_box_list:
				layout_two.removeWidget(checkbox)
			check_box_list.clear() 
			checked_list = [0]

			print("make checkboxes")
			#make checkboxes
			for i in range(1, datum_num+1):
				check = QtGui.QCheckBox(titles[i])
				check.setChecked(True)
				layout_two.addWidget(check)
				check_box_list.append(check)
				checked_list.append(1)

			print("select datum_num: "+str(datum_num))

	def update_display(dat_num):
		print("datum_num2: "+str(int(dat_num)))
		print("update display")
		checked_list = [0]
		#read checkboxes
		for checkbox in check_box_list:
			if checkbox.isChecked():
				checked_list.append(1)
			else:
				checked_list.append(0)
		print("checked_list: "+str(checked_list))
		#redraw graphs
		check_count = checked_list.count(1)
		e = math.ceil(math.sqrt(check_count))
		pl_v = e*100+e*10
		j = 1

		print("titles: "+str(titles))
		print("datum_num"+str(dat_num))
		for i in range(1, 7):
			print("loop: "+str(i))
			if(checked_list[i]):
				x = ts
				y = np_data[i]
				ax = figure.add_subplot(pl_v + j)
				j = j+1
				ax.clear()
				ax.set_title(titles[i])
				ax.plot(x, y)
		canvas.draw()









	file_select_button = QtGui.QPushButton("select_file")
	update_button = QtGui.QPushButton("update")
	button_2 = QtGui.QPushButton("button_2")
	layout_two.addWidget(file_select_button)
	layout_two.addWidget(update_button)
	#layout_two.addWidget(button_4)
	file_select_button.clicked.connect(select_file)
	print("first datum_num: "+str(datum_num))
	update_button.clicked.connect(update_display, datum_num)
	button_2.clicked.connect(action_2)


	

	layout_two.addWidget(canvas)
	layout_two.addWidget(toolbar)


	data_tab.setLayout(layout_two)

def set_generic_tab(gen_tab):

	def file_dialog():
		
		print(filename)

	vBoxlayout	= QtGui.QVBoxLayout()
	pushButton1 = QtGui.QPushButton("Start")
	pushButton2 = QtGui.QPushButton("Settings")
	pushButton3 = QtGui.QPushButton("Stop")
	pushButton1.clicked.connect(file_dialog)

	check1 = QtGui.QCheckBox("button")
	check1.setChecked(True)

	vBoxlayout.addWidget(check1)
	vBoxlayout.addWidget(pushButton1)
	vBoxlayout.addWidget(pushButton2)
	vBoxlayout.addWidget(pushButton3)
	gen_tab.setLayout(vBoxlayout)  


def main():
	app 	= QtGui.QApplication(sys.argv)
	tabs	= QtGui.QTabWidget()

	# Create tabs
	tab1	= QtGui.QWidget()
	tab2	= QtGui.QWidget()

	tabs.resize(1200, 1000)

	# Set layout of first tab
	set_generic_tab(tab1)


	# set layout of data_logs tab
	#set_data_log_tab(tab2)
	gp = graph_page.Graph_Page(tab2)
 
	# Add tabs
	tabs.addTab(tab2,"data_logs")
	tabs.addTab(tab1,"GPS_pos")
 
	# Set title and show
	tabs.setWindowTitle('Jesse is great')
	tabs.show()
 
	sys.exit(app.exec_())
 
 
if __name__ == '__main__':
	main()