import pdb 
from board import Board

board = Board()
moves = 0 

print("Welcome to the world's premier Tick Tack Toe experience!")
board.draw()

player = input("Would you like to play as X or O? ").upper()

if player == 'X':
    AI = 'O'
elif player == 'O':
    AI = 'X'

# print("player", player, "AI", AI)

# game loop zoen
while moves <  9:
    move = int(input("Where would you like to move? "))
    moves += 1
    board.draw(move, player)

print("The board is full. The game is over")


