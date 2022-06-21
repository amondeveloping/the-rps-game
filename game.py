# Import packages to extend Python
from random import randint
from secrets import choice

from gameComponents import gameVars, winLose

# [] => this is an array
# name = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number)
# the index always starts at 0

# player_choice == False
while gameVars.player_choice is False:
    print("===============*/ RPS GAME */==================")
    print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
    print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
    print("===============================================")

    # Version 1, to explain array indexing
    # player_choice = choices[1]
    # print("index 1 in the choice array is " + player_choice + ", which is paper")

    print("Choose your weapon! Or type quit to exit\n")

    gameVars.player_choice = input("Choose rock, paper, or scissors: \n")

    if gameVars.player_choice == "quit":
        print("You chose to quit")
        exit()

    print("user chose: " + gameVars.player_choice)
    # this will be the AI choice -> a random pick from the choices array
    gameVars.computer_choice = gameVars.choices[randint (0, 2)]

    print("computer chose: " + gameVars.computer_choice)

    if gameVars.computer_choice == gameVars.player_choice:
        print("tie")

    elif gameVars.computer_choice == "rock":
        if gameVars.player_choice == "scissors":
            print("you're a LOSER")
            gameVars.player_lives = gameVars.player_lives - 1
        else:
            print("winner winner chicken dinner")
            gameVars.computer_lives = gameVars.computer_lives - 1

    elif gameVars.computer_choice == "paper":
        if gameVars.player_choice == "scissors":
            print("winner winner chicken dinner")
            gameVars.computer_lives = gameVars.computer_lives - 1
        else:
            print("you're a LOSER")
            gameVars.player_lives = gameVars.player_lives - 1

    elif gameVars.computer_choice == "scissors":
        if gameVars.player_choice == "paper":
            print("you're a LOSER")
            gameVars.player_lives = gameVars.player_lives - 1
        else:
            print("winner winner chicken dinner")
            gameVars.computer_lives = gameVars.computer_lives - 1

    if gameVars.player_lives == 0:
        winLose.winorlose("lose")
       

    if gameVars.computer_lives == 0:
        winLose.winorlose("win")
        


    print("Player lives:", gameVars.player_lives)
    print("Computer lives:", gameVars.computer_lives)


    gameVars.player_choice = False











