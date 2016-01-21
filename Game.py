# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtGui

class Game(QFrame):

    def __init__(self,nRows,nColumns,firstPlayer,secondPlayer):
        super(Game, self).__init__()
        self.setWindowTitle("Game")
        self.resize(880,560)
        self.labelTitle = QLabel(self)
        self.labelTitle.setPixmap(QPixmap("TitileofGame.png"))
        self.labelTitle.move(350,10)
        self.labelPlayer = QLabel(self)
        self.labelPlayer.setText("<h1>Box_PLayer</h1>")
        self.labelPlayer.move(100,150)
        self.lineScorePlayer = QLabel(self)
        self.lineScorePlayer.setText("<h1>____</h1>")
        self.lineScorePlayer.move(258,150)
        self.labelPc = QLabel(self)
        self.labelPc.setText("<h1>Box_PC</h1>")
        self.labelPc.move(320,150)
        self.lineScorePc = QLabel(self)
        self.lineScorePc.setText("<h1>____</h1>")
        self.lineScorePc.move(430,150)
        self.buttonRestart = QPushButton("Restart",self)
        self.buttonRestart.move(490,160)
        self.buttonShowTree = QPushButton("Show Tree",self)
        self.buttonShowTree.move(590,160)
        self.labelTurn = QLabel(self)
        self.labelTurn.setText("<h1>Turn</h1>")
        self.labelTurn.move(680,155)
        self.labelScorePlayer = QLabel(self)
        self.labelScorePlayer.setText("<h1>8</h1>")
        self.labelScorePlayer.move(278,148)
        self.labelScorePc = QLabel(self)
        self.labelScorePc.setText("<h1>7</h1>")
        self.labelScorePc.move(460,144)
        self.labelNumberTurn = QLabel(self)
        self.labelNumberTurn.setText("<h1>12</h1>")
        self.labelNumberTurn.move(750,155)
        FILA = 4
        COLUMNA = 5
        self.builGraphBoard(4,4)
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
        COLUMNA = 308
        FILA = 220
        nfilas = 2*Rows -1
        nColumnas = 2*Columns-1
        for i in range(nfilas):
            if i%2==0:
                for j in range(nColumnas):
                    if j%2==0:
                        boton=QPushButton(self)
                        boton.setMinimumHeight(60)
                        boton.setMinimumWidth(80)
                        boton.setIcon(QIcon("Puntos-01.png"))
                        boton.move(COLUMNA,FILA)
                    else:
                        boton=QPushButton(self)
                        boton.setMinimumHeight(60)
                        boton.setMinimumWidth(80)
                        boton.move(COLUMNA,FILA)
                    COLUMNA = COLUMNA + 70     
                FILA = FILA + 50
                COLUMNA = 308
            else:
                for j in range(nColumnas):
                    boton = QPushButton(self)
                    boton.setMinimumHeight(60)
                    boton.setMinimumWidth(80)
                    boton.move(COLUMNA,FILA)
                    COLUMNA = COLUMNA + 70
                FILA = FILA + 50
                COLUMNA = 308
                    
                
    
    def PasarMouse(self):
        return "null"
    
    def darClick(self):
        return "null"
    
    
appDotsandBoxes = QApplication(sys.argv)
backgroundPicture = QPalette()
backgroundPicture.setBrush(QPalette.Background,QBrush(QPixmap("BackgroundGame-01.png")))
Ventana = Game(2,3,1,0)
Ventana.setPalette(backgroundPicture)
Ventana = Game(2,3,1,0)
Ventana.show()
sys.exit(appDotsandBoxes.exec_())












