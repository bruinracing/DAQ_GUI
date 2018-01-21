import sys
import math
from PyQt4 import QtGui
from PyQt4 import QtCore

import numpy as np
import matplotlib.pyplot as plt


from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import csv_reader

 
def main():
	tup = csv_reader.read_csv_file(sys.argv[1])
	data = tup[1]
	titles = tup[0]
	print("data: "+str(data))
	print("titlese: "+str(titles))
	np_data = list()
	for i in range(0, len(data)):
		np_data.append(np.array(data[i][1:]))
		print("np_type: "+ str(type(np_data[i][0])))
	datum_num = len(data)
	edge = math.ceil(math.sqrt(datum_num))
	plot_val = edge*100 + edge*10



	app 	= QtGui.QApplication(sys.argv)
	tabs	= QtGui.QTabWidget()

	# Create tabs
	tab1	= QtGui.QWidget()
	tab2	= QtGui.QWidget()

	tabs.resize(1200, 1000)

	# Set layout of first tab
	vBoxlayout	= QtGui.QVBoxLayout()
	pushButton1 = QtGui.QPushButton("Start")
	pushButton2 = QtGui.QPushButton("Settings")
	pushButton3 = QtGui.QPushButton("Stop")
	vBoxlayout.addWidget(pushButton1)
	vBoxlayout.addWidget(pushButton2)
	vBoxlayout.addWidget(pushButton3)
	tab1.setLayout(vBoxlayout)   

	layout_two = QtGui.QVBoxLayout()

	button_3 = QtGui.QPushButton("show()")
	button_4 = QtGui.QPushButton("data_read")
	figure = Figure()
	canvas = FigureCanvas(figure)
	toolbar = NavigationToolbar(canvas, tab2)

	layout_two.addWidget(canvas)
	layout_two.addWidget(toolbar)
	layout_two.addWidget(button_3)
	layout_two.addWidget(button_4)

	tab2.setLayout(layout_two)


	def on_click_1():
		x = np.arange(0, 5, 0.1)
		y = np.sin(x)
		plt.subplot(211)
		plt.plot(x, y)
		plt.show()

	def on_click_2():
		x = np.arange(0, 5, 0.1)
		y = np.sin(x)
		plt.subplot(212)
		plt.plot(x, y)
		plt.show()

	def graph_show():
		x = np.arange(0, 5, 0.1)
		y = np.sin(x)
		ax = figure.add_subplot(111)
		ax.clear()
		ax.scatter(x, y)
		canvas.draw()

	def data_read():
		print("data_read()")
		for i in range(0, datum_num):
			x = np.arange(0, np_data[i].size-1, 1)
			y = np.array(data[i][1:])
			ax = figure.add_subplot(plot_val + i+1)
			ax.clear()
			ax.plot(y)
		canvas.draw()



		#x = np.arange(0, np_data[0].size-1, 1)
		#y = np.array(data[0][1:])
		#ax2 = figure.add_subplot(111)
		#ax2.clear()
		#ax2.plot(x, y)
		#canvas.draw()


	button_3.clicked.connect(graph_show)
	button_4.clicked.connect(data_read)

 
	# Add tabs
	tabs.addTab(tab2,"data_logs")
	tabs.addTab(tab1,"GPS_pos")
 
	# Set title and show
	tabs.setWindowTitle('Jesse is great')
	tabs.show()
 
	sys.exit(app.exec_())
 
 
if __name__ == '__main__':
	main()