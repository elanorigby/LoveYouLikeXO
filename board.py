# just draw the board 

class Board:
    def __init__(self):
        self.wall = "+---+---+---+"
        self.cells = "| {a} | {b} | {c} |"
        self.initalize = [
                {'a': 1, 'b': 2, 'c': 3},
                {'a': 4, 'b': 5, 'c': 6},
                {'a': 7, 'b': 8, 'c': 9}]

    def part(self, row):
        print(self.wall)
        print(self.cells.format(**row))

    def draw(self, *arg):
        if arg:
            rows = arg[0]
        else:
            rows = self.initalize
        for row in rows:
            self.part(row)
        print(self.wall)

board = Board()
board.draw()
# board takes in other list of dirs to populate

new_rows = [
    {'a': 'X', 'b': 'X', 'c': 3},
    {'a': 4, 'b': 'O', 'c': 6},
    {'a': 7, 'b': 8, 'c': 'O'}]

board.draw(new_rows)
        

