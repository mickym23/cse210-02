from game.terminal_service import TerminalService
from game.secret_word import Secret_word
from game.guesser import Guesser

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        secret_word (Secret_word): The game's secret_word.
        is_playing (boolean): Whether or not to keep playing.
        guesser (Guesser): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._secret_word = Secret_word()  # instance creation of the Secret_word class
        self._is_playing = True
        self._guesser = Guesser()  # instance creation of the Guesser class
        self._terminal_service = TerminalService() #instance creation of the TerminalService class
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        welcome_message = True
        while self._is_playing:

            # printing the welcome display for the game only once
            if (welcome_message == True):
                self.welcome_display()
                
            
            # continuing with the repeated game flow
            self._get_inputs()
            self._do_updates()
            self._outputs()

            welcome_message = False

    def _get_inputs(self):
        """Makes the guesser have a new guessed letter

        Args:
            self (Director): An instance of Director.
        """
        # self._guesser.get_letter()
        new_guessed_letter = self._terminal_service.read_letter("\nGuess a letter [a - z]: ")
        # print(new_guessed_letter)
        self._guesser.update_new_guessed_letter(new_guessed_letter)
        # self._guesser.get_letter()
        
    def _do_updates(self):
        """Check if the guessed letter is correct and do the adjustments.

        Args:
            self (Director): An instance of Director.
        """
        # print()
        # self._guesser.get_letter()
        self._secret_word.check_letter(self._guesser)
        
    def _outputs(self):
        """
        Overview:
            Checks if the user is still playing and outputs appropriately.

        Args:
            self (Director): An instance of Director.
        """
        self._is_playing = self._secret_word._is_playing
        if(self._is_playing == True):
            print("")
        else:
            print()
            play_again = self._terminal_service.read_letter("Do you want to play again? (y/n): ")

            if play_again.strip().lower() == 'y':
                self._is_playing = True
                self._secret_word._reset()
                self.start_game()
            else: 
                self._terminal_service.write_text('Thank you for playing!\n')


  
    def welcome_display(self):
        """
        Overview:
            This is the initial welcome board that introduces the new player and lets them know what they are looking out for.

        Args:
            self (Director): An instance of Director.
        """
        # making a copy of the secret word that will displayed and changed as game flows
        secret_word2 = self._secret_word._secret_word

        length = len(secret_word2)
        # print(f"length of guess word is {length}")
        show_word = []

        i = 0
        while i < length:
            show_word.append("_")
            i = i + 1

        print(f"\nWelcome To The Jumper Game!\nYour mission: Guess a letter that is part of the {length} lettered word below!")
        print() # blank line

        word_secret_output = '' 

        for space in show_word:
            word_secret_output += ' ' + space
        
        print(f'Word: {word_secret_output}')

        print()
        print("   ___  ")
        print(" / ___ \\")
        print(" \     /")
        print("  \   /")
        print("    0        ")
        print("  / | \ ")
        print("   / \ ")

        print("\n^^^^^^^^^")
