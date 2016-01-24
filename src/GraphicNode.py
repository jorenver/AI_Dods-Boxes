from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor,QPen
from GraphicBox import *
from GraphicPoint import *
from LineasPunteadas import *
from Lineas import *
import sys

class GraphicNode(QWidget):

	def __init__(self,rows,column,verticalEdges,horizontalEdges,boxmatriz,*args):
		super(GraphicNode,self).__init__()
		self.Row = int(rows)
		self.Column = int(column)
		self.move(50,100)
		self.setMinimumHeight(300)
		self.setMinimumWidth(300)
		self.horizontalEdges = horizontalEdges
		self.verticalEdges = verticalEdges
		self.matrizbox = boxmatriz
		self.builNodeTable()

	def builNodeTable(self):
		COLUMNA = 0
		FILA = 0
		fx = 0
		fy = 0
		fz = 0
		decrementadorh = 1
		decrementadorv = 0
		decrementadorb = 1
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
						type = "H"
						if self.hayLineaHorizontal(fx,posColumnaH):
							arcoh = Lineas(type,self)
							arcoh.setMinimumWidth(30)
							arcoh.setMinimumHeight(60)
							arcoh.move(COLUMNA,FILA)
						#else:
							#arcoh = LineasPunteadas(type,self)
							#arcoh.setMinimumWidth(30)
							#arcoh.setMinimumHeight(60)
							#arcoh.move(COLUMNA,FILA)
						decrementadorh = decrementadorh + 1
						COLUMNA = COLUMNA + 60
				FILA = FILA + 30
				decrementadorh = 1
				COLUMNA = 0
				fx= fx + 1
			else:
				for j in range(nColumnas):
					if j%2==0:
						posColumnaV= j - decrementadorv
						type = "V"
						if self.hayLineaVertical(fy,posColumnaV):
							arcoV = Lineas(type,self)
							arcoV.setMinimumHeight(60)
							arcoV.setMinimumWidth(30)
							arcoV.move(COLUMNA,FILA)
						#else:
							#arcoV = LineasPunteadas(type,self)
							#arcoV.setMinimumHeight(60)
							#arcoV.setMinimumWidth(30)
							#arcoV.move(COLUMNA,FILA)
						COLUMNA = COLUMNA + 30
						decrementadorv = decrementadorv + 1
					else:
						posColumnab = j - decrementadorb
						if self.hayCaja(fz,posColumnab):
							caja = GraphicBox(self)
							caja.setMinimumHeight(60)
							caja.setMinimumWidth(60)
							caja.move(COLUMNA,FILA)
							COLUMNA = COLUMNA + 60	
				FILA = FILA + 60
				COLUMNA = 0
				decrementadorv = 0
				fy = fy + 1
				fz = fz + 1

		
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
		if self.matrizbox[filas][columnas] == 1:
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

app = QApplication(sys.argv)
matrizhorizontal =  builMatrixHorizontalEdges()
matrizvertical = buildMatrixVerticalEdges()
box = builboxMatriz()
matrizvertical[0][0]=1
matrizvertical[0][1]=1
matrizvertical[0][2]=1
matrizhorizontal[0][0]=1
matrizhorizontal[1][0]=1
print matrizhorizontal
print matrizvertical[0]
print matrizhorizontal[1]
print matrizhorizontal[2]
print matrizhorizontal[0][0]
ventana = GraphicNode(3,3,matrizvertical,matrizhorizontal,box)
ventana.show()
sys.exit(app.exec_())
