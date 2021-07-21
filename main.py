# xd #
import random
import time
import os

print("Welcome to Flippy's Geometry Dash Challenge Script.")

while True:
    chMode = input("Which mode do you want to play? For a list of mode's type 'listmodes'. ")
    if chMode==("listmodes"):
        print("""
mappack
        """)
    elif chMode==("mappack"):
        print("In this mode, you get random Map-Pack levels, you cannot skip or practice them and you have a specific amount of attempts")
        mpchAmount=input("How many levels do you want? (MAX: 100) ")
        mpAmount = (int(mpchAmount))
        # Checks if the amount of levels if over 100, if it is the script will set it to 100 itself
        if (mpAmount>100):
            print("ERROR: You entered an amount over 100, setting amount of levels to 100.")
            mpAmount=100
        chDifficulty=input("Choose your difficulty, (Easy, Medium, Hard, Insane) ")
        if chDifficulty==("Easy"):
            intDifficulty=(100)
        elif chDifficulty==("Medium"):
            intDifficulty=(50)
        elif chDifficulty==("Hard"):
            intDifficulty=(25)
        elif chDifficulty==("Insane"):
            intDifficulty=(10)
       # Calculates the amount of attempts the user can spend on all levels.
        amAttempts=(mpAmount * intDifficulty)
        print("You chose "+str(mpAmount)+" levels, and difficulty "+(chDifficulty)+", this will give you "+(str(amAttempts))+" attempts to complete the levels.")
        # Gets the cwd (Current Working Directory) to open the file with all the mappack IDs in it.
        cwdPath = os.getcwd()
        with open(cwdPath + "/lvlist/mpids.cid") as f:
            ids = [line.rstrip() for line in f]
            random.shuffle(ids)
            # This runs for every ID in the list (Specified by the user earlier, check line 16)
            for elem in ids[:mpAmount]:
                print("You got "+str(elem)+" you have "+str(amAttempts)+" attempts left.")
                attImp = input("How many attempts did you need for the level? ")
                # Calculation to subtract the attempts the user needed from the total attempts available
                subAttct=(int(attImp))
                amAttempts=amAttempts-subAttct
                if amAttempts<1:
                    print("You failed the challenge! You needed to many attempts")
                    time.sleep(3)
                    break
                else:
                    print("You have " + str(amAttempts) + " left.")











