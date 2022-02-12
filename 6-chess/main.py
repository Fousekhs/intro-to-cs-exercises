from random import randint
from typing import Tuple

def check_coords(*args):
    for arg in args:
        if arg < 0 or arg > 7:
            return False
    return True

class Piece:

    def __init__(self, colour) -> None:
        self.colour = colour
        self.x = None 
        self.y = None
        self.available_moves = []

    @property
    def coords(self):
        return (self.x, self.y)

    @coords.setter
    def coords(self, value: Tuple[int]) -> None:
        x, y = value
        self.x = x
        self.y = y

class Queen(Piece):

    def __init__(self, colour) -> None:
        super().__init__(colour)
        self.legal_moves = [(1, 1), (1, 0), (0,1), (-1, -1), (0, -1), (-1, 0), (-1, 1), (1, -1)]

class Bishop(Piece):

    def __init__(self, colour) -> None:
        super().__init__(colour)
        self.legal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

class Rook(Piece):

    def __init__(self, colour: str) -> None:
        super().__init__(colour)
        self.legal_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Board:

    def __init__(self) -> None:
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.pieces = [Queen("black"), Bishop("white"), Rook("white")]
        self.score = {"black": 0, "white": 0}

    def is_tile_free(self, coords: Tuple[int]) -> bool:
        x, y = coords
        if check_coords(y, x):
            return self.board[y][x] is None
        return False

    def put_piece(self, piece: Piece) -> None:
        coords = (randint(0, 7), randint(0, 7))
        while not self.is_tile_free(coords):
            coords = (randint(0, 7), randint(0, 7))
        
        self.board[coords[1]][coords[0]] = piece
        piece.coords = coords

    def move_calculations(self, piece: Piece) -> None:
        for d in piece.legal_moves:
            dx, dy = d
            x, y = piece.coords
            x += dx 
            y += dy

            while self.is_tile_free((x, y)):
                x += dx
                y += dy
            else:
                if check_coords(x, y):
                    if self.board[y][x].colour != piece.colour:
                        self.score[piece.colour] += 1

    def play(self) -> None:
        for piece in self.pieces:
            self.put_piece(piece)
        for piece in self.pieces:
            self.move_calculations(piece)
        print(self.score["white"])
        return self.score


score = {"white": 0, "black": 0}
for _ in range(100):
    board = Board()
    result = board.play()
    score["white"] += result["white"]
    score["black"] += result["black"]
print(score)