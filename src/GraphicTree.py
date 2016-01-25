import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, QObject,Qt
from Dod import *
from PyQt5.QtGui import *
import networkx as nx
from GraphicNode import *

class GraphicTree(QWidget):

	def __init__(self,*args):
		super(GraphicTree, self).__init__()
		self.setWindowTitle("Tree")
		self.dimX=1200
		self.dimY=700
		self.star=10
		self.radio=50
		self.resize(self.dimX,self.dimY)
		self.graph=nx.Graph()
		self.graph.add_node(1)
		self.graph.add_node(2)
		self.graph.add_node(3)
		self.graph.add_node(4)
		self.graph.add_node(5)
		self.graph.add_node(6)
		self.graph.add_node(7)
		self.graph.add_node(8)
		self.graph.add_node(9)
		self.graph.add_node(10)
		self.graph.add_node(11)
		self.graph.add_node(12)
		self.graph.add_node(13)
		self.graph.add_node(14)
		self.graph.add_node(15)
		self.graph.add_node(16)
		self.graph.add_node(17)
		self.graph.add_node(18)
		self.graph.add_node(19)
		self.graph.add_node(20)

		self.graph.add_edge(1,2)
		self.graph.add_edge(1,3)
		self.graph.add_edge(1,4)
		self.graph.add_edge(1,5)
		self.graph.add_edge(2,6)
		self.graph.add_edge(2,7)
		self.graph.add_edge(2,8)
		self.graph.add_edge(2,9)
		self.graph.add_edge(2,10)
		self.graph.add_edge(6,11)
		self.graph.add_edge(6,12)
		self.graph.add_edge(6,13)
		self.graph.add_edge(6,14)
		self.graph.add_edge(6,15)
		self.graph.add_edge(11,16)
		self.graph.add_edge(11,17)
		self.graph.add_edge(11,18)
		self.graph.add_edge(11,19)
		self.graph.add_edge(11,20)
		nodes=[]
		nodes.append(1) #agrego la raiz del arbol
		n=GraphicNode(None,self)
		n.move(self.dimX/2,self.star)
		cont=1
		while cont<=5:
			hijos=self.graph.neighbors(1)
			cont2=0
			for i in hijos:
				#dibjar a cada hijo
				n=GraphicNode(None,self)
				n.move(cont2*self.dimX/len(hijos),self.star+cont*100)
				cont2=cont2+1
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
		nodes.append(1) #agrego la raiz del arbol
		n=GraphicNode(None,self)
		n.move(self.dimX/2,self.star)
		cont=1
		while cont<=5:
			hijos=self.graph.neighbors(1)
			cont2=0
			for i in hijos:
				#dibjar a cada hijo
				n=GraphicNode(None,self)
				n.move(cont2*self.dimX/len(hijos),self.star+cont*100)
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