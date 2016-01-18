import Game
class Board():

    def __init__(self,rows,column):
        super(Board, self).__init__()
        self.Row = int(rows)
        self.Column = int(column)
        self.horizontalEdges = self.builMatrixHorizontalEdges()
        self.verticalEdges = self.buildMatrixVerticalEdges()
        self.boxesMatrix = self.builMatrixBoxes()





    def builBoard(self):
        boardChain = [None]*self.Row
        for i in range(self.Row):
            boardChain[i] = [None]*(self.Column)
        for i in self.Row:
            for j in self.Column:
                if j%2 == 0:
                    boardChain[i][j]="*"
        return boardChain


    def updateEdge(self,type,edge):
        return "null"




    def getWinner(self):
        return "null"


    def builMatrixHorizontalEdges(self):
        horizontalEdges = [None]*self.Row
        for i in range(self.Row):
            horizontalEdges[i] = [None]*(self.Column-1)
        return horizontalEdges


    def buildMatrixVerticalEdges(self):
        verticalEdges = [None]*(self.Row-1)
        for j in range(self.Row):
            verticalEdges[j] = [None]*(self.Column)
        return verticalEdges

    def builMatrixBoxes(self):
        boxesMatrix = [None]*(self.Row-1)
        for i in range(self.Row-1):
            boxesMatrix[i] = [None]*(self.Column-1)
        return boxesMatrix

    """


    """
    def toStringBoard(self,Board):
        print ' ',
        for i in range(len(Board)):
            print i,
        print
        for i,element in enumerate(Board):
            print i, ' '.join(element)



