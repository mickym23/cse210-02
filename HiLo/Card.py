import random

class Card:

    def __init__(self):
        self.value = 0
        self.points = 0

    def pick(self):
        self.value = random.randint(1, 13)
