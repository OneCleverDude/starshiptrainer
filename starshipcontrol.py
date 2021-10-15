import string
import time
from starship import Starship 
from player import Player
from starbase import Starbase

def makeSomeScreenSpace(howmany):
    # this routine should be pretty easy to understand.  It basically clears out 6 lines.
    # think about how you'd make this a piece of code that could take an argument so it would
    # clear as many lines as you told it too.  What would that look like?
    if (howmany == 0):
        howmany = 6
    for x in range(howmany):
        print("\n")
def boom(displayName):
    print("     _.-^^---....,,--")
    print(" _--                  --_")
    print("<                        >)")
    if (len(displayName) > 0):
        shipLine = "|"
        for x in range(12-(len(displayName)//2)):
            shipLine = shipLine + " "
        shipLine = shipLine + displayName
        for x in range(13-(len(displayName)//2)):
            shipLine = shipLine + " "
        shipLine= shipLine + "|"
        print(shipLine)
    else:
        print("|                         |")
    print(" \._                   _./")
    print("    ```--. . , ; .--'''")
    print("          | |   |")
    print("       .-=||  | |=-.")
    print("       `-=#$%&%$#=-'")
    print("          | ;  :|")
    print(" _____.,-#%&$@%#&#~,._____")
def teddy():
    print("\n")
    print("Quit your crying!! Here's a Teddy Bear!!!")
    print("\n")
    print("     ,~~.,''''`'.~~.")
    print("    : {` .- _ -. '} ;")
    print("     `:   O(_)O   ;'")
    print("      ';  ._|_,  ;`")
    print("       '`-.\_/,.'`")
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    boom()
    teddy()

def main():
    makeSomeScreenSpace(4)

    currentplayer = Player(input("I am ready to be relieved, ...? "))

    print("Welcome to the bridge, " + currentplayer.fullrankandtitle)
    #
    # This makes an object called myShip which is a instance of the Starship class above.
    #
    myShip = Starship(input("what is the name of your ship? "))
    print("\n")
    orders = "take command"
    deepSpaceNine = Starbase("Deep Space Nine")

    password = '12345'
    while orders.lower() != 'quit':
        print("\n")
        orders = input("What are your orders " + currentplayer.fullrankandtitle + " ")
        if orders.lower() == "rename":
            myShip.renameShip(input("what should the name of the ship be? "))
            #
            #  This was changed to call a method on the Starship class!
            #
            myShip.showShip()
        if orders.lower() == "beam me up":
            myShip.transport(currentplayer.playername)
        if (orders.lower() == "self destruct" or orders.lower() == 'quit'):
            boom(myShip.shipname)
            orders = 'quit'
        if orders.lower() == "self destruct":
            confirmation = input("Are you sure?")
            if confirmation.upper()[:1] == 'Y':
                # TODO add pw request
                # Print("What is the Self Destruct")
                # countdown function call
                countdown(int(5))
                orders = 'quit'

        if orders.lower() == 'help':
            print("I understand orders for Help, Rename, Self Destruct, Beam me up, Launch Fighters, shoot and quit ")
        if orders.lower() == 'shoot':
            print("pew pew pew")
            myShip.launchTorpedo()
        if orders.lower() == "status":
            myShip.showShip()

        if orders.lower() == "promote":
            currentplayer.promotePlayer()
        if orders.lower() == 'launch fighters':
            myShip.launchFighters()


if __name__ == "__main__":
    main()


