import pcPlayer as pc
import matplotlib.pyplot as plt
import networkx as nx
class nodo:
	def __init__(self,v):
		self.heuristicValue=0
		self.value=v
	def __str__(self):
		return "(value: ",str(self.value)," heuristic: ", str(self.heuristicValue),")"


def generateChildren(a):
	aux=[2,3]
	result=[]
	for i in aux:
		n=nodo(0)
		n.value=a.value//i
		result.append(n)
	return result

def heuristic(a):
	return a.value



if __name__ == "__main__":
	obj=pc.pcPlayer(25)
	node=nodo(25)
	
	obj.miniMax(node,2,generateChildren,heuristic,"max")
	print ("edges: ",obj.graph.number_of_edges())
	print ("nodos: ",obj.graph.number_of_nodes())
	nx.draw(obj.graph)
	plt.show()
	'''
	pos=nx.graphviz_layout(obj.graph,prog='dot')
	nx.draw(bobj.graph,pos,with_labels=False,arrows=False)
	'''
	'''
	for i in obj.graph.edges():
		print "( value: ", str(i[0].value), "heuristic: ", str(i[0].heuristicValue), " ) -->", "( value: ", str(i[1].value), "heuristic: ", str(i[1].heuristicValue), " )"

	print "resultado"
	for i in obj.graph.nodes():
		print i
	
	a= generateChildren(node)
	for i in a:
		for j in i.values:
			print j , '\n'
	'''