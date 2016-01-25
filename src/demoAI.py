import pcPlayer as pc
from node import*
from Box import *
from AI_Board import*

import networkx as nx
import matplotlib


"""
Board

	 0 1 2  
	*-*-* *
0	|     
	* * * *
1	|        
	* * * *
2	       
	*-*-*-*


"""


horizontalEdge = [ [1,1,0], 
				   [0,0,0], 
				   [0,0,0], 
				   [1,1,1] ]

verticalEdge = [ [1,0,0,0],
				 [1,0,0,0], 
				 [0,0,0,0] ]



boxes = [[Box(0,0, 2), Box(0,1, 1), Box(0,2, 0)], 
		 [Box(1,0, 1), Box(1,1, 0), Box(1,2, 0)],
		 [Box(2,0, 0), Box(2,1, 0), Box(2,2, 0)]]


sequenceEdge = []




if __name__ == "__main__":

	node = Node(horizontalEdge, verticalEdge, boxes, sequenceEdge )

	obj=pc.pcPlayer(None, 2,None,None)
	
	obj.miniMax(node, 2 , "max")
	print ("edges: ",obj.graph.number_of_edges())

	nx.draw(obj.graph)
	plt.show()

	'''
	for i in obj.graph.edges():
		print "( value: ", str(i[0].value), "heuristic: ", str(i[0].heuristicValue), " ) -->", "( value: ", str(i[1].value), "heuristic: ", str(i[1].heuristicValue), " )"

	print "resultado"
	for i in obj.graph.nodes():
		print i
	
	a= generateChildren(node)
	for i in a:
		for j in i.values:
			print j , 
	'''