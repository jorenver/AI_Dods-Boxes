from PyQt5.QtWidgets import *
from GraphicEdge import *
from GraphicBox import *
from GraphicPoint import *
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

	def updateGraphicEdge(self,typeE,dod,owner):
		boxes=self.Board.getBoxesAffected(dod,typeE)
		if(typeE=="V"):
			print "Vertical x: ",dod.x," Y: ",dod.y," Owner: ",owner
			self.GraphicVerticalEdges[dod.x][dod.y].drawLinePc(owner)
		else:
			print "horizontal x: ",dod.x," Y: ",dod.y," Owner: ",owner
			self.GrapicHorizontalEdges[dod.x][dod.y].drawLinePc(owner)

	def updateGraphicBox(self,dod,owner):
		self.GraphicBoxesMatrix[dod.x][dod.y].updateBox(owner)
		self.GraphicBoxesMatrix[dod.x][dod.y].repaint()


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
						auxDod=Dod(i//2,j//2)
						gEdge=GraphicEdge("H",auxDod,self.observer,self)
						#gEdge=QPushButton("H",self.contendorBoard)
						gEdge.setMinimumHeight(30)
						gEdge.setMinimumWidth(60)
						gEdge.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 60
						auxHorizontal.append(gEdge)
				FILA = FILA + 30
				COLUMNA = 0
				self.GrapicHorizontalEdges.append(auxHorizontal)
			else:
				auxVertical=[]
				auxBoxes=[]
				for j in range(nColumnas):
					if j%2==0: #verticar Edge
						auxDod=Dod(i//2,j//2)
						gEdge=GraphicEdge("V",auxDod,self.observer,self)
						#gEdge=QPushButton("V",self.contendorBoard)
						gEdge.setMinimumHeight(60)
						gEdge.setMinimumWidth(30)
						gEdge.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 30
						auxVertical.append(gEdge)
					else: #box
						gBox=GraphicBox(self)
						#gBox=QPushButton("B",self.contendorBoard)
						gBox.setMinimumHeight(60)
						gBox.setMinimumWidth(60)
						gBox.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 60
						auxBoxes.append(gBox)
				FILA = FILA + 60
				COLUMNA = 0
				self.GraphicVerticalEdges.append(auxVertical)
				self.GraphicBoxesMatrix.append(auxBoxes)
		#print "horizontal: ",len(self.GrapicHorizontalEdges)
		#print "horizontal 0: ",len(self.GrapicHorizontalEdges[0])
		#print "Vertical: ",len(self.GraphicVerticalEdges)
		#print "Vertical 0: ",len(self.GraphicVerticalEdges[0])
		#print "boxes ",len(self.GraphicBoxesMatrix)
		#print "boxes 0 ",len(self.GraphicBoxesMatrix[0])
