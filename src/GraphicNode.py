import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject,Qt
from Dod import *
from PyQt5.QtGui import QPainter, QColor, QPen
from node import *
from GraphicNodeContend import *
from Box import *
class Communicate(QObject):
    
	signal = pyqtSignal() 

class GraphicNode(QWidget):

	def __init__(self,node,rows,columns,*args):
		QWidget.__init__(self,*args)
		self.handled = Communicate()
		self.handled.signal.connect(self.openNodeContend)
		self.node=node
		self.setMinimumHeight(50)
		self.setMinimumWidth(50)
		self.rows=rows
		self.columns=columns
	
	def openNodeContend(self):
		print "me abriste"
		horizontalEdge = [ [1,1,0], 
						   [0,0,0], 
						   [0,0,0], 
						   [1,1,1] ]
		verticalEdge = [ [1,0,0,0],
						 [1,0,0,0], 
						 [0,0,0,0] ]
		boxes = [[Box(0,0, 2), Box(0,1, 1), Box(0,2, 0)], 
				 [Box(1,0, 1), Box(1,1, 0), Box(1,2, 0)],
				 [Box(2,0, 0), Box(2,1, 0), Box(2,2, 0)]]
		self.w = GraphicNodeContend(self.rows,self.columns,self.node.verticalEdge,self.node.horizontalEdge,self.node.boxes)
		self.w.show()
		print "se abrio"

	def mousePressEvent(self, event):
		self.openNodeContend()


	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		qp.setBrush(QColor(200, 0, 0))
		qp.drawEllipse(0,0,50,50)
		qp.setPen(QColor(0, 0, 0))
		qp.drawText(e.rect(), Qt.AlignVCenter,str(self.node.heuristicValue))

if __name__ == "__main__":
    appDotsandBoxes = QApplication(sys.argv)
    wSetting = GraphicNode(None)
    wSetting.show()
    sys.exit(appDotsandBoxes.exec_())