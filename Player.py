from Card import Card

class Player:

    def __init__(self):
        self.card = ''
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.player_current_card = ''
        self.higher_lower = ''

    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.player_is_playing()

    def get_inputs(self):
        current_card = Card()
        current_card.pick()
        print(f'The card is {current_card.value}')
        self.higher_lower = input("Higher or lower [h/l] ")
        self.player_current_card = current_card.value

    def do_updates(self):
       
        if not self.is_playing:
            return 
        
        player_new_card = Card()
        player_new_card.pick()

        # if self.player_current_card > player_new_card.value:
        print(f'Next card was: {player_new_card.value}')

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
        print(f'Your score: {self.total_score}')
        self.score = 0

    def player_is_playing(self):
        play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again == "y")