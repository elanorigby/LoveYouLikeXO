# just draw the board 

class Board:
    def __init__(self):
        self.wall = "+---+---+---+"
        self.cells = "| {a} | {b} | {c} |"
        self.rows = [
                {'a': 1, 'b': 2, 'c': 3},
                {'a': 4, 'b': 5, 'c': 6},
                {'a': 7, 'b': 8, 'c': 9}]

    def part(self, row):
        print(self.wall)
        print(self.cells.format(**row))

    def edit(self, move, player):
        for row in self.rows:
            for key, val in row.items():
                if val == move:
                    idx =  self.rows.index(row) 
                    self.rows[idx][key] = player

    def draw(self, *args):
        if args:
            move, player = args
            for row in self.rows:
                for key, val in row.items():
                    if val == move:
                        idx =  self.rows.index(row) 
                        self.rows[idx][key] = player

        for row in self.rows:
            self.part(row)
        print(self.wall)


if __name__=="__main__":
    board = Board()
    board.draw()
    # board takes in other list of dirs to populate

    new_rows = [
        {'a': 'X', 'b': 'X', 'c': 3},
        {'a': 4, 'b': 'O', 'c': 6},
        {'a': 7, 'b': 8, 'c': 'O'}]

    board.draw(2, 'X')
    print(board.rows)
        

