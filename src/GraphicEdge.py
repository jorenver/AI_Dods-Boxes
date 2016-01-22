
import sys
from PyQt5.QtWidgets import *
class GraphicEdge(QWidget):

	def __init__(self,typeEdge,*args):
		QWidget.__init__(self,*args)
		self.type = typeEdge
		#self.board = board
		layout = QVBoxLayout(self)
		self.setLayout(layout)
		if(typeEdge=="vertical"):
			layout.addWidget(QLabel("|"))
		else:
			layout.addWidget(QLabel("--------"))



	def drawLine(self,owner):
		return None



	def eraseLine(self):
		return None

