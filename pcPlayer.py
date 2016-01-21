import networkx as nx
import node as n

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

	def __init__(self,board):
		self.boardPlayer = board
		self.graph=nx.Graph()


	def getListEdge (self,Graph):
		pass

	def changeType(self,x):
		if(x=="min"):
			return "max"
		else:
			return "min"


	def miniMax(self,node,depth,generateClindren,heuristic,typeLevel):
		self.graph.add_node(node)
		if(depth==0):
			node.heuristicValue=heuristic(node)
		else:
			children= generateClindren(node)
			for i in children:
				self.graph.add_edge(node,i)
				auxTypeLevel=self.changeType(typeLevel)
				self.miniMax(i,depth-1,generateClindren,heuristic,auxTypeLevel)
			if (typeLevel=="min"):
				node.heuristicValue=getMin(children).heuristicValue
			else:
				node.heuristicValue=getMax(children).heuristicValue
		print (node.value," heuristic value: ", str(node.heuristicValue))




