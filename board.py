# just draw the board 

class Board:
    def __init__(self):
        self.wall = "+---+---+---+"
        self.cells = "| {a} | {b} | {c} |"
        self.rows = [
                {'a': 1, 'b': 2, 'c': 3},
                {'a': 4, 'b': 5, 'c': 6},
                {'a': 7, 'b': 8, 'c': 9}]

    def _part(self, row):
        print(self.wall)
        print(self.cells.format(**row))

    def _edit(self, move, player):
        for idx, row in enumerate(self.rows):
            for key, val in row.items():
                if val == move:
                    self.rows[idx][key] = player

    def check(self):
        for idx, row in enumerate(self.rows):
            if all(val == row['a'] for val in row.values()):
                print("You won horizontally")

        for char in 'abc':
            if self.rows[0][char] == self.rows[1][char] == self.rows[2][char]:
                print("You won vertically")

        if self.rows[0]['a'] == self.rows[1]['b'] == self.rows[2]['c']:
            print("You won like this: \\")

        if self.rows[0]['c'] == self.rows[1]['b'] == self.rows[2]['a']:
            print("You won like this: /")

            

    def draw(self, *args):
        if args:
            move, player = args
            self._edit(move, player)

        for row in self.rows:
            self._part(row)
        print(self.wall)


if __name__=="__main__":
    board = Board()
    board.draw()
    board.draw(2, 'X')
    print(board.rows)
        

