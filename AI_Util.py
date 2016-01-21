import copy
import math
from Box import *
from AI_Board import *

class AI_Util:
	def __init__(self, ai_board):
		self.ai_board = ai_board
		self.children = []
		
	def getBoardChildren(self, owner):

		board = self.ai_board
		sequenceEdge = []
		print ("*****DoMoves*****")
		generateChild = self.doMoves(owner, sequenceEdge)
		if(not(generateChild)):
			newVerticalEdge = copy.deepcopy(board.verticalEdge) # copy vertical edge
			newHorizontalEdge = copy.deepcopy(board.horizontalEdge)
			newBoxes = copy.deepcopy(board.boxes)
			newSequenceEdge = copy.deepcopy(sequenceEdge)
			
			child = (newHorizontalEdge, newVerticalEdge, newBoxes, newSequenceEdge)
			self.children.append(child)
			return self.children


		for i in range(0, board.rows + 1):
			for j in range(0, board.columns + 1):
				#child from complete vertical edges
				
				if(i>=0 and i < board.rows ): # valid coordinates for vertical edge 
					
					newVerticalEdge = copy.deepcopy(board.verticalEdge) # copy vertical edge
					newSequenceEdge = copy.deepcopy(sequenceEdge)

					if(newVerticalEdge[i][j]== 0):
						

						bandVertical = board.verify_symmetry(i,j, 'V')
						if(bandVertical):
							
							newVerticalEdge[i][j] = 1

							newHorizontalEdge = copy.deepcopy(board.horizontalEdge) # copy horizontal edge
							newBoxes = copy.deepcopy(board.boxes) # copy the boxes
							afectedBoxes = board.getBoxesCoordinatesByEdge(i,j, 'V')

							for b in afectedBoxes:
								x = b[0]
								y = b[1]
								newBoxes[x][y].grade += 1 #actualizar cajas

							#DoMoves ------ 
							#create a complete tuple
							edge = (i,j, 'V')
							newSequenceEdge.append(edge)
							child = (newHorizontalEdge, newVerticalEdge, newBoxes, newSequenceEdge)
							self.children.append(child)
							
							"""
							for a in range(0,board.rows):
								for b in range(0, board.columns):
									print newBoxes[a][b].owner
							"""

				#child from complete horizontal edges
				if(j >=0 and j < board.columns):
					newHorizontalEdge = copy.deepcopy(board.horizontalEdge) # copy horizontal edge
					newSequenceEdge = copy.deepcopy(sequenceEdge)

					if(newHorizontalEdge[i][j]== 0):	
						#revisar simetria
						

						bandHorizontal = board.verify_symmetry(i,j, 'H')

						if (bandHorizontal):
							#create a complete tuple
							newHorizontalEdge[i][j] = 1 #revisar si esta bien ahi

							newVerticalEdge = copy.deepcopy(board.verticalEdge) # copy vertical edge
							newBoxes = copy.deepcopy(board.boxes) # copy the boxes
							afectedBoxes = board.getBoxesCoordinatesByEdge(i,j, 'H')

							
							edge = (i,j, 'H')
							#self.DoMoves(owner, child, edge, children)

							for b in afectedBoxes:
								x = b[0]
								y = b[1]
								newBoxes[x][y].grade += 1


							edge = (i,j, 'H')
							newSequenceEdge.append(edge)
							child = (newHorizontalEdge, newVerticalEdge, newBoxes, newSequenceEdge)
							

							self.children.append(child)

							"""
							for a in range(0,board.rows):
								for b in range(0, board.columns):
									print newBoxes[a][b]
							"""

							
		return self.children

	def updateBoxes(self, edge, owner):
		board = self.ai_board
		orientation = None 

		coordBoxes = board.getBoxesCoordinatesByEdge(edge[0], edge[1], edge[2])

		for b in coordBoxes:
			x = b[0]
			y = b[1]
			box = board.boxes[x][y]
			box.grade+=1
			if(box.grade == 4):
				box.owner = owner

		if (edge[2] == 'V'):
			x = edge[0]
			y = edge[1]
			board.verticalEdge[x][y] = 1
		else:
			x = edge[0]
			y = edge[1]
			board.horizontalEdge[x][y] = 1

	def closeChain(self, chain, ini, fin, owner ):
		board = self.ai_board
		sequenceEdge = []
		print "inicio, fin" ,ini, fin

		for i in range (ini, fin ):
			box = chain[i]
			edges = board.GetEdgesbyBox(box)
			edge = edges[0]
			print edge
			self.updateBoxes(edge, owner)
			sequenceEdge.append(edge)

		return sequenceEdge



	def getParalelOrientationEdge(self, edge):
		orientation = edge[2]

		if(orientation == 'T'):
			return "B"
		if(orientation == 'B'):
			return "T"
		if(orientation == 'L'):
			return "R"
		if(orientation == 'R'):
			return "L"

	def convertOrientation(self, orientation):
		if(orientation == 'T' or orientation == 'B'):
			return 'H'
		if(orientation == 'L' or orientation == 'R'):
			return 'V'


	def completeChain(self, chain, index, owner, sequenceEdge):
		board = self.ai_board
		lengthChain = len(chain)

		print "chain"
		print "index: ", index
		for x in chain:
			print x

		if(lengthChain > 2):

			nextChainTam = lengthChain - index 
			if(nextChainTam > index ):
				#la segunda parte de la cadena es mas larga
				ini = index
				fin = lengthChain - 2
				aux = self.closeChain(chain, ini, fin, owner)

				iniDoublecross = chain[lengthChain - 3]
				lastEdges = board.GetDirEdgesbyBox(iniDoublecross)
				lastEdge = lastEdges[0]
				paralelOrientation = self.getParalelOrientationEdge(lastEdge)

				newEdge = iniDoublecross.getEdge(paralelOrientation)
				newOrientation = self.convertOrientation(paralelOrientation)
				edge = (newEdge[0], newEdge[1], newOrientation )
				sequenceEdge.append(edge)
				self.updateBoxes(edge, owner) #update the grade and the owner
				board.setEdge(edge) #set an edge

				ini = 0
				fin = index
				aux = self.closeChain(chain, ini, fin, owner)
			else:
				#la primera parte de la cadena es mas larga
				ini  = 0
				fin = index - 2
				seq1 = self.closeChain(chain, ini, fin, owner)
				print "estoy aqui"

				iniDoublecross = chain[index - 2]
				print "init doublecroos", iniDoublecross
				lastEdges = board.GetDirEdgesbyBox(iniDoublecross)
				lastEdge = lastEdges[0]
				

				finDoubleCross = chain[index-1]

				newEdge = finDoubleCross.getEdge(lastEdge[2])
				
				newOrientation = self.convertOrientation(lastEdge[2])

				edge = (newEdge[0], newEdge[1], newOrientation )
				seq1.append(edge)
				self.updateBoxes(edge, owner) #update the grade and the owner
				board.setEdge(edge) #set an edge

				ini = index
				fin = lengthChain
				seq2 = self.closeChain(chain, ini, fin, owner)
				seq = seq2 + seq1
				sequenceEdge += seq



	def doMoves(self, owner , sequenceEdge):
		
		board = self.ai_board
		rows = board.rows
		columns = board.columns


		newEdges = []
		generateChild  = True

		#find a box with grade = 3, C-Boxes
		for i in range(0, rows):
			for j in range (0, columns):
				box = board.boxes[i][j]
				#if a box is c-box and not visited
				if(box.grade == 3 and box.visited == 0 ):
					adjacentCBoxes = board.getAdjacentCBoxes(box)
					lengthAdj = len(adjacentCBoxes)
					boxTuple = (box, lengthAdj )
					nextBoxes = board.getNextBoxes(box)
					lengthNextBoxes = len(nextBoxes)
					
					if( lengthAdj == 0 and lengthNextBoxes == 0): # it is a single box
						edge = board.GetEdgesbyBox(box) #return the avalable edge

						self.updateBoxes(edge[0], owner) #update the grade and the owner
						board.setEdge(edge[0]) #set an edge
						box.visited = 1
						sequenceEdge.insert(0, edge) #insert at the beginning


					else: #other case
						

						if(lengthNextBoxes != 0):
							nextBox = nextBoxes[0]
							chain = []
							chain = board.findChain(nextBox.coordX, nextBox.coordY)
							chain.insert(0, box)
							index = 0
							print "box: ", box
							#complete other part of the chain
							if(lengthAdj!=0):
								adjcbox = adjacentCBoxes[0]
								print "****adyacent cbox:", adjcbox
								nextadjcboxes = board.getNextBoxes(adjcbox)
								nextadjcbox = nextadjcboxes[0]
								otherChain = board.findChain(nextadjcbox.coordX, nextadjcbox.coordY)
								otherChain.insert(0, adjcbox)
								chain = otherChain + chain
								index += len(otherChain)

							self.completeChain(chain, index, owner, sequenceEdge)

							if(len(chain)>2):
								generateChild = False
							else:
								generateChild = True

		return generateChild
