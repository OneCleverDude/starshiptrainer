import string
import time
import random

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
    print("Quit your crying!! Here's a couple Teddy Bears!!!")
    print("\n")
    print("     ,~~.,''''`'.~~.")
    print("    : {` .- _ -. '} ;")
    print("     `:   O(_)O   ;'")
    print("      ';  ._|_,  ;`")
    print("       '`-.\_/,.'`")
    print("\n")
    print("                  _     _")
    print("                 ( \---/ )")
    print("                  ) . . (")
    print("____________,--._(___Y___)_,--.___________ ")
    print("            `--'           `--'")

# def subwaySandwich():
#     print("                      88                                                     ")
#     print("                      88                                                     ")
#     print("                      88                                                     ")
#     print(",adPPYba, 88       88 88,dPPYba,  8b      db      d8 ,adPPYYba, 8b       d8  ")
#     print("I8[    "" 88       88 88P'    ""8a `8b    d88b    d8' ""     `Y8 `8b     d8'  ")
#     print(" `""Y8ba,  88       88 88       d8  `8b  d8'`8b  d8'  ,adPPPPP88  `8b   d8'   ")
#     print("aa    ]8I ""8a,   ,a88 88b,   ,a8""   `8bd8'  `8bd8'   88,    ,88   `8b,d8'    ")
#     print("`"YbbdP"'  `"YbbdP'Y8 8Y"Ybbd8"'      YP      YP     `"8bbdP"Y8     Y88'     ")
#     print("                                                                    d8'      ")
#     print("                                                                   d8'       ")


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
    shipName = ""
    playerName = input("I am ready to be relieved, Commander...? ")
    playerName = "Cmdr. " + playerName
    print("Welcome to the bridge, " + playerName + ". Here's your ship")
    print("\n")
    shipName = playerName
    showShip(shipName)
    print("\n")
    print("We've named your ship after you. If you'd like to rename it type in, 'rename'.")
    orders = "take command"
    passcode = "12345"
    orderUnderstood = 0
    while orders.lower() != 'quit':
        print("\n")
        orders = input("What are your orders " + playerName + " ")

        # Orders below - rename, show ship, self destruct, help, quit, etc..
        if orders.lower() == "rename":
            nameTheShip = input("Are you sure you want to rename the ship, " + playerName +"?")
            if (nameTheShip.upper()[:1] == 'Y'):
                shipName = input("What should the new name of the ship be? ")
                showShip(shipName)
            orderUnderstood == True
        if orders.lower() == "show ship":
            showShip(shipName)
            orderUnderstood == True
        if orders.lower() == "self destruct":
            confirmation = input("Are you sure? ")
            if confirmation.upper()[:1] == 'Y':
                passcodeRequest = input("What is the Self Destruct code? ")
                if passcodeRequest != passcode:
                    print("Sorry that's an incorrect passcode.")
                    continue
                else:
                    countdown(int(5))
                    orders = 'quit'
            else:
                continue
            orderUnderstood == True
        if orders.lower() == 'help':
            print("I understand orders for Help, Rename, Self Destruct and Quit ")
            orderUnderstood == True
        # if orders.lower() == 'subway' or 'sandwich':
        #     print("Justin has made you a delicous Subway sandwich!! Here it is")
        #     print("\n")
        #     print("\n")
        #     subwaySandwich()
        #     print("\n")
        #     print("\n")
        #     orderUnderstood == True
        if orderUnderstood == False:
            print("I'm sorry, I do not understand that command. Ask for 'help' if you want a list of commands.")


if __name__ == "__main__":
    main()


