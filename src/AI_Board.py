import copy
import math
from Box import *
from node import*

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



class AI_Board:
	def __init__(self, horizontalEdge, verticalEdge, boxes):
		self.verticalEdge = verticalEdge
		self.horizontalEdge = horizontalEdge
		self.boxes = boxes
		self.rows = self.getRowsTam(boxes) #number of horizontal boxes
		self.columns = self.getColummnsTam(boxes) #number of vertical boxes
		self.children = []

	def getRowsTam(self, boxes):
		rows = len(boxes)
		return rows

	def getColummnsTam(self, boxes):
		aux = boxes[0]
		columns = len(aux)
		return columns

	def setUnvisited(self):
		for i in range(0, self.rows):
			for j in range(self.columns):
				self.boxes[i][j].visited = 0
	#****basic functions

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
		

		columns = self.columns + 1
		if(posY>= math.ceil(float(columns)/2) and posY<= columns ):
			value = not(self.verifySymmetry_Y(posX, posY,orientation))
			return value

		rows = self.rows;
		if(posX >= math.ceil(float(rows)/2) and posX<= rows):
			value = not(self.verifySymmetry_X(posX, posY, orientation))
			return value

		return True

		
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
			if( y >= 0 and y <= self.columns ):
				return True
			else:
				return False

	#validate the coordinate of a box
	def validateBoxCoords(self, x, y):
		if (x >= 0 and x< self.rows and y>=0 and y < self.columns ):
			return True
		else:
			return False

	#Return True is a box is available to form part of a chain
	def isBoxAvailable(self, box):

		value = True

		if(box.grade == 2 or box.grade == 3):
			#self.boxes[i][j].visited = 1
			value = True

		if(box.visited == 1):
			value = False

		return value

	def isBoxChainAvailable(self, box):

		value = True

		if(box.grade == 2):
			value = True

		if(box.visited == 1):
			value = False

		return value


	def GetEdgesbyBox(self, box):
		Edges = []
		print "box", box
		Edges.append(box.getEdge('T')) #horizontal
		Edges.append(box.getEdge('B')) #horizontal
		Edges.append(box.getEdge('L')) #vertical
		Edges.append(box.getEdge('R')) #vertical

		#filter the edges and find next boxes
		temp = []

		for e in Edges:
			if(self.validateEdgeCoods(e)):
				x = e[0]
				y = e[1]
				orientation = e[2] 
				if(orientation == 'L' or orientation == 'R'):
					
					if(self.verticalEdge[x][y] == 0):
						
						edge = (e[0], e[1], 'V')
						temp.append(edge)
				else:
					if(self.horizontalEdge[x][y] == 0):
						edge = (e[0], e[1], 'H')
						temp.append(edge)

		return temp

	
	def GetDirEdgesbyBox(self, box):
		Edges = []

		Edges.append(box.getEdge('T')) #horizontal
		Edges.append(box.getEdge('B')) #horizontal
		Edges.append(box.getEdge('L')) #vertical
		Edges.append(box.getEdge('R')) #vertical

		#filter the edges and find next boxes
		temp = []

		for e in Edges:
			if(self.validateEdgeCoods(e)):
				x = e[0]
				y = e[1]
				orientation = e[2] 
				if(orientation == 'L' or orientation == 'R'):
					if(self.verticalEdge[x][y] == 0):
						edge = (e[0], e[1], orientation)
						temp.append(edge)
				else:
					if(self.horizontalEdge[x][y] == 0):
						edge = (e[0], e[1], orientation)
						temp.append(edge)

		return temp



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


	def updateBoxes(self, edge, owner):
	
		orientation = None 

		coordBoxes = self.getBoxesCoordinatesByEdge(edge[0], edge[1], edge[2])

		for b in coordBoxes:
			x = b[0]
			y = b[1]
			box = self.boxes[x][y]
			box.grade+=1
			if(box.grade == 4):
				box.owner = owner

		if (edge[2] == 'V'):
			x = edge[0]
			y = edge[1]
			self.verticalEdge[x][y] = 1
		else:
			x = edge[0]
			y = edge[1]
			self.horizontalEdge[x][y] = 1


	def convertOrientation(self, orientation):
		if(orientation == 'T' or orientation == 'B'):
			return 'H'
		if(orientation == 'L' or orientation == 'R'):
			return 'V'



	def calculateScore(self):
		score = 0

		for i in range(0, self.rows):
			for j in range(0, self.columns):
				box = self.boxes[i][j]
				if(box.grade==4):
					score+=1

		return score








	#complex functions

	def getBoardChildren(self, owner):

		sequenceEdge = []
		#print ("*****DoMoves*****")
		generateChild = self.doMoves(owner, sequenceEdge)
		if(not(generateChild)):
			#print "No mas hijos"
			newVerticalEdge = copy.deepcopy(self.verticalEdge) # copy vertical edge
			newHorizontalEdge = copy.deepcopy(self.horizontalEdge)
			newBoxes = copy.deepcopy(self.boxes)
			newSequenceEdge = copy.deepcopy(sequenceEdge)
			
			child = Node(newHorizontalEdge, newVerticalEdge, newBoxes, newSequenceEdge)
			self.children.append(child)
			return self.children


		for i in range(0, self.rows + 1):
			for j in range(0, self.columns + 1):
				#child from complete vertical edges
				
				if(i>=0 and i < self.rows ): # valid coordinates for vertical edge 
					
					newVerticalEdge = copy.deepcopy(self.verticalEdge) # copy vertical edge
					newSequenceEdge = copy.deepcopy(sequenceEdge)

					if(newVerticalEdge[i][j]== 0):
						

						bandVertical = self.verify_symmetry(i,j, 'V')
						if(bandVertical):
							
							newVerticalEdge[i][j] = 1

							newHorizontalEdge = copy.deepcopy(self.horizontalEdge) # copy horizontal edge
							newBoxes = copy.deepcopy(self.boxes) # copy the boxes
							afectedBoxes = self.getBoxesCoordinatesByEdge(i,j, 'V')

							for b in afectedBoxes:
								x = b[0]
								y = b[1]
								newBoxes[x][y].grade += 1 #actualizar cajas

							#DoMoves ------ 
							#create a complete tuple
							edge = (i,j, 'V')
							newSequenceEdge.append(edge)
							child = Node(newHorizontalEdge, newVerticalEdge, newBoxes, newSequenceEdge)
							self.children.append(child)
							"""
							print "******HIJO**** vertical"
							print "Horizontal", newHorizontalEdge
							print "Vertical", newVerticalEdge
							
							for a in range(0,self.rows):
								for b in range(0, self.columns):
									print newBoxes[a][b]
							print "Sequence", newSequenceEdge
							"""

				#child from complete horizontal edges
				if(j >=0 and j < self.columns):
					newHorizontalEdge = copy.deepcopy(self.horizontalEdge) # copy horizontal edge
					newSequenceEdge = copy.deepcopy(sequenceEdge)

					if(newHorizontalEdge[i][j]== 0):	
						#revisar simetria
						

						bandHorizontal = self.verify_symmetry(i,j, 'H')

						if (bandHorizontal):
							#create a complete tuple
							newHorizontalEdge[i][j] = 1 #revisar si esta bien ahi

							newVerticalEdge = copy.deepcopy(self.verticalEdge) # copy vertical edge
							newBoxes = copy.deepcopy(self.boxes) # copy the boxes
							afectedBoxes = self.getBoxesCoordinatesByEdge(i,j, 'H')

							
							edge = (i,j, 'H')
							#self.DoMoves(owner, child, edge, children)

							for b in afectedBoxes:
								x = b[0]
								y = b[1]
								newBoxes[x][y].grade += 1


							edge = (i,j, 'H')
							newSequenceEdge.append(edge)
							child = Node(newHorizontalEdge, newVerticalEdge, newBoxes, newSequenceEdge)
							

							self.children.append(child)
							"""
							print "******HIJO**** horizonatl"
							print "Horizontal", newHorizontalEdge
							print "Vertical", newVerticalEdge
							for a in range(0,self.rows):
								for b in range(0, self.columns):
									print newBoxes[a][b]
							print "Sequence", newSequenceEdge
							""" 
							
		return self.children




	#close all the simple and double boxes
	def closeCBoxes(self, owner, sequenceEdge):

		for i in range(0, self.rows):
			for j in range (0, self.columns):
				box = self.boxes[i][j]

				if (box.grade == 3 and box.visited == 0 ):
					#get the next box
					nextBoxes = self.getNextBoxes(box)
					if(len(nextBoxes)!=0):
						nextBox = nextBoxes[0]
						if(nextBox.grade!=2):
							edge = self.GetEdgesbyBox(box) #return the avalable edge
							box.visited = 1
							self.updateBoxes(edge[0], owner) #update the grade and the owner
							sequenceEdge.append( edge) #add the edge to the sequence
					else:
						edge = self.GetEdgesbyBox(box) #return the avalable edge
						box.visited = 1
						self.updateBoxes(edge[0], owner) #update the grade and the owner
						sequenceEdge.append( edge) #add the edge to the sequence
	
	def findCBox(self):

		for i in range(0, self.rows):
			for j in range (0, self.columns):
				box = self.boxes[i][j]

				if (box.grade == 3 and box.visited == 0 ):
					return box

		return None

	def testBoxes(self, boxes):

		for b in boxes:
			x = b[0]
			y = b[1]
			box = self.boxes[x][y]
			if (box.grade>=2):
				return False

		return True


	def searchFreeEdge(self, owner):
		
		for i in range(0, self.rows + 1):
			for j in range(0, self.columns + 1):
				
				#search in the vertical edges
				if(i>=0 and i < self.rows ):

					if(self.verticalEdge[i][j]==0):
						afectedBoxes = self.getBoxesCoordinatesByEdge(i,j, 'V')
						if(self.testBoxes(afectedBoxes)):
							edge = (i,j,'V')
							return edge

				#search in horizontal edge
				if(j>=0 and j < self.columns ):

					if(self.horizontalEdge[i][j]==0):
						afectedBoxes = self.getBoxesCoordinatesByEdge(i,j, 'H')
						if(self.testBoxes(afectedBoxes)):
							edge = (i,j,'H')
							return edge

		return None


	def closeAllCBoxes(self, owner, sequenceEdge):

		for i in range(0, self.rows):
			for j in range (0, self.columns):
				box = self.boxes[i][j]

				if (box.grade == 3 and box.visited == 0 ):
					edge = self.GetEdgesbyBox(box) #return the avalable edge
					box.visited = 1
					self.updateBoxes(edge[0], owner) #update the grade and the owner
					sequenceEdge.append( edge ) #add the edge to the sequence

		box = self.findCBox()
		if(box != None):
			print "ENCONTRE OTRO CBOX"
			self.closeAllCBoxes(owner, sequenceEdge)


	def closeSequence(self, sequenceBoxes, owner ,sequenceEdge):

		seq = sequenceBoxes[1]
		
		for x in seq:
			print x

		for b in seq:
			edges = self.GetEdgesbyBox(b)
			if(len(edges)!=0):
				edge = edges[0]
				self.updateBoxes(edge, owner) #update the grade and the owner
				sequenceEdge.append(edge)


	def doDoubleCrossDealing(self, owner ,sequenceBoxes, sequenceEdge):

		cycle = sequenceBoxes[0]
		seq = sequenceBoxes[1]
		orientation = None

		totalScore = (self.rows)*(self.columns)
		realScore = self.calculateScore()

		tamSequence = len(seq)

		if(totalScore == realScore + tamSequence):
			self.closeSequence(sequenceBoxes, owner, sequenceEdge)
			return


		tamDealing = tamSequence
		if(cycle):
			tamDealing -=2
			#print "ciclo"

		for b in seq:
			if(tamDealing>0):
				
				
				edges = self.GetDirEdgesbyBox(b)
				edge = edges[0]

				if(len(edges)>1):
					for e in edges:
						if(e[2]!=oppOrientation):
							edge = e

				orientation = edge[2]

				if(orientation == 'T'):
					oppOrientation = 'B'
				if(orientation == 'B'):
					oppOrientation = 'T'
				if(orientation == 'L'):
					oppOrientation = 'R'
				if(orientation == 'R'):
					oppOrientation = 'L'
				
				#print "oritntacion", orientation, oppOrientation
				
				newOrientation = self.convertOrientation(edge[2])
				newEdge = (edge[0], edge[1], newOrientation)
				if(tamDealing!=2):
					#print "seteo edge", newEdge
					sequenceEdge.append(newEdge)
					self.updateBoxes(newEdge, owner) #update the grade and the owner
			

				
				tamDealing -= 1


	def searchSequence(self, xo, yo):

		sequence = []
		cycle = False

		box = self.boxes[xo][yo]

		if ( box.grade > 2 and box.visted==0 ):
			cycle = True
			box.visited = 1
			sequence.append(box)
			
		elif( box.grade > 1 and box.visited == 0):
			self.boxes[xo][yo].visited = 1
			sequence.append(box)
			#get next boxes
			nextBoxes = self.getNextBoxes(box)

			while(len(nextBoxes)!= 0):

				b = nextBoxes[0]
				if(b.grade>2):
					cycle = True

				self.boxes[b.coordX][b.coordY].visited = 1
				sequence.append(b)
				
				nextBoxes = self.getNextBoxes(b)


		return (cycle,sequence)

	#return a list of tuplas (cycle, seq)
	def searchALLSequenceBoxes(self, inibox):

		sequences = []


		if (inibox.visited == 0 ):
			x = inibox.coordX
			y = inibox.coordY

			nextBoxes = self.getNextBoxes(inibox)
			nextBox = nextBoxes[0]
			inibox.visited = 1
			sequence = self.searchSequence(nextBox.coordX, nextBox.coordY)
			seq = sequence[1]
			seq.insert(0, inibox)

		return sequence



	#close boxes in a chain or in a cycle but do doubleCross dealing
	def AnalizeSequenceBox(self , inibox ,owner,sequenceEdge):

		sequencesBoxes = []
		
		while(inibox!= None):
			seq = self.searchALLSequenceBoxes(inibox) #return a list of the chains or cycles
			#print "****buscando cadenas"
			sequencesBoxes.append(seq)
			inibox = self.findCBox()


		numberSequences = len(sequencesBoxes)

		if(numberSequences == 1):
			self.doDoubleCrossDealing(owner,sequencesBoxes[0], sequenceEdge)
			#print "***Fin doubleCrossDealing"
			#print self.ai_board.horizontalEdge		

		if(numberSequences > 1):

			for i in range(0, numberSequences -1 ):
				self.closeSequence(sequencesBoxes[i], owner, sequenceEdge)

			self.doDoubleCrossDealing(owner, sequencesBoxes[numberSequences -1], sequenceEdge)



	def doMoves(self, owner, sequenceEdge):

		generateChild = False

		#close the single c-boxes
		self.closeCBoxes(owner, sequenceEdge)
		box = self.findCBox()

		#it a c_box was found
		if(box!=None):
			edge = self.searchFreeEdge(owner)
			#if a free edge was found
			if(edge!=None):
				#close all the c-boxes
				print "Entro aqui"
				self.closeAllCBoxes(owner, sequenceEdge)
				self.updateBoxes(edge, owner)
				sequenceEdge.append(edge)
			else:
				self.AnalizeSequenceBox(box ,owner,sequenceEdge)

		else:
			generateChild = True

		print sequenceEdge

		self.setUnvisited()
		return generateChild

	#Try to find a chain from a coordiniate of a box (xo, yo)
	def findChain(self, xo, yo):
		
		stack =[]
		chain = []

		box = self.boxes[xo][yo]

		if ( self.isBoxChainAvailable(box) ):

			self.boxes[xo][yo].visited = 1
			chain.append(box)
			#get next boxes
			nextBoxes = self.getNextBoxes(box)

			while(len(nextBoxes)!= 0):
				if(len(nextBoxes) == 2 ):
					
					if(nextBoxes[1].grade != 2):
						return []

					stack.append(nextBoxes[1]) #push a box

				b = nextBoxes[0]
				
				if(nextBoxes[0].grade != 2):
					return []

				self.boxes[b.coordX][b.coordY].visited = 1

				chain.append(b) #append in the chain
				nextBoxes = self.getNextBoxes(b)

		for box in stack:
			chain.insert(0, box)
			self.boxes[box.coordX][box.coordY].visited = 1
			nextBoxes = self.getNextBoxes(box)

			while(len(nextBoxes)!= 0):
				if(len(nextBoxes) == 2 ):
					if(nextBoxes[1].grade != 2):
						return []
					stack.append(nextBoxes[1]) #push a box

				b = nextBoxes[0]
				
				if(nextBoxes[0].grade != 2):
					return []

				self.boxes[b.coordX][b.coordY].visited = 1

				chain.insert(0,b) #append in the chain
				nextBoxes = self.getNextBoxes(b)

		return chain



	def heuristic(self, orderTurn):

		parity = -1
		longChains = 0
		captureBox = 0
		C_boxes = 0

		self.setUnvisited()

		for i in range(0, self.rows):
			for j in range(self.columns):
				chain = self.findChain(i,j)
				
				if(len(chain)>2):
					longChains +=1

				box = self.boxes[i][j]

				if(box.grade == 3 ):
					C_boxes +=1
					box.visited = 1

				if(box.owner == "PC"):
					captureBox +=1


		dots = (self.rows + 1)*(self.columns + 1)

		if(dots%2 == 0):#if the number of dots is even
			if(orderTurn == 1 and (longChains%2 ==0 )):
				parity = 1

			if(orderTurn == 2 and (longChains%2 == 1)):
				parity = 1

		if(dots%2 == 1):
			if(orderTurn == 1 and (longChains%2 ==1 )):
				parity = 1

			if(orderTurn == 2 and (longChains%2 == 0)):
				parity = 1


		value = parity*longChains + captureBox - C_boxes

		#print parity, longChains, captureBox, C_boxes
		#print "El valor heurisitco", value
		return value







