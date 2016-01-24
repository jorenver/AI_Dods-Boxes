import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import QObject,Qt
from PyQt5.QtGui import QPainter,QPen

class LineasPunteadas(QWidget):
	def __init__(self,type,*args):
		QWidget.__init__(self,*args)
		self.tipo = type

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.PaintDashLine(qp)
		qp.end()


	def PaintDashLine(self,qp):
		if self.tipo == "H":
			penhorizontal = QPen(Qt.black,2,Qt.DashLine)
			qp.setPen(penhorizontal)
			qp.drawLine(0,15,60,15)
		else:
			penvertical = QPen(Qt.black,2,Qt.DashLine)
			qp.setPen(penvertical)
			qp.drawLine(15,0,15,60)