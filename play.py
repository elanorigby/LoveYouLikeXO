import pdb 
from board import Board

board = Board()
board.draw()
# have a stab at the game play

row_dict = [
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 4, 'b': 5, 'c': 6},
    {'a': 7, 'b': 8, 'c': 9}]
        
player = 'X'


# find number in dict list, change to letter
def key_to_change():
    #pdb.set_trace()
    move = int(input("Where would you like to move? "))
    for row in row_dict:
        for key, val in row.items():
            if val == move:
                return row_dict.index(row), key


rownum, key = key_to_change()

print(rownum, key)

row_dict[rownum][key] = player
print(row_dict)
board.draw(row_dict)
