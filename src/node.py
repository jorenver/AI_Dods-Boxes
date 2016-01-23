class Node():
	def __init__(self, horizontalEdge, verticalEdge, boxes, sequenceEdge ):
		self.horizontalEdge = horizontalEdge
		self.verticalEdge = verticalEdge
		self.boxes = boxes
		self.sequenceEdge = sequenceEdge
		self.heuristicValue=0

	def __cmp__(self, other):
		return cmp(self.heuristicValue, other.heuristicValue)

	def __hash__(self):
		return 0

