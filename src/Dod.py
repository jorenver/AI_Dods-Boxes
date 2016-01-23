class Dod():

    def __init__(self,x1,y1):
        self.x =int(x1)
        self.y =int(y1)
        self.listxy =[]
        self.setXY()

    def getXY (self):
        return self.listxy

    def setXY (self):
        self.listxy.append(self.x)
        self.listxy.append(self.y)

    def getX (self):
        return self.x

    def getY (self):
        return self.y

    def setX (self,valuex):
        self.x = valuex

    def setY (self,valuey):
        self.y = valuey
