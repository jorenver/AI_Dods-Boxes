import copy
import math
from AI_Board import *

def printBoard(board):
	print "Hoizontal:"
	print board[0]
	print "Vertical:"
	print board[1]
	print "____________"

def printBoard2(board):
	
	print "El padre"
	print "Hoizontal:"
	print board.horizontalEdge
	print "Vertical:"
	print board.verticalEdge
	print "____________"


if __name__ == "__main__":
	b = AI_Board(6,6)
	b.initBoard()
	Temp_children = b.getChildren()
	print "Nivel 1: numero de hijos", len(Temp_children)

	cont = 0
	print "Nivel 2, numero de hijos"
	children = []
	for c in Temp_children:
		child = AI_Board(6,6)
		child.horizontalEdge = c[0]
		child.verticalEdge = c[1]
		child.boxes = c[2]
		children.append(child)

	for c in children:
		Temp_children = c.getChildren()
		cont +=  len(Temp_children)
	print cont



