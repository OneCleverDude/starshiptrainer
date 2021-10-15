import string

def launch(starship):
    if starship.fighters == "docked":
        print("Launching fighters!")
        starship.fighters = "launched"
    else:
        print("No fighters are docked Commander.")