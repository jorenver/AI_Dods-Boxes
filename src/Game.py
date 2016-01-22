# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from GraphicEdge import *
from GraphicBox import *

class Game(QMainWindow):

    def __init__(self,nRows,nColumns,firstPlayer):
        # firstPlayer is 0 for pc and 1 for Human
        super(Game, self).__init__()
        self.setWindowTitle("Dots And Boxes")
        self.resize(880,560)
        self.labelPlayer = QLabel(self)
        self.labelPlayer.setText("Box_PLayer: ")
        self.labelPlayer.move(100,50)
        self.labelPc = QLabel(self)
        self.labelPc.setText("Box_PC: ")
        self.labelPc.move(320,50)
        self.buttonRestart = QPushButton("Restart",self)
        self.buttonRestart.move(490,60)
        self.buttonShowTree = QPushButton("Show Tree",self)
        self.buttonShowTree.move(590,60)
        self.labelTurn = QLabel(self)
        self.labelTurn.setText("Turn: ")
        self.labelTurn.move(700,55)
        self.labelScorePlayer = QLabel(self)
        self.labelScorePlayer.setText("8")
        self.labelScorePlayer.move(270,50)
        self.labelScorePc = QLabel(self)
        self.labelScorePc.setText("7")
        self.labelScorePc.move(435,50)
        self.labelNumberTurn = QLabel(self)
        self.labelNumberTurn.setText("12")
        self.labelNumberTurn.move(750,55)
        self.builGraphBoard(nRows,nColumns)
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
    
    """
    @description :
    """
    def builGraphBoard(self,Rows,Columns):
        COLUMNA = 50
        FILA = 200
        nfilas = 2*Rows+1
        nColumnas = 2*Columns+1
        for i in range(nfilas):
            if i%2==0:
                for j in range(nColumnas):
                    if j%2==0:
                        dot=QWidget(self)
                        dot.setMinimumHeight(30)
                        dot.setMinimumWidth(30)
                        #boton.setIcon(QIcon("Puntos-01.png"))
                        layout = QVBoxLayout(self)
                        dot.setLayout(layout)
                        layout.addWidget(QLabel("*"))
                        dot.move(COLUMNA,FILA)
                        COLUMNA = COLUMNA + 30 
                    else:
                        gEdge=GraphicEdge("horizontal",self)
                        gEdge.setMinimumHeight(30)
                        gEdge.setMinimumWidth(80)
                        gEdge.move(COLUMNA,FILA)
                        COLUMNA = COLUMNA + 60 
                      
                FILA = FILA + 50
                COLUMNA = 30
            else:
                for j in range(nColumnas):
                    if j%2==0:
                        gEdge=GraphicEdge("vertical",self)
                        gEdge.setMinimumHeight(60)
                        gEdge.setMinimumWidth(30)
                        gEdge.move(COLUMNA,FILA)
                        COLUMNA = COLUMNA + 30
                    else:
                        gBox=GraphicBox(self)
                        gBox.setMinimumHeight(60)
                        gBox.setMinimumWidth(60)
                        gBox.move(COLUMNA,FILA)
                        COLUMNA = COLUMNA + 60
                    
                    
                FILA = FILA + 50
                COLUMNA = 50
                    
                
    
    def PasarMouse(self):
        return None
    
    def darClick(self):
        return None












