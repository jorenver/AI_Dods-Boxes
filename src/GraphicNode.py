from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor,QPen
from GraphicBox import *
from GraphicPoint import *
from LineasPunteadas import *
from Lineas import *
import sys

class GraphicNode(QWidget):

	def __init__(self,rows,column,verticalEdges,horizontalEdges,*args):
		super(GraphicNode,self).__init__()
		self.Row = int(rows)
		self.Column = int(column)
		self.move(50,100)
		self.setMinimumHeight(300)
		self.setMinimumWidth(300)
		self.horizontalEdges = horizontalEdges
		self.verticalEdges = verticalEdges
		self.builNodeTable()

	def builNodeTable(self):
		COLUMNA = 0
		FILA = 0
		decrementadorh = 1
		decrementadorv = 0
		nfilas = 2*self.Row + 1
		nColumnas = 2*self.Column + 1
		print nfilas
		print nColumnas
		for i in range(nfilas):
			if i%2==0:
				for j in range(nColumnas):
					if j%2==0:
						dot = GraphicPoint(self)
						dot.setMinimumHeight(30)
						dot.setMinimumWidth(30)
						dot.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 30
					else:
						posColumnaH = j-decrementadorh
						print 'else 1'
						print posColumnaH
						print j
						print decrementadorh
						print i
						type = "H"
						if self.hayLineaHorizontal(i,posColumnaH):
							arcoh = Lineas(type,self)
							arcoh.setMinimumWidth(30)
							arcoh.setMinimumHeight(60)
							arcoh.move(COLUMNA,FILA)
						else:
							arcoh = LineasPunteadas(type,self)
							arcoh.setMinimumWidth(30)
							arcoh.setMinimumHeight(60)
							arcoh.move(COLUMNA,FILA)
						decrementadorh = decrementadorh + 1
						COLUMNA = COLUMNA + 60
				FILA = FILA + 30
				decrementadorh = 1
				COLUMNA = 0
			else:
				for j in range(nColumnas):
					if j%2==0:
						posColumnaV= j - decrementadorv
						print 'else 2'
						print posColumnaV
						print decrementadorv
						print j
						print i
						type = "V"
						if self.hayLineaVertical(i,posColumnaV):
							arcoV = Lineas(type,self)
							arcoV.setMinimumHeight(60)
							arcoV.setMinimumWidth(30)
							arcoV.move(COLUMNA,FILA)
						else:
							arcoV = LineasPunteadas(type,self)
							arcoV.setMinimumHeight(60)
							arcoV.setMinimumWidth(30)
							arcoV.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 30
						decrementadorv = decrementadorv + 1
					else:
						caja = GraphicBox(self)
						caja.setMinimumHeight(60)
						caja.setMinimumWidth(60)
						caja.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 60
					
				FILA = FILA + 60
				COLUMNA = 0
				decrementadorv = 0

		
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

if __name__ == "__main__":

	"""
	@description : Estas funcione serviran de pruebfil
	"""

def builMatrixHorizontalEdges():
    horizontalEdges1 = [[0 for x in range(7)] for x in range(7)]
    return horizontalEdges1


def buildMatrixVerticalEdges():
    verticalEdges1 = [[0 for x in range(7)] for x in range(7)]
    return verticalEdges1

app = QApplication(sys.argv)
matrizhorizontal =  builMatrixHorizontalEdges()
matrizvertical = buildMatrixVerticalEdges()
matrizvertical[0][0]=1
matrizvertical[0][1]=1
matrizvertical[0][2]=1
matrizhorizontal[0][0]=1
matrizhorizontal[1][1]=1
matrizhorizontal[2][2]=1
print matrizhorizontal
print matrizvertical[0]
print matrizhorizontal[1]
print matrizhorizontal[2]
print matrizhorizontal[0][0]
ventana = GraphicNode("3","3",matrizvertical,matrizhorizontal)
ventana.show()
sys.exit(app.exec_())
