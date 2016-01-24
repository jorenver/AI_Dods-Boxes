
import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject,Qt
from Dod import *
from PyQt5.QtGui import QPainter, QColor, QPen

class GraphicPoint(QWidget):

	def __init__(self,*args):
		QWidget.__init__(self,*args)

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		qp.setBrush(QColor(200, 0, 0))
		qp.drawEllipse(8,8,15,15) 
		qp.end()
		