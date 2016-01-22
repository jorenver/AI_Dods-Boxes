class node():
	def __init__(self,AIBoard):
		self.horizontalEdges = AIBoard.horizontalEdge
		self.verticalEdges = AIBoard.verticalEdge
		self.boxesMatrix = AIBoard.boxes
		self.heuristicValue=0

	def __cmp__(self, other):
		return cmp(self.heuristicValue, other.heuristicValue)

