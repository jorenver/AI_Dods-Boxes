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

class Game(QMainWindow):

    def __init__(self,nRows,nColumns,firstPlayer):
        # firstPlayer is 1 for pc and 2 for Human
        super(Game, self).__init__()
        self.setWindowTitle("Dots And Boxes")
        self.resize(880,900)
        self.labelPlayer = QLabel(self)
        self.labelPlayer.setText("Box_PLayer: ")
        self.labelPlayer.move(50,50)
        self.labelPc = QLabel(self)
        self.labelPc.setText("Box_PC: ")
        self.labelPc.move(200,50)
        self.buttonRestart = QPushButton("Restart",self)
        self.buttonRestart.move(450,50)
        self.buttonShowTree = QPushButton("Show Tree",self)
        self.buttonShowTree.move(550,50)
        self.labelTurn = QLabel(self)
        self.labelTurn.setText("Turn: ")
        self.labelTurn.move(350,50)
        self.labelScorePlayer = QLabel(self)
        self.labelScorePlayer.setText("0")
        self.labelScorePlayer.move(150,50)
        self.labelScorePc = QLabel(self)
        self.labelScorePc.setText("0")
        self.labelScorePc.move(280,50)
        self.labelNumberTurn = QLabel(self)
        self.labelNumberTurn.setText("Player")
        self.labelNumberTurn.move(400,50)
        self.turn=firstPlayer
        self.Board=Board(nRows,nColumns,self)
        self.graphicBoard=GraphicBoard(nRows,nColumns,self,self.Board)
        self.graphicBoard.builGraphBoard()
        self.Board.observerGraphicBoard=self.graphicBoard
        self.pcPlayer=pcPlayer(self.Board, firstPlayer,self,self.graphicBoard)
        if(self.turn==1):
            self.pcPlayerTurn()
        print nRows,nColumns

    def changeTurn(self):
        if(self.turn==1):
            self.turn=2
        else:
            self.turn=1

    def notifyPlay(self,change):
        print "CAMBIO ",change
        if(change):
            self.changeTurn()
            if( self.turn==1):
                print "TURNO: ",self.turn
                self.pcPlayerTurn()

    def pcPlayerTurn(self):
        movimientos=[(0,0,"H")]
        print "TURNO DE LA PC"
        cont=0
        for i in movimientos:
            cont=cont+1
            if(cont<len(movimientos)):
                self.Board.updateEdge(i[2],Dod(i[0],i[1]),1,False)
            else:
                print "SI VOY A CAMBIAR DE TURNO"
                self.Board.updateEdge(i[2],Dod(i[0],i[1]),1,True)
            

    def updateGraphicBox(self,dod,owner):
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