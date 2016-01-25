from Box import *
from Dod import *
class Board():

    def __init__(self,rows,column,Game):
        self.Row = int(rows)
        self.Column = int(column)
        self.horizontalEdges = self.builMatrixHorizontalEdges()
        self.verticalEdges = self.buildMatrixVerticalEdges()
        self.boxesMatrix = self.builMatrixBoxes()
        self.observerGame=Game
        self.observerGraphicBoard=None
        self.flagTurn=False


        #1 representa a el Pc y 2 representa al Jugagdor
    def updateEdge(self,typeE,dod,owner,flag):
        boxes=self.getBoxesAffected(dod,typeE)
        if(typeE=="V"):
            self.verticalEdges[dod.x][dod.y]=1
        else:
            self.horizontalEdges[dod.x][dod.y]=1
        if(owner==1):
            self.observerGraphicBoard.updateGraphicEdge(typeE,dod,owner)
            
        for i in boxes:
            self.boxesMatrix[i.x][i.y].grade=self.boxesMatrix[i.x][i.y].grade+1
            if(self.boxesMatrix[i.x][i.y].grade==4):
                self.boxesMatrix[i.x][i.y].owner=owner
                self.observerGame.updateGraphicBox(i,owner)
                if(owner==2):
                    self.flagTurn=True
        self.toStringBoard()
        if(owner==2):
            self.observerGame.notifyPlay(self.isChangeTurn())
        else:# flag sirve para saber cuando la pc aun tiene jugada 
            self.observerGame.notifyPlay(flag)


    def validateBoxCoords(self, dod):
        if (dod.x >= 0 and dod.x< self.Row and dod.y>=0 and dod.y < self.Column ):
            return True
        else:
            return False

    def getBoxesAffected(self, dod, typeE):

        CoordsBoxes = []
        CoordsBoxes.append(dod)

        if(typeE == 'V'):
            CoordsBoxes.append( Dod(dod.x,dod.y-1))
        else:
            CoordsBoxes.append(Dod(dod.x-1,dod.y))

        #filter the no legal boxes
        temp = []
        for x in CoordsBoxes:
            if(self.validateBoxCoords(x)):
                temp.append(x)

        return temp


    def isChangeTurn(self):
        if(self.flagTurn):
            self.flagTurn=False
            return False
        return True

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
                aux.append(Box(i,j,0))
            boxesMatrix.append(aux)
        return boxesMatrix
        

    """
    """
    def toStringBoard(self):
        print "- horizontal\n"
        for i in self.horizontalEdges:
            aux=""
            for j in i:
                aux=aux+str(j)+","
            print aux,"\n"

        print "| Vertical\n"
        for i in self.verticalEdges:
            aux=""
            for j in i:
                aux=aux+str(j)
            print aux,"\n"

        print "| Boxes\n"
        for i in self.boxesMatrix:
            aux=""
            for j in i:
                aux=aux+str(j)
            print aux,"\n"

