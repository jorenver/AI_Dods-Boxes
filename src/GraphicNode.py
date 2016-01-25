import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject,Qt
from Dod import *
from PyQt5.QtGui import QPainter, QColor, QPen
from node import *

class Communicate(QObject):
    
	signal = pyqtSignal() 

class GraphicNode(QWidget):

	def __init__(self,node,*args):
		QWidget.__init__(self,*args)
		self.handled = Communicate()
		self.handled.signal.connect(self.openNodeContend)
		self.node=node
		self.setMinimumHeight(50)
		self.setMinimumWidth(50)
	
	def openNodeContend(self):
		print "me abriste"

	def mousePressEvent(self, event):
		self.openNodeContend()


	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		qp.setBrush(QColor(200, 0, 0))
		qp.drawEllipse(0,0,50,50)

if __name__ == "__main__":
    appDotsandBoxes = QApplication(sys.argv)
    wSetting = GraphicNode(None)
    wSetting.show()
    sys.exit(appDotsandBoxes.exec_())