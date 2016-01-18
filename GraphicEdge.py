
from PyQt4 import QtGui
class GraphicEdge():

    def __init__(self,typeEdge,board,edge):
        super(GraphicEdge, self).__init__()
        self.type = typeEdge
        self.Edge = edge
        self.tablero = board




    def drawLine(self,owner):
        return "null"



    def eraseLine(self):
        return "null"

