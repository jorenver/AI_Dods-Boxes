import networkx as nx


class PcPlayer:
	def __init__(self, board):
		self.board=board
		self.graph=nx.Graph()
	
	def reset(self, board):
		self.board=board
		self.graph=nx.Graph()
	

	def minimax(self,node,generateChildren,level):
		if(level==0):


