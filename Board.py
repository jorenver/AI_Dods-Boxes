import copy
import math
from Box import *

"""
Board

	 0 1 2  
	* * * *
0	       
	* * * *
1	         
	* * * *
2	        
	* * * *


"""

class Board:
	def __init__(self, rows, columns):
		self.verticalEdge = []
		self.horizontalEdge = []
		self.rows = rows #number of horizontal boxes
		self.columns = columns #number of vertical boxes
		self.boxes = []

	def createVerticalEdges(self):
		for i in range(0,self.rows):
			self.verticalEdge.append([0]*(self.columns+ 1))

		print self.verticalEdge

	def createHorizontalEdges(self):
		for i in range(0,self.rows + 1):
			self.horizontalEdge.append([0]*self.columns)	

		print self.horizontalEdge

	def createBoxes(self):

		for i in range(0, self.rows):
			boxes = []
			for j in range (0, self.columns):
				box = Box(i,j,0)
				boxes.append(box)
			self.boxes.append(boxes)

		for i in range(0, self.rows):
			for i in range(0, self.columns):
				print self.boxes[i][j]



	def initBoard(self):
		self.createHorizontalEdges()
		self.createVerticalEdges()
		self.createBoxes()

	#set 0 in the visited flag of a box
	def setUnvisited(self):
		for i in range(0, self.rows):
			for j in range(self.columns):
				self.boxes[i,j] = 0

	#validate the coordinates of an edge,
	#the edge is a tuple (x,y, orientation)
	# orintation = T, B, L, R
	def validateEdgeCoods(self, edge):
		x = edge[0]
		y = edge[1]
		orientation = edge[2]

		if (orientation == 'T' or orientation == 'B'): #Horizontal
			if ( x >= 0 and x < self.rows ):
				return True
			else:
				return False

		if(orientation == 'L' or orientation == 'R'): #Vertical
			if( y >= 0 and y < self.columns ):
				return True
			else:
				return False

	#validate the coordinate of a box
	def validateBoxCoords(self, x, y):
		if (x >= 0 and x< self.rows and y>=0 and y < self.columns ):
			return True
		else:
			return False


	#get the adjacence boxes of a box 
	def getNextBoxes(self, box):
		Edges = []

		Edges.append(box.getEdge('T')) #horizontal
		Edges.append(box.getEdge('B')) #horizontal
		Edges.append(box.getEdge('L')) #vertical
		Edges.append(box.getEdge('R')) #vertical

		#filter the edges and find next boxes
		nextBoxes = []

		for e in Edges:
			if(self.validateEdgeCoods(e)):
				orientation = e[2]
				x = None
				y = None
				if(orientation == 'T'):
					x = box.coordX - 1
					y = box.coordY
				if(orientation == 'B'):
					x = box.coordX + 1
					y = box.coordY
				if(orientation == 'L'):
					x = box.coordX
					y = box.coordY -1
				if(orientation == 'R'):
					x = box.coordX
					y = box.coordY + 1

				if(self.validateBoxCoords(x,y)):
					if(orientation == 'T' or orientation == 'B'):
						value = self.horizontalEdge[e[0]][e[1]]
						if (value == 0):
							nextBoxes.append(self.boxes[x][y])

					if(orientation == 'L' or orientation == 'R'):
						value = self.verticalEdge[e[0]][e[1]]
						if (value == 0):
							nextBoxes.append(self.boxes[x][y])

		#filter next boxes
		temp = []
		for b in nextBoxes:
			if(self.isBoxAvailable(b)):
				temp.append(b)

		nextBoxes = temp

		return nextBoxes


	#Return True is a box is available to form part of a chain
	def isBoxAvailable(self, box):

		value = True

		if(box.grade == 0 or box.grade == 1 or box.grade == 3):
			self.boxes[i][j].visited = 1
			value = False

		if (box.owner != None ):
			self.boxes[i][j].visited = 1
			value = False

		if(box.visited == 1):
			value = False

		return value


	#Try to find a chain from a coordiniate of a box (xo, yo)
	def findChain(self, xo, yo):
		
		stack =[]
		chain = []
		box = self.boxes[xo][yo]

		if ( self.isBoxAvailable(box) ):

			self.boxes[xo][yo].visited = 1
			chain.append(box)
			#get next boxes
			nextBoxes = self.getNextBoxes(box)

			while(len(nextBoxes)!= 0):
				if(len(nextBoxes) == 2 ):
					stack.append(nextBoxes[1]) #push a box

				b = nextBoxes[0]
				self.boxes[b.coordX][b.coordY].visited = 1

				chain.append(b) #append in the chain
				nextBoxes = self.getNextBoxes(b)

		for box in stack:
			chain.insert(0, box)
			self.boxes[box.coordX][box.coordY].visited = 1
			nextBoxes = self.getNextBoxes(box)

			while(len(nextBoxes)!= 0):
				if(len(nextBoxes) == 2 ):
					stack.append(nextBoxes[1]) #push a box

				b = nextBoxes[0]
				self.boxes[b.coordX][b.coordY].visited = 1

				chain.insert(0,b) #append in the chain
				nextBoxes = self.getNextBoxes(b)

		return chain

	#this method recieve the coordinates and the orientation of an edge and 
	# return a list of the coordinates (tuplas) of the adjacents boxes
	def getBoxesCoordinatesByEdge(self, posX, posY, orientation):

		CoordsBoxes = []
		CoordsBoxes.append( (posX, posY) ) 

		if(orientation == 'V'):
			CoordsBoxes.append((posX , posY - 1 ))
		else:
			CoordsBoxes.append((posX -1 , posY))

		#filter the no legal boxes
		temp = []
		for x in CoordsBoxes:
			if(self.validateBoxCoords(x[0], x[1])):
				temp.append(x)

		return temp


	#this function recive the coordinates an the orientation of and edge and
	#return true if its symmetric edge in the Y axis exits
	def verifySymmetry_Y(self, posX, posY, orientation):

		value = True
		s_posY = 0
		s_posX = 0
		Edges = []

		if(orientation == 'V'):

			#calculate the coordinates of the symetric edge (symmetry with vertical axis)
			s_posY = self.columns - posY
			s_posX = posX
			Edges = self.verticalEdge
		else:
			#calculate the coordinates of the symetric edge (symmetry with vertical axis)
			s_posY = self.columns - posY -1
			s_posX = posX
			Edges = self.horizontalEdge

		s_BoxesCoords = self.getBoxesCoordinatesByEdge(s_posX, s_posY, orientation)
		BoxesCoords = self.getBoxesCoordinatesByEdge(posX, posY, orientation)

		s_BoxGrades = []
		BoxGrades = []

		for b in s_BoxesCoords:
			x = b[0]
			y = b[1]
			
			if (Edges[s_posX][s_posY] == 1):
				s_BoxGrades.append(self.boxes[x][y].grade ) #get the grades of the boxes
			else:
				s_BoxGrades.append(self.boxes[x][y].grade + 1) #get the grades of the boxes
			


		for b in BoxesCoords:
			x = b[0]
			y = b[1]
			BoxGrades.append(self.boxes[x][y].grade + 1) #get the grades of the boxes

		
		s_BoxGrades = s_BoxGrades[::-1] #reverse the list

		
		for i in range(0, len(s_BoxGrades)):
			if(s_BoxGrades[i] != BoxGrades[i]):
				value = False

		return value

	#this function recive the coordinates an the orientation of and edge and
	#return true if its symmetric edge in the X axis exits
	def verifySymmetry_X(self, posX, posY, orientation):

		value = True
		s_posY = 0
		s_posX = 0
		Edges = []

		if(orientation == 'V'):

			#calculate the coordinates of the symetric edge (symmetry with horizontal axis)
			s_posY = posY
			s_posX = self.rows - posX -1
			Edges = self.verticalEdge
		else:
			#calculate the coordinates of the symetric edge (symmetry with horizontal axis)
			s_posY = posY
			s_posX = self.rows - posX
			Edges = self.horizontalEdge

		s_BoxesCoords = self.getBoxesCoordinatesByEdge(s_posX, s_posY, orientation)
		BoxesCoords = self.getBoxesCoordinatesByEdge(posX, posY, orientation)

		s_BoxGrades = []
		BoxGrades = []

		for b in s_BoxesCoords:
			x = b[0]
			y = b[1]
			if (Edges[s_posX][s_posY]==0):
				s_BoxGrades.append(self.boxes[x][y].grade + 1) #get the grades of the boxes
			else:
				s_BoxGrades.append(self.boxes[x][y].grade) #get the grades of the boxes

		for b in BoxesCoords:
			x = b[0]
			y = b[1]
			BoxGrades.append(self.boxes[x][y].grade + 1) #get the grades of the boxes

		s_BoxGrades = s_BoxGrades[::-1] #reverse the list

		
		for i in range(0, len(s_BoxGrades)):
			if(s_BoxGrades[i] != BoxGrades[i]):
				value = False

		return value



	def verify_symmetry(self, posX, posY, orientation):
		#revisar simetria

		
		if(orientation == 'H'):
			
			if(posX == 0 and posY == 0):
				return False


		columns = self.columns + 1
		if(posY>= math.ceil(float(columns)/2) and posY<= columns ):
			value = not(self.verifySymmetry_Y(posX, posY,orientation))
			return value

		rows = self.rows;
		if(posX >= math.ceil(float(rows)/2) and posX<= rows):
			value = not(self.verifySymmetry_X(posX, posY, orientation))
			return value

		return True



	def getChildren(self):
		children = []
		
		bandHorizontal = True

		for i in range(0, self.rows + 1):
			for j in range(0, self.columns + 1):
				#child from complete vertical edges
				
				if(i>=0 and i < self.rows ): # valid coordinates for vertical edge 
					
					newVerticalEdge = copy.deepcopy(self.verticalEdge) # copy vertical edge
					
					if(newVerticalEdge[i][j]== 0):
						

						bandVertical = self.verify_symmetry(i,j, 'V')
						if(bandVertical):
							
							newVerticalEdge[i][j] = 1

							newHorizontalEdge = copy.deepcopy(self.horizontalEdge) # copy horizontal edge
							newBoxes = copy.deepcopy(self.boxes) # copy the boxes
							afectedBoxes = self.getBoxesCoordinatesByEdge(i,j, "V")

							for b in afectedBoxes:
								x = b[0]
								y = b[1]
								newBoxes[x][y].grade += 1

							#DoMoves ------ 
							#create a complete tuple
							child = (newHorizontalEdge, newVerticalEdge, newBoxes)
							children.append(child)
							
							"""
							for a in range(0,self.rows):
								for b in range(0, self.columns):
									print newBoxes[a][b]
							"""


				#child from complete horizontal edges
				if(j >=0 and j < self.columns):
					newHorizontalEdge = copy.deepcopy(self.horizontalEdge) # copy horizontal edge
					

					if(newHorizontalEdge[i][j]== 0):	
						#revisar simetria
						bandHorizontal = self.verify_symmetry(i,j, 'H')

						if (bandHorizontal):
							#create a complete tuple
							newHorizontalEdge[i][j] = 1

							newVerticalEdge = copy.deepcopy(self.verticalEdge) # copy vertical edge
							newBoxes = copy.deepcopy(self.boxes) # copy the boxes
							afectedBoxes = self.getBoxesCoordinatesByEdge(i,j, 'H')

							for b in afectedBoxes:
								x = b[0]
								y = b[1]
								newBoxes[x][y].grade += 1


							#DoMoves ------ 

							child = (newHorizontalEdge, newVerticalEdge, newBoxes)
							children.append(child)

							"""
							for a in range(0,self.rows):
								for b in range(0, self.columns):
									print newBoxes[a][b]
							"""
		return children


