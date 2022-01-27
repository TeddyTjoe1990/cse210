from hilo import Hilo
class Player:
    """
    The player direct control the game.
    Player starts the game with 300 points.
    If player guess higher or lower:
    - The player earns 100 points if guess is correct.
    - The player loses 75 points if they guessed is incorrectly.
    - If player reaches 0 points the game is over.
    Player decides to keep playing or stop the game.
    """
    def __init__(self):
        """
        Construct a player object.
        """
        self.points = 300
        self.is_playing = True
        self.total_points = 0
        self.hl = 0
        
    def play_game(self):
        """
        Start the game Hilo
        """
        while self.is_playing:
            card = Hilo()
            card.show_card1()
            self.hl = card.high_or_low()
            self.update_points()
            card.show_card2()
            self.display_score()
            self.play_again()

    def guess_hilo(self):
        """
        Ask user for a higher or lower guess.
        """
        guess = input("Higher or lower? [h/l]: ")
        return guess

    def update_points(self):
        """
        It will add or substract point from the user.
        """
        player_guess = self.guess_hilo()
        if (self.hl == 1 and player_guess == "h") or (self.hl == 0 and player_guess == "l"):
            self.points += 100
        elif (self.hl == 1 and player_guess == "l") or (self.hl == 0 and player_guess == "h"):
            self.points -= 75
        else:
            self.points += 0

    def display_score(self):
        """
        Display final score to the player.
        """
        self.total_points = self.points
        print(f'Your score is:  {self.total_points}')

    def play_again(self):
        """
        Ask the user if they want to play again and check if points are not 0
        """
        again = input("Play again? [y/n]: ")
        if self.points > 0 and again == "y":
            self.is_playing = True
            print()
        elif self.points <= 0 or again == "n":
            print("Game is over.")
            print()
            self.is_playing = False
