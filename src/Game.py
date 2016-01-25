# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from GraphicEdge import *
from GraphicBox import *
from Board import *
from GraphicBoard import *
from node import *
from pcPlayer import *
from Dod import *
import copy
class Game(QMainWindow):

    def __init__(self,nRows,nColumns,firstPlayer):
        # firstPlayer is 1 for pc and 2 for Human
        super(Game, self).__init__()
        #self.M=[[(0,0,"H")],[(0,0,"V")],[(1,0,"H")],[(0,1,"V")],[(1,1,"H")],[(1,2,"H")],[(2,1,"V")],[(2,2,"H")],[(2,3,"V")]]
        self.CONTADOR=0
        self.setWindowTitle("Dots And Boxes")
        self.resize(880,900)
        self.labelPlayer = QLabel(self)
        self.labelPlayer.setText("Box_PLayer: ")
        self.labelPlayer.move(50,50)
        self.labelPc = QLabel(self)
        self.labelPc.setText("Box_PC: ")
        self.labelPc.move(200,50)
        #self.buttonRestart = QPushButton("Restart",self)
        #self.buttonRestart.move(450,50)
        self.buttonShowTree = QPushButton("Show Tree",self)
        self.buttonShowTree.move(350,50)
        #self.labelTurn = QLabel(self)
        #self.labelTurn.setText("Turn: ")
        #self.labelTurn.move(350,50)
        self.labelScorePlayer = QLabel(self)
        self.labelScorePlayer.setText("0")
        self.labelScorePlayer.move(150,50)
        self.labelScorePc = QLabel(self)
        self.labelScorePc.setText("0")
        self.labelScorePc.move(280,50)
        #self.labelNumberTurn = QLabel(self)
        #self.labelNumberTurn.move(400,50)
        self.turn=firstPlayer
        self.Board=Board(nRows,nColumns,self)
        self.graphicBoard=GraphicBoard(nRows,nColumns,self,self.Board)
        self.graphicBoard.builGraphBoard()
        self.Board.observerGraphicBoard=self.graphicBoard
        self.pcPlayer=pcPlayer(self.Board, firstPlayer,self,self.graphicBoard)
        self.scorePlyer=0
        self.scorePc=0
        if(self.turn==1):
            self.pcPlayerTurn()
        print nRows,nColumns

    def changeTurn(self):
        if(self.turn==1):
            self.turn=2
            #self.labelNumberTurn.setText("Player")
        else:
            self.turn=1
            #self.labelNumberTurn.setText("Computadora")

    def notifyPlay(self,change):
        print "CAMBIO ",change
        if(change):
            self.changeTurn()
            if( self.turn==1):
                print "TURNO: ",self.turn
                self.pcPlayerTurn()

    def pcPlayerTurn(self):
        #movimientos=self.M[self.CONTADOR]
        #self.CONTADOR=self.CONTADOR+1
        node=Node(copy.deepcopy(self.Board.horizontalEdges),copy.deepcopy(self.Board.verticalEdges),copy.deepcopy(self.Board.boxesMatrix),[])
        self.pcPlayer.reset()
        self.pcPlayer.miniMax(node, 2 , "max")
        auxMovimientos=self.pcPlayer.graph.neighbors(node)
        if(len(auxMovimientos)>0):
            print "Valor escogido", getMin(self.pcPlayer.graph.neighbors(node)).heuristicValue
            movimientos=getMin(self.pcPlayer.graph.neighbors(node)).sequenceEdge


            print "TURNO DE LA PC"
            cont=0
            for i in movimientos:
                print "$$$$$$$$$$$$$$$$ ",i
                cont=cont+1
                if(cont<len(movimientos)):
                    self.Board.updateEdge(i[2],Dod(i[0],i[1]),1,False)
                else:
                    print "SI VOY A CAMBIAR DE TURNO"
                    self.Board.updateEdge(i[2],Dod(i[0],i[1]),1,True)
        else:
            print "LA COMPUTADORA COME AL FINAL"
            

    def updateGraphicBox(self,dod,owner):
        if(owner==1):
            self.scorePc=self.scorePc+1
            self.labelScorePc.setText(str(self.scorePc))
        else:
            self.scorePlyer=self.scorePlyer+1
            self.labelScorePlayer.setText(str(self.scorePlyer))
        self.graphicBoard.updateGraphicBox(dod,owner)

    """
    @description : This function return a int number
                    with QString,this function is useful
                    when you need show the result in the label
    """
    def putScorePlayer(self,valueInt):
        score = QtCore.QString()
        score.setNum(valueInt)
        return score

    """
    @description : This function return a int number
                    with QString,this function is useful
                    when you need show the result in the label
    """
    def putScorePc(self,valueInt):
        score = QtCore.QString()
        score.setNum(valueInt)
        return score

    """
    @description : This function return a int number
                    with QString,this function is useful
                    when you need show the result in the label
    """
    def putTurn(self,valueInt):
        score = QtCore.QString()
        score.setNum(valueInt)
        return score
    
                    
                
    
    def PasarMouse(self):
        return None
    
    def darClick(self):
        return None