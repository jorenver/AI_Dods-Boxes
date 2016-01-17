import copy
import math
from Board import *



if __name__ == "__main__":
	b = Board(3,3)
	b.initBoard()
	children = b.getChildren()
	print len(children)