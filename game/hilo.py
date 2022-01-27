print(">Welcome to HiLo Games<")
import random

class Hilo:
    """
    Individual cards are represented as a number from 1 to 13. 
    Current card will be displayed. 
    The next card will be displayed. 
    """

    def __init__(self) -> None:
        """
        Initialize two random cards.
        """
        self.card1 = random.randint(1,13)
        self.card2= random.randint(1,13)
        self.card1 = random.randint(1,14)
        self.card2 = random.randint(1,14)


    def show_card1(self):
        """
        Display first card to the user.
        """
        output = f'The card is: {self.card1}'
        print(output)

    def show_card2(self):
        """
        Display second card to the user. 
        """

        output = f'The card is: {self.card2}'
        print(output)

        output = f'Next card was: {self.card2}'
        print(output)

    def high_or_low(self):
        """
        Check high card or low card. 
        """
        if self.card2 > self.card1:     # check for high card
            return 1
        elif self.card2 < self.card1:   # check for low card
            return 0
        else:                           # same value card
            return -1