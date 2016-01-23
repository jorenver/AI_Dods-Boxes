
import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject
from Dod import *
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
		self.handled.signal.connect(self.drawLinePlayer)
		if(typeEdge=="vertical"):
			layout.addWidget(QLabel("|"))
		else:
			layout.addWidget(QLabel("-----"))

	def drawLinePlayer(self):
		self.owner="player"
		print "x: " , self.dod.x, "y: ", self.dod.y
		#self.repaint()

	def drawLine(self,owner):
		self.owner=owner
		#self.repaint()
	def mousePressEvent(self, event):
		if(self.owner):
			print "ya Fue seleccionado, x:", self.dod.x, "y: ", self.dod.y
		else:
			self.owner="player"
			print "x: " , self.dod.x, "y: ", self.dod.y
			self.observer.Board.updateEdge(self.type,self.dod,2)



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

