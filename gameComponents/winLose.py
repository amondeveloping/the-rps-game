from gameComponents import gameVars

def winorlose(status):
    #print("Inside winorlose function; status is:", status)
    print("You", status, "Would you like to play again?")
    gameVars.choice = input("Y / N? ")

    if gameVars.choice == "N" or gameVars.choice == "n":
        print("You're a QUITTER! Better luck next time!")
        exit()
    elif gameVars.choice == "Y" or gameVars.choice == "y":

        gameVars.player_lives = gameVars.total_lives
        gameVars.computer_lives = gameVars.total_lives
    else:
        print("Pick one dum dum - Y or N")
        gameVars.choice = input("Y / N? ")