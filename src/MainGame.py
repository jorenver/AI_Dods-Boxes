# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Game import *

class windowSettingGame(QWidget):
    def __init__(self,*args):
        QWidget.__init__(self,*args)
        self.main_widget = QWidget(self)
        self.setWindowTitle("Setting Dods And Boxes")
        self.resize(880,560)
        verticalContainer = QVBoxLayout(self)
        self.labelTitle = QLabel(self)
        self.labelTitle.setPixmap(QPixmap("TitileofGame.png"))
        self.labelTitle.move(350,10)

        self.Image = QLabel(self)
        self.Image.setPixmap(QPixmap("../imagenes/Machine.png"))
        self.Image.move(410,60)

        #Body of Widget
        self.labelRows = QLabel("Rows",self)
        self.labelRows.setStyleSheet('color:black')
        self.labelRows.move(320,160)
        self.Rows = QLineEdit(self)
        self.Rows.move(450,165)
        self.labelColumns = QLabel("Columns",self)
        self.labelColumns.setStyleSheet('color:black')
        self.labelColumns.move(320,220)
        self.Columns = QLineEdit(self)
        self.Columns.move(450,220)
        self.btnStart = QPushButton("START",self)
        self.btnStart.move(450,420)
        self.GroupOptions = QGroupBox(self)
        self.GroupOptions.setTitle("First Game")
        self.GroupOptions.setFont(QFont('SansSerif', 18))
        self.GroupOptions.setStyleSheet(" width:130px;color:black")
        self.OptionPlayerPc =QRadioButton("PC")
        self.OptionPlayerPc.setStyleSheet('color:black')
        self.OptionPlayerPc.setFont(QFont('SansSerif',16))

        self.OptionPlayerHuman = QRadioButton("Human")
        self.OptionPlayerHuman.setStyleSheet('color:black')
        self.OptionPlayerHuman.setFont(QFont('SansSerif',16))

        verticalContainer.addWidget(self.OptionPlayerHuman)
        verticalContainer.addWidget(self.OptionPlayerPc)
        self.GroupOptions.setLayout(verticalContainer)
        self.GroupOptions.move(330,300)
        self.btnStart.clicked.connect(self.openGame)

    def openGame(self):
        rows=int(self.Rows.text())
        columns=int(self.Columns.text())
        self.Ventana = Game(rows,columns,1)
        self.close()
        self.Ventana.show()

if __name__ == "__main__":
    appDotsandBoxes = QApplication(sys.argv)
    backgroundPicture = QPalette()
    backgroundPicture.setBrush(QPalette.Background,QBrush(QPixmap("../imagenes/BackgroundImage.png")))
    wSetting = windowSettingGame()
    wSetting.setPalette(backgroundPicture)
    wSetting.show()
    sys.exit(appDotsandBoxes.exec_())

