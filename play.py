import pdb 
from board import Board

board = Board()

print("Welcome to the world's premier Tick Tack Toe experience!")
board.draw()

player = input("Would you like to play as X or O? ").upper()

if player == 'X':
    AI = 'O'
elif player == 'O':
    AI = 'X'

print("player", player, "AI", AI)


