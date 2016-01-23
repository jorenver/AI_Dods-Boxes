from PyQt5.QtWidgets import *
from GraphicEdge import *
from GraphicBox import *
class GraphicBoard(QWidget):

	def __init__(self,rows,column,Game,Board,*args):
		super(GraphicBoard, self).__init__(Game)
		self.Row = int(rows)
		self.Column = int(column)
		self.move(50,100)
		self.setMinimumHeight(800)
		self.setMinimumWidth(800)
		self.GrapicHorizontalEdges = []
		self.GraphicVerticalEdges = []
		self.GraphicBoxesMatrix = []
		self.Board=Board
		self.observer=Game

	def builGraphBoard(self):
		COLUMNA = 0
		FILA = 0
		nfilas = 2*self.Row+1
		nColumnas = 2*self.Column+1
		for i in range(nfilas):
			if i%2==0:
				for j in range(nColumnas):
					if j%2==0: #dot
						dot=QPushButton("D",self)
						dot.setMinimumHeight(30)
						dot.setMinimumWidth(30)
						dot.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 30 
						print "dot"
					else: #horizontal Edge
						auxDod=Dod(i//2,j//2)
						gEdge=GraphicEdge("horizontal",auxDod,self.observer,self)
						#gEdge=QPushButton("H",self.contendorBoard)
						gEdge.setMinimumHeight(30)
						gEdge.setMinimumWidth(60)
						gEdge.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 60 
						print "H"
				FILA = FILA + 30
				COLUMNA = 0
			else:
				for j in range(nColumnas):
					if j%2==0: #verticar Edge
						auxDod=Dod(i//2,j//2)
						gEdge=GraphicEdge("vertical",auxDod,self.observer,self)
						#gEdge=QPushButton("V",self.contendorBoard)
						gEdge.setMinimumHeight(60)
						gEdge.setMinimumWidth(30)
						gEdge.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 30
						print "V"
					else: #box
						gBox=GraphicBox(self)
						#gBox=QPushButton("B",self.contendorBoard)
						gBox.setMinimumHeight(60)
						gBox.setMinimumWidth(60)
						gBox.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 60
						print "Box"
				FILA = FILA + 60
				COLUMNA = 0