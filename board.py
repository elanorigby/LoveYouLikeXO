# just draw the board 

class Board:
    def __init__(self):
        self.wall = "+---+---+---+"
        self.cells = "| {} | {} | {} |"

    def part(self):
        print(self.wall)
        print(self.cells.format(1,2,3))

    def draw(self):
        self.part()
        self.part()
        self.part()
        print(self.wall)

board = Board()
board.draw()

