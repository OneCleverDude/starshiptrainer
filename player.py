import string

class Player:
    def __init__(self, playername):
        self.playername = playername
        self.currentrank = "lt."
        self.fullrankandtitle = self.currentrank + " " + self.playername
    
    def promotePlayer(self):       
        if self.currentrank == "cmdr.":
            self.currentrank = "private"
            print("busted!  You can't promote yourself that high.")
        if self.currentrank == "lt. cmdr.":
            self.currentrank = "cmdr."
        if self.currentrank == "lt.":
            self.currentrank = "lt. cmdr."
        
        self.fullrankandtitle = self.currentrank + " " + self.playername   