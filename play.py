import pdb 
from board import Board


# adjust for enter key
def get_player():
    player = input("Would you like to play as X or O? ").upper()
    if player not in "XO":
        print("Sorry, that's not an option.")
        get_player()
    else:
        return player

#if player == 'X':
#    AI = 'O'
#elif player == 'O':
#    AI = 'X'


def get_move(moves):
    try:
        move = int(input("Where would you like to move? "))
        if  move > 9 or move < 1:
            print("That spot doesn't exist")
            get_move(moves)

        if move in moves:
            print("That spot is taken.")
            get_move(moves)
        
        moves.append(move)
        return move

    except ValueError:
        print("That spot doesn't exist")
        get_move(moves)

    
if __name__ == "__main__":    

    board = Board()

    print("Welcome to the world's premier Tick Tack Toe experience!")

    board.draw()

    player = get_player()

    moves = [] 

    while len(moves) <  9:
        move = get_move(moves)
        board.draw(move, player)

        
    print("The board is full. The game is over")

