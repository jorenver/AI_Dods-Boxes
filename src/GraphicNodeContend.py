from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor,QPen
from GraphicBox import *
from GraphicPoint import *
from LineasPunteadas import *
from Lineas import *
from GraphicEdge import *
import sys

class GraphicNodeContend(QWidget):

	def __init__(self,rows,column,verticalEdges,horizontalEdges,boxmatriz,*args):
		super(GraphicNodeContend, self).__init__()
		self.Row = int(rows)
		self.Column = int(column)
		#self.move(50,100)
		#self.setMinimumHeight(300)
		#self.setMinimumWidth(300)
		self.horizontalEdges = horizontalEdges
		self.verticalEdges = verticalEdges
		self.matrizbox = boxmatriz
		self.GraphicVerticalEdges=[]
		self.GraphicBoxesMatrix=[]
		self.GrapicHorizontalEdges=[]
		self.builGraphBoard()

	def builGraphBoard(self):
		COLUMNA = 0
		FILA = 0
		nfilas = 2*self.Row+1
		nColumnas = 2*self.Column+1
		for i in range(nfilas):
			if i%2==0:
				auxHorizontal=[]
				for j in range(nColumnas):
					if j%2==0: #dot
						dot=GraphicPoint(self)
						dot.setMinimumHeight(30)
						dot.setMinimumWidth(30)
						dot.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 30
					else: #horizontal Edge
						if self.hayLineaHorizontal(i//2,j//2):
							gEdge=Lineas("H",self)
							gEdge.setMinimumHeight(30)
							gEdge.setMinimumWidth(60)
							gEdge.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 60
				FILA = FILA + 30
				COLUMNA = 0
			else:
				for j in range(nColumnas):
					if j%2==0: #verticar Edge
						if self.hayLineaVertical(i//2,j//2):
							gEdge=Lineas("V",self)
							#gEdge=QPushButton("V",self.contendorBoard)
							gEdge.setMinimumHeight(60)
							gEdge.setMinimumWidth(30)
							gEdge.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 30
					else: #box
						gBox=GraphicBox(self)
						#gBox=QPushButton("B",self.contendorBoard)
						gBox.setMinimumHeight(60)
						gBox.setMinimumWidth(60)
						gBox.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 60
				FILA = FILA + 60
				COLUMNA = 0

		
	def hayLineaHorizontal(self,filas,columnas):
		if self.horizontalEdges[filas][columnas] == 1:
			return True
		else:
			return False

	def hayLineaVertical(self,filas,columnas):
		if self.verticalEdges[filas][columnas] == 1:
			return True
		else:
			return False
	def hayCaja(self,filas,columnas):
		if self.matrizbox[filas][columnas] != None:
			return True
		else:
			return False


if __name__ == "__main__":

	"""
	@description : Estas funcione serviran de pruebfil
	"""

def builMatrixHorizontalEdges():
    horizontalEdges1 = [[0 for x in range(4)] for x in range(4)]
    return horizontalEdges1


def buildMatrixVerticalEdges():
    verticalEdges1 = [[0 for x in range(4)] for x in range(4)]
    return verticalEdges1

def builboxMatriz():
	boxmatriz = [[1 for x in range(5)] for x in range(5)]
	return boxmatriz


