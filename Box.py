
class Box:
	def __init__(self, coordX, coordY, grade):
		self.coordX = coordX
		self.coordY = coordY
		self.grade = grade
		self.owner = None
		self.visited = 0

	def getEdge(self, direction):

		if(direction == 'T'): #TOP
			return (self.coordX, self.coordY, 'T')
		if(direction == 'B'): #BOTTOM
			return (self.coordX + 1, self.coordY, 'B')
		if(direction == 'L'): #LEFT
			return (self.coordX, self.coordY, 'L')
		if(direction == 'R'): #RIGHT
			return (self.coordX, self.coordY + 1, 'R')

	def __str__(self):
		return "Box {grade:" + str(self.grade) + " coordX: " + str(self.coordX) + " coordY: " + str(self.coordY) + "owner: " + str(self.owner) + "}"