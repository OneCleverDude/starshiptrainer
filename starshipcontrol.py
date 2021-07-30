import string
import time

def showShip(displayName):
    
    # This block has a lot of the code we've looked at.  Try to 
    # see if you can understand how and why it makes the choices it does.
    # 
    # Why pick 20 to subtract from?  Then why 21 later?
    # Are those the correct numbers?
    # Why pick the integer division // instead of just a / ?
    print("                   ___")
    print("      ___....-----'---'-----....___")
    if (len(displayName) > 0):
        shipLine = " "
        for x in range(20-(len(displayName)//2)):
            shipLine = shipLine + "="
        shipLine = shipLine + displayName
        for x in range(21-(len(displayName)//2)):
            shipLine = shipLine + "="
        print(shipLine)
    else:
        print(" =========================================")
    print("       ___'---..._______...---'___  ")
    print("      (___)      _|_|_|_      (___)  ")
    print("        \\____.-'_.---._'-.____//  ")
    print("          cccc'.__'---'__.'cccc ")
    print("                  ccccc")

def makeSomeScreenSpace(howmany):
    # this routine should be pretty easy to understand.  It basically clears out 6 lines.
    # think about how you'd make this a piece of code that could take an argument so it would
    # clear as many lines as you told it too.  What would that look like?
    if (howmany == 0):
        howmany = 6
    for x in range(howmany):
        print("\n")

def boom():
    print("     _.-^^---....,,--")
    print(" _--                  --_")
    print("<                        >)")
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
    playerName = input("I am ready to be relieved, Commander...? ")
    playerName = "Cmdr. " + playerName
    print("Welcome to the bridge, " + playerName)
    showShip("")
    print("\n")
    print("Right now I can't do much of anything, can I?")
    orders = "take command"
    password = '12345'
    while orders.lower() != 'quit':
        print("\n")
        orders = input("What are your orders " + playerName + " ")
        if orders.lower() == "rename":
            nameTheShip = input("maybe you want to rename the ship, " + playerName +"?")
            if (nameTheShip.upper()[:1] == 'Y'):
                shipName = input("what should the name of the ship be? ")
                showShip(shipName)
        if orders.lower() == "self destruct":
            confirmation = input("Are you sure?")
            if confirmation.upper()[:1] == 'Y':
                # TODO add pw request
                # Print("What is the Self Destruct")
                # countdown function call
                countdown(int(5))
                orders = 'quit'

        if orders.lower() == 'help':
            print("I understand orders for Help, Rename, Self Destruct and quit ")


if __name__ == "__main__":
    main()


