import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject,Qt
from Dod import *
from PyQt5.QtGui import *
import networkx as nx
from GraphicNode import *

def getMin2(l):
	n=l[0]
	cont=0
	index=0
	for i in l:
		if(i.heuristicValue < n.heuristicValue):
			n=i
			index=cont
		cont=cont+1

	return n,l.pop(index)

def getMax2(l):
	n=l[0]
	cont=0
	index=0
	for i in l:
		if(i.heuristicValue > n.heuristicValue):
			n=i
			index=cont
		cont=cont+1
	return n,l.pop(index)

class GraphicTree(QMainWindow):

	def __init__(self,graph,root,rows,colums,*args):
		super(GraphicTree, self).__init__()
		self.setWindowTitle("Tree")
		self.dimX=1200
		self.dimY=700
		self.star=10
		self.radio=50
		self.resize(self.dimX,self.dimY)
		
		self.graph=graph
		self.rows=rows
		self.colums=colums
		self.root=root
		nodes=[]
		nodes.append(self.root) #agrego la raiz del arbol
		n=GraphicNode(self.root,self.rows,self.colums,self)
		n.move(self.dimX/2,self.star)
		cont=1
		axuType="max"
		while cont<3:
			hijos=self.graph.neighbors(self.root)
			numHijos=0
			nhijos=[]
			'''
			while len(hijos)!=0 and numHijos<4:
				if axuType=="max":
					auxHijo,hijos=getMax2(hijos)
					nhijos.append(auxHijo)
				else:
					auxHijo,hijos=getMin2(hijos)
					nhijos.append(auxHijo)
				numHijos=numHijos+1
			'''

			cont2=0
			for i in hijos:
				#dibjar a cada hijo
				n=GraphicNode(i,self.rows,self.colums,self)
				n.move(cont2*self.dimX/len(hijos),self.star+cont*100)
				if cont2==0:	
					self.root=i
				cont2=cont2+1
				
			if(axuType=="max"):
				axuType="min"
			else:
				axuType="max"
			nodes.pop()
			if(hijos[0]):
				nodes.append(hijos[0])
			cont=cont+1
			lenAnterior=len(hijos)



	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		pen = QPen(Qt.black, 2, Qt.SolidLine)
		qp.setBrush(QColor(200, 0, 0))
		
		
		nodes=[]
		nodes.append(self.root) #agrego la raiz del arbol
		cont=1
		while cont<3:
			hijos=self.graph.neighbors(self.root)
			cont2=0
			for i in hijos:
				#dibjar a cada hijo
				#qp.drawEllipse(cont2*self.dimX/len(hijos),self.star+cont*100,self.radio,self.radio)
				if(cont==1):#solo en la primera pasada se dibuja desde la raiz
					qp.drawLine(self.dimX/2+self.radio/2, self.star+self.radio, cont2*self.dimX/len(hijos)+self.radio/2, self.star+cont*100)
				else:#se conectan con el 1 nodo de el nivel anterior
					#si se desea cambiar el nodo al cual se conecta se debe cambiar el 0 por la posicion del nodo que se desea
					qp.drawLine(0*self.dimX/lenAnterior+self.radio/2, self.star+self.radio+(cont-1)*100, cont2*self.dimX/lenAnterior+self.radio/2, self.star+cont*100)
				cont2=cont2+1
			nodes.pop()
			if(hijos[0]):
				nodes.append(hijos[0])
			cont=cont+1
			lenAnterior=len(hijos)



		qp.end()

if __name__ == "__main__":
    appDotsandBoxes = QApplication(sys.argv)
    wSetting = GraphicTree()
    wSetting.show()
    sys.exit(appDotsandBoxes.exec_())