from Dod import *
class Edge():

    def __init__(self,dodNext,dodPrev,Owner):
        super(Edge, self).__init__()
        self.prev = dodPrev
        self.next = dodNext
        self.owner = Owner


    def getPrevDod(self):
        return self.prev

    def getNextDod(self):
        return self.next

    def getOwner (self):
        return self.owner

    def setOwner (self,Owner):
        self.owner = Owner
