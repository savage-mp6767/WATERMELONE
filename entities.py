##  WATERMELONE  ##
##  SERVER BUILD ##
##  11/13/14     ##
##  ENTITY SYSTM ##

#base class for entities
class WMSGameEnt:
    def __init__(self):
        pass

    def Update(self):
        pass

#entity manager class
class WMSGameEntManager:
    def __init__(self):
        self.entlist = []
        self.entcount = 0

    def RegisterEnt(self,ent):
        self.entlist.append(ent)
        self.entcount = self.entcount + 1

    def Update(self):
        for ent in self.entlist:
            ent.Update()

#game object class (representing objects in the game world itself)
class WMSGameObj(WMSGameEnt):
    def __init__(self):
        pass

    def Update(self):
        pass

if __name__ == "main":
    pr
