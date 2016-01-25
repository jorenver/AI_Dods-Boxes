
import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject,Qt
from Dod import *
from PyQt5.QtGui import QPainter, QColor, QPen
class Communicate(QObject):
    
	signal = pyqtSignal() 


class GraphicEdge(QWidget):

	def __init__(self,typeEdge,dod,Game,*args):
		QWidget.__init__(self,*args)
		self.type = typeEdge
		self.observer=Game
		#self.board = board
		self.owner=None
		self.dod=dod
		layout = QVBoxLayout(self)
		self.setLayout(layout)
		self.handled = Communicate()
		self.handled.signal.connect(self.drawLine)


	def drawLine(self,owner):
		if(self.owner):
			print "ya Fue seleccionado, x:", self.dod.x, "y: ", self.dod.y
		else:
			self.owner=owner
			print "x: " , self.dod.x, "y: ", self.dod.y
			self.observer.Board.updateEdge(self.type,self.dod,owner,True)
			self.repaint()

	def drawLinePc(self,owner):
		if(self.owner):
			print "ya Fue seleccionado, x:", self.dod.x, "y: ", self.dod.y
		else:
			self.owner=owner
			print "x: " , self.dod.x, "y: ", self.dod.y
			self.repaint()

	def mousePressEvent(self, event):
		self.drawLine(2)

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawLinePaint(qp)
		qp.end()

	def drawLinePaint(self, qp):
		pen = QPen(Qt.black, 2, Qt.SolidLine)
		if(self.owner):
			qp.setPen(pen)
			if(self.type=="H"):
				qp.drawLine(0, 15, 60, 15)
			if(self.type=="V"):
				qp.drawLine(15, 0, 15, 60)

		


	def eraseLine(self):
		return None

'''

	def paintEvent(self, event):
		paint = QPainter(self)
		paint.begin(self)
		painter.setPen(QPen(Qt.darkGray,3))
		if(typeEdge=="vertical" and self.owner):
			painter.drawLine(QPoint(15,0),QPoint(15,80))
		elif(self.owner):
			painter.drawLine(QPoint(0,15),QPoint(80,15))
		paint.end()
		'''

