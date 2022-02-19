import random

class Board:

    def __init__(self) -> None:
        self.cards = [i+1 for i in range(13) for symbol in ["Heart", "Diamond", "Spade", "Club"]]
        random.shuffle(self.cards)
        self.players = [0, 0]

    def card(self, P1 = False, P2 = False) -> int:
        i=0
        if P1:
            while self.cards[i] < 10:
                i += 1
        if P2:
            while self.cards[i] > 10:
                i += 1
        return self.cards.pop(i)

    def play(self, fixed = False) -> str:
        while self.players[0] < 16:
            self.players[0] += self.card(P1=fixed)

        if self.players[0] > 21:
            return "P2"

        while self.players[1] < 16:
            self.players[1] += self.card(P2=fixed)
        if self.players[1] > 21:
            return "tie"
        
        if self.players[0] > self.players[1]:
            return "P1"
        return "P2"

for _ in range(20):
    for i in range(2): 
        score = {"P1": 0, "P2": 0, "tie": 0}
        for j in range(100):
            board = Board()
            score[board.play(i)] += 1
        if i == 1:
            print("The results over a hundred fixed games are: ")
        else:
            print("The results over a hundred normal games are: ")
        print(score)