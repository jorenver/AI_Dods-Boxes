import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject,Qt
from Dod import *
from PyQt5.QtGui import QPainter, QColor, QPen
class GraphicBox(QWidget):

	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.owner = None

	def updateBox(self,owner):
		self.owner=owner
		self.repaint()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		qp.setPen(QColor(255, 0, 0))
		#qp.setFont(QFont('Decorative', 10))
		if(self.owner==1):
			qp.drawText(e.rect(), Qt.AlignVCenter, "Computer")
		if(self.owner==2):
			qp.drawText(e.rect(), Qt.AlignVCenter, "   Player")
		qp.end()
