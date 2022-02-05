import random

def add_one(*args) -> int:
    return args[0] + 1

def remain(*args) -> int:
    return args[0]

def reduce_one(*args) -> int:
    return args[0] - 1

def first_diagonal_y(*args) -> int:
    return args[1]

def second_diagonal_y(*args) -> int:
    return 2 - args[1]

class Board:

    def __init__(self) -> None:
        self.available_pieces = [0]*9 + [1]*9 + [2]*9
        random.shuffle(self.available_pieces)
        self.pieces = [[[False for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.rounds = 0

    def put_ring(self, coords) -> None:
        x, y = coords
        ring = self.available_pieces[0]
        if not self.pieces[y][x][ring]:
            self.pieces[y][x][ring] = True
            self.available_pieces.pop(0)
            self.rounds += 1

    def completed(self) -> bool:
        for i in range(-1, 4):
            if self.horizontal_completion(i) or self.vertical_completion(i) or self.diagonal_completion(i):
                return True            
        return False

    def diagonal_completion(self, i) -> bool:
        return self.line(add_one, second_diagonal_y, i) or self.line(add_one, first_diagonal_y, i)

    def horizontal_completion(self, i) -> bool:
        for y in range(3):
            if self.line(add_one, remain, i, x=-1, y=y):
                return True
        return False

    def vertical_completion(self, i) -> bool:
        for x in range(3):
            if self.line(remain, add_one, i, x=x, y = -1):
                return True
        return False

    def line(self, func_x, func_y, i, x=-1, y=-1):
        if i == -1:
            return self.search(add_one, func_x, func_y, i, x=x, y=y)

        if i == 3:
            return self.search(reduce_one, func_x, func_y, i, x=x, y=y)

        return self.search(remain, func_x, func_y, i, x=x, y=y)

    def search(self, func_i, func_x, func_y, i, x=-1, y=-1):
        for _ in range(3):
            i = func_i(i) 
            x = func_x(x)
            y = func_y(y, x)
            if not self.pieces[y][x][i]:
                return False
        return True

    def play(self):
        i = 0
        while not self.completed():
            i += 1
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            self.put_ring((x, y))
        return self.rounds

sum = 0
iterations = 100
for _ in range(iterations):
    board = Board()
    sum += board.play()
print(sum/iterations)