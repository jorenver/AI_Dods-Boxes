# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

class windowSettingGame(QtGui.QFrame):
    def __init__(self):
        super(windowSettingGame, self).__init__()
        self.setWindowTitle("Main Window Dots and Boxes")
        self.resize(880,560)
        verticalContainer = QtGui.QVBoxLayout(self)
        self.labelTitle = QtGui.QLabel(self)
        self.labelTitle.setPixmap(QtGui.QPixmap("TitileofGame.png"))
        self.labelTitle.move(350,10)

        self.Image = QtGui.QLabel(self)
        self.Image.setPixmap(QtGui.QPixmap("Machine.png"))
        self.Image.move(410,60)

        #Body of Widget
        self.labelRows = QtGui.QLabel("<h1>Rows</h1>",self)
        self.labelRows.setStyleSheet('color:black')
        self.labelRows.move(320,160)
        self.Rows = QtGui.QLineEdit(self)
        self.Rows.move(450,165)
        self.labelColumns = QtGui.QLabel("<h1>Columns</h1>",self)
        self.labelColumns.setStyleSheet('color:black')
        self.labelColumns.move(320,220)
        self.Columns = QtGui.QLineEdit(self)
        self.Columns.move(450,220)
        self.btnStart = QtGui.QPushButton("START",self)
        self.btnStart.move(450,420)
        self.GroupOptions = QtGui.QGroupBox(self)
        self.GroupOptions.setTitle("First Game")
        self.GroupOptions.setFont(QtGui.QFont('SansSerif', 18))
        self.GroupOptions.setStyleSheet(" width:130px;color:black")
        self.OptionPlayerPc = QtGui.QRadioButton("PC")
        self.OptionPlayerPc.setStyleSheet('color:black')
        self.OptionPlayerPc.setFont(QtGui.QFont('SansSerif',16))

        self.OptionPlayerHuman = QtGui.QRadioButton("Human")
        self.OptionPlayerHuman.setStyleSheet('color:black')
        self.OptionPlayerHuman.setFont(QtGui.QFont('SansSerif',16))

        verticalContainer.addWidget(self.OptionPlayerHuman)
        verticalContainer.addWidget(self.OptionPlayerPc)
        self.GroupOptions.setLayout(verticalContainer)
        self.GroupOptions.move(330,300)

appDotsandBoxes = QtGui.QApplication(sys.argv)
backgroundPicture = QtGui.QPalette()
backgroundPicture.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("BackgroundImage.png")))


wSetting = windowSettingGame()
wSetting.setPalette(backgroundPicture)
wSetting.show()
sys.exit(appDotsandBoxes.exec_())

