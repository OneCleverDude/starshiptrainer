import string
import time
from transporters import transport
from fighters import launch

class Starship:
    def __init__(self, shipname):
        self.shipname = shipname
        self.shields = "down"
        self.fighters = "docked"
        self.shiptype = "galaxy class heavy cruiser"
        self.torpedoes = 3
        self.maxtorpedoes = 5

    def renameShip(self, shipname):
        self.shipname = shipname
        print ("Ship has been renamed to " + self.shipname)    

    def transport(self, crewmember):
        transport(crewmember)

    def launchFighters(self):
        launch(self)

    def showShip(self):
        # This block has a lot of the code we've looked at.  Try to 
        # see if you can understand how and why it makes the choices it does.
        # 
        # Why pick 20 to subtract from?  Then why 21 later?
        # Are those the correct numbers?
        # Why pick the integer division // instead of just a / ?
        print("                   ___")
        print("      ___....-----'---'-----....___")
        if (len(self.shipname) > 0):
            shipLine = " "
            for x in range(20-(len(self.shipname)//2)):
                shipLine = shipLine + "="
            shipLine = shipLine + self.shipname
            for x in range(21-(len(self.shipname)//2)):
                shipLine = shipLine + "="
            print(shipLine)
        else:
            print(" =========================================")
        print("       ___'---..._______...---'___  ")
        print("      (___)      _|_|_|_      (___)  ")
        print("        \\____.-'_.---._'-.____//  ")
        print("          cccc'.__'---'__.'cccc ")
        print("                  ccccc")
        print ("\n")
        print ("Torpedoes aboard " + str(self.torpedoes))
        print ("fighters aboard " + str(self.fighters))
    
    
    def launchTorpedo(self):
        if self.torpedoes > 0:
            print("launch torpedo!")
            self.torpedoes = self.torpedoes -1
        else:
            print("You are all out of torpedoes!  Go back to starbase and get more")