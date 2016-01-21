# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class windowSettingGame(QFrame):
    def __init__(self):
        super(windowSettingGame, self).__init__()
        self.setWindowTitle("Main Window Dots and Boxes")
        self.resize(880,560)
        verticalContainer = QVBoxLayout(self)
        self.labelTitle = QLabel(self)
        self.labelTitle.setPixmap(QPixmap("TitileofGame.png"))
        self.labelTitle.move(350,10)

        self.Image = QLabel(self)
        self.Image.setPixmap(QPixmap("Machine.png"))
        self.Image.move(410,60)

        #Body of Widget
        self.labelRows = QLabel("<h1>Rows</h1>",self)
        self.labelRows.setStyleSheet('color:black')
        self.labelRows.move(320,160)
        self.Rows = QLineEdit(self)
        self.Rows.move(450,165)
        self.labelColumns = QLabel("<h1>Columns</h1>",self)
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


appDotsandBoxes = QApplication(sys.argv)
backgroundPicture = QPalette()
backgroundPicture.setBrush(QPalette.Background,QBrush(QPixmap("BackgroundImage.png")))


wSetting = windowSettingGame()
wSetting.setPalette(backgroundPicture)
wSetting.show()
sys.exit(appDotsandBoxes.exec_())

