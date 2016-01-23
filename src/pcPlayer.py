import networkx as nx
import node as n

from AI_Util import*

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

	def __init__(self, board, orderTurn):
		self.boardPlayer = board
		self.graph=nx.Graph()
		self.orderTurn = orderTurn


	def getListEdge (self,Graph):
		pass

	def changeType(self,x):
		if(x=="min"):
			return "max"
		else:
			return "min"


	def miniMax(self,node, depth, typeLevel):
		self.graph.add_node(node)
		
		ai_util = AI_Util(node.horizontalEdge, node.verticalEdge, node.boxes )


		if(depth==0):
			node.heuristicValue = ai_util.heuristic(self.orderTurn)
		else:

			owner = None
			if(typeLevel == "max"):
				owner = "PC"
			else:
				owner = "YOU"

			children= ai_util.getBoardChildren(owner)
			for i in children:
				self.graph.add_edge(node,i)
				auxTypeLevel=self.changeType(typeLevel)
				self.miniMax(i,depth-1, auxTypeLevel)
			if (typeLevel=="min"):
				node.heuristicValue = getMin(children).heuristicValue
			else:
				node.heuristicValue=getMax(children).heuristicValue

		print (node.heuristicValue," heuristic value: ", str(node.heuristicValue))


	def draw():
		x.draw(obj.graph)
		plt.show()


