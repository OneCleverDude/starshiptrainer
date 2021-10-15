import string
from transporters import transport

class Starbase:
    def __init__(self, starbasename):
        self.starbasename = starbasename
        self.torpedoes = 15
        print ("Yay, " + starbasename + " is in range!")

    def transferTorpedos(self):
        if self.torpedoes > 1:
            self.torpedoes = self.torpedoes -1
            print ("transfered a torpedo")
        else:
            print ("starbase is out of torpedos")
    
    def transport(crewmember):
        transport(crewmember)