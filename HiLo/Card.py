import random

class Card:
    """A single card with a number.
    The card holds the randomly picked number.
   
    Attributes:
        value (int): The actual card number.
    """

    def __init__(self):
        """Constructs a new instance of the Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0
        # self.points = 0

    def pick(self):
        """Picks a randome number between 1 and 13.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value = random.randint(1, 13)
