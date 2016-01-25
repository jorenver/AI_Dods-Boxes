import copy
import math
from AI_Board import *



"""
Board

	 0 1 2  
	*-*-*-*
0	| | | |
	*-*-*-*
1	| | | |
	*-*-*-*
2	| | | |
	*-*-*-*


"""


horizontalEdge = [ [1,1,1], 
				   [1,1,1], 
				   [1,1,1], 
				   [1,1,1] ]

verticalEdge = [ [1,1,1,1],
				 [1,1,1,1], 
				 [1,1,1,1] ]



boxes = [[Box(0,0, 4), Box(0,1, 4), Box(0,2, 4)], 
		 [Box(1,0, 4), Box(1,1, 4), Box(1,2, 4)],
		 [Box(2,0, 4), Box(2,1, 4), Box(2,2, 4)]]


sequenceEdge = []



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
	
	board = AI_Board(horizontalEdge, verticalEdge, boxes)

	children = board.getBoardChildren("PC")

	print "chlidrens", len(children)


