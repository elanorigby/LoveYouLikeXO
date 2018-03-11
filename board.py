# just draw the board 

class Board:
    def __init__(self):
        self.wall = "+---+---+---+"
        self.cells = "| {} | {} | {} |"

    def part(self):
        print(self.wall)
        print(self.cells)

    def draw(self):
        self.part()
        self.part()
        self.part()
        print(self.wall)

board = Board()
board.draw()

