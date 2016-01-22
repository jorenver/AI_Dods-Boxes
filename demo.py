import copy
import math
from AI_Board import *
from AI_Util import *


"""
Board

	 0 1 2  
	* *-* *
0	|     
	* *-*-*
1	  | | |  
	* * * *
2	  |   |
	*-*-*-*


"""


horizontalEdge = [ [0,1,0], 
				   [0,1,1], 
				   [0,0,0], 
				   [1,1,1] ]

verticalEdge = [ [1,0,0,0],
				 [0,1,1,1], 
				 [0,1,0,1] ]



boxes = [[Box(0,0, 1), Box(0,1, 2), Box(0,2, 1)], 
		 [Box(1,0, 1), Box(1,1, 3), Box(1,2, 3)],
		 [Box(2,0, 2), Box(2,1, 2), Box(2,2, 2)]]


def printBoard(board):
	print ("Hoizontal:")
	print (board[0])
	print ("Vertical:")
	print (board[1])

	print ("____________")

def printBoard2(board):
	
	print ("El padre")
	print ("Hoizontal:")
	print (board.horizontalEdge)
	print ("Vertical:")
	print (board.verticalEdge)
	print ("____________")


if __name__ == "__main__":
	b = AI_Board(3,3)

	b.verticalEdge = verticalEdge
	b.horizontalEdge = horizontalEdge
	b.boxes = boxes
	ai_util = AI_Util(b)
	Temp_children = ai_util.getBoardChildren("eloy")
	print ("Nivel 1: numero de hijos", len(Temp_children))

	children = Temp_children[0]

	print "Vertical edge", children[1]
	print "horizontal Edge", children[0]
	print "Secuencia", children[3]

	cajas = children[2]
	for x in range(0, len(cajas)):
		for y in range(0,len(cajas[x]) ):
			print cajas[x][y]

	""""
	for x in Temp_children:
		printBoard(x)
	"""

	"""
	cont = 0
	print "Nivel 2, numero de hijos"
	children = []
	for c in Temp_children:
		child = AI_Board(7,7)
		child.horizontalEdge = c[0]
		child.verticalEdge = c[1]
		child.boxes = c[2]
		children.append(child)

	for c in children:
		Temp_children = c.getChildren("eloy")
		cont +=  len(Temp_children)
	print cont
	""" 


