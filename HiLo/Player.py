from pyray import poll_input_events
from Card import Card

class Player:
    """The person directing the game flow. 
     Controls the sequence of play.

    Attributes:
        is_playing (boolean): indicates if the game is being played or not.
        score (int): The score for one round of play.
        total_score (int): Accumulated total score - player starts with an initial 300 points.
        higher_lower :holds user input for the guess of number being higher or lower
    """

    def __init__(self):
        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        self.is_playing = True
        # self.card = ''
        self.score = 0
        self.total_score = 300
        self.player_current_card = ''
        self.higher_lower = ''

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Player): an instance of Player.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.player_is_playing()

    def get_inputs(self):
        """Ask the user the guess of the next card being higher or lower.

        Args:
            self (Player): An instance of Player.
        """
        current_card = Card()
        current_card.pick()

        print("\nHiLO Game!")
        print("Guess if the next card number will be Higher or Lower than the current card number shown.")
        print(f'\nThe card is {current_card.value}')
        self.higher_lower = input("Higher or lower [h/l] : ")
        self.player_current_card = current_card.value

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Player): An instance of Player.
        """
       
        if not self.is_playing:
            return 
        
        player_new_card = Card()
        player_new_card.pick()

        # if self.player_current_card > player_new_card.value or if if self.player_current_card < player_new_card.value
        # show the player if their guess was right or wrong
        print(f'Next card was: {player_new_card.value}')

        # if player guess is higher and its true add 100 to player score else reduce by 75
        # if player is lower and its true add 100 to player score else reduce by 75
        if self.higher_lower == "h" and self.player_current_card < player_new_card.value:
            self.score = self.score + 100
        elif self.higher_lower == "h" and self.player_current_card > player_new_card.value:
            self.score = self.score - 75
        elif self.higher_lower == "l" and self.player_current_card > player_new_card.value:
            self.score = self.score + 100
        elif self.higher_lower == "l" and self.player_current_card < player_new_card.value:
            self.score = self.score - 75


        self.total_score += self.score

    def do_outputs(self):
        """Shows the players total score which is either increased if player won or reduced if player lost. 

        Args:
            self (Player): An instance of Player.
        """
        print(f'Your score: {self.total_score}')
        self.score = 0

    def player_is_playing(self):
        """Asks the player if he wants to play again or not. 

        Args:
            self (Player): An instance of Player.
        """
        play_again = input("Play again? [y/n] : ")
        self.is_playing = (play_again == "y")