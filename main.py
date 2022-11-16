# LIBS
import sys
from random import randint
from tkinter import *

# WINDOW CREATION

root = Tk()

root.title("Rock Paper Scissors")

root.geometry("450x300")

# FUNCTIONS


def exitButtonClicked():
    root.destroy()


def computerPlays():
    computerMove = int(randint(0, 2))
    # print(computerMove)
    if computerMove == 0:
        computerLabel['text'] = 'Computer played rock'
    if computerMove == 1:
        computerLabel['text'] = 'Computer played paper'
    if computerMove == 2:
        computerLabel['text'] = 'Computer played scissors'
    return computerMove


def userPlaysRock():
    userMove = 0
    computerPlays()
    compare(userMove, computerPlays())
    playerLabel.configure(text="Player plays: Rock")


def userPlaysPaper():
    userMove = 1
    computerPlays()
    compare(userMove, computerPlays())
    playerLabel.configure(text="Player plays: Paper")


def userPlaysScissors():
    userMove = 2
    computerPlays()
    compare(userMove, computerPlays())
    playerLabel.configure(text="Player plays: Scissors")


def compare(computerMove, userMove):
    w = 'You win!'
    l = 'You lose!'
    if computerMove == userMove:
        resultLabel['text'] = 'Its a draw'
    elif userMove == 0 and computerMove == 1:
        resultLabel['text'] = w
    elif userMove == 0 and computerMove == 2:
        resultLabel['text'] = l
    elif userMove == 1 and computerMove == 0:
        resultLabel['text'] = l
    elif userMove == 1 and computerMove == 2:
        resultLabel['text'] = w
    elif userMove == 2 and computerMove == 0:
        resultLabel['text'] = w
    elif userMove == 2 and computerMove == 1:
        resultLabel['text'] = l

# GUI ELEMENTS


firstLabel = Label(
    root, text="ROCK PAPER SCISSORS GAME, CHOOSE WHAT YOU WANT TO PLAY")

firstLabel.pack()

rockButton = Button(root, text="ROCK", command=userPlaysRock)

rockButton.pack()

paperButton = Button(root, text="PAPER", command=userPlaysPaper)

paperButton.pack()

scissorsButton = Button(root, text="SCISSORS", command=userPlaysScissors)

scissorsButton.pack()

playerLabel = Label(root, text='Player plays: ')

playerLabel.pack()

computerLabel = Label(root, text='Computer plays')

computerLabel.pack()

closeButton = Button(root, text="EXIT", command=exitButtonClicked)

resultLabel = Label(root, text='Result: ')

resultLabel.pack()

closeButton.pack()

root.mainloop()
