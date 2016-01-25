import networkx as nx
import node as n

from AI_Board import*

def getMin(l):
	n=l[0]
	for i in l:
		if(i.heuristicValue < n.heuristicValue):
			n=i
	return n

def getMax(l):
	n=l[0]
	for i in l:
		if(i.heuristicValue > n.heuristicValue):
			n=i
	return n	

class pcPlayer():

	def __init__(self, board, orderTurn,game,GraphicBoard):
		self.boardPlayer = board
		self.graph=nx.Graph()
		self.orderTurn = orderTurn
		self.observerGame=game
		self.observerGraphicBoard=GraphicBoard
		self.root=None

	def reset(self):
		self.graph=nx.Graph()

	def getListEdge (self):
		pass

	def changeType(self,x):
		if(x=="min"):
			return "max"
		else:
			return "min"


	def miniMax(self,node, depth, typeLevel):
		self.graph.add_node(node)
		
		ai_board = AI_Board(node.horizontalEdge, node.verticalEdge, node.boxes )


		if(depth==0):
			node.heuristicValue = ai_board.heuristic(self.orderTurn)
		else:

			owner = None
			if(typeLevel == "max"):
				owner = "PC"
			else:
				owner = "YOU"

			children= ai_board.getBoardChildren(owner)
			if(len(children)==0):
				node.heuristicValue = ai_board.heuristic(self.orderTurn)
			else:
				print "########################## ",len(children)
				for i in children:
					self.graph.add_edge(node,i)
					auxTypeLevel=self.changeType(typeLevel)
					self.miniMax(i,depth-1, auxTypeLevel)
				if (typeLevel=="min"):
					node.heuristicValue = getMin(children).heuristicValue
				else:
					node.heuristicValue=getMax(children).heuristicValue


	def draw():
		x.draw(self.graph)
		plt.show()


