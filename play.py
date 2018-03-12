import pdb 
from board import Board

board = Board()

print("Welcome to the world's premier Tick Tack Toe experience!")
board.draw()

# adjust for enter key
def get_player():
    player = input("Would you like to play as X or O? ").upper()
    if player not in "XO":
        print("Sorry, that's not an option.")
        get_player()
    else:
        return player

player = get_player()

if player == 'X':
    AI = 'O'
elif player == 'O':
    AI = 'X'

# print("player", player, "AI", AI)

# game loop zoen

def get_move(moves):
    move = int(input("Where would you like to move? "))
    if  move > 9 or move < 1:
        print("That spot doesn't exist")
        get_move(moves)
    if move in moves:
        print("That spot is taken.")
        get_move(moves)
    else:
        moves.append(move)
        board.draw(move, player) 
    
    

moves = [] 

while len(moves) <  9:
    get_move(moves)
    
print("The board is full. The game is over")


