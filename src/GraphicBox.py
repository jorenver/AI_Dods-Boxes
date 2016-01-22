import sys
from PyQt5.QtWidgets import *
class GraphicBox(QWidget):

	def __init__(self,*args):
		QWidget.__init__(self,*args)
		self.owner = None
		#self.board = board
		layout = QVBoxLayout(self)
		self.setLayout(layout)
		layout.addWidget(QLabel("PC"))

	def drawLine(self,owner):
		return None



	def eraseLine(self):
		return None
