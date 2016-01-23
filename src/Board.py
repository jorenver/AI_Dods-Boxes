class Board():

    def __init__(self,rows,column):
        self.Row = int(rows)
        self.Column = int(column)
        self.horizontalEdges = self.builMatrixHorizontalEdges()
        self.verticalEdges = self.buildMatrixVerticalEdges()
        self.boxesMatrix = self.builMatrixBoxes()


        #1 representa a el Pc y 2 representa al Jugagdor
    def updateEdge(self,typeE,dod,player):
        if(typeE=="vertical"):
            self.verticalEdges[dod.x][dod.y]=player
        else:
            self.horizontalEdges[dod.x][dod.y]=player




    def getWinner(self):
        return None


    def builMatrixHorizontalEdges(self):
        horizontalEdges = []
        for i in range(self.Row+1):
            aux=[]
            for j in range(self.Column):
                aux.append(0)
            horizontalEdges.append(aux)
        return horizontalEdges


    def buildMatrixVerticalEdges(self):
        verticalEdges = []
        for i in range(self.Row):
            aux=[]
            for j in range(self.Column+1):
                aux.append(0)
            verticalEdges.append(aux)
        return verticalEdges

    def builMatrixBoxes(self):
        boxesMatrix = []
        for i in range(self.Row):
            aux=[]
            for j in range(self.Column):
                aux.append(0)
            boxesMatrix.append(aux)
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

