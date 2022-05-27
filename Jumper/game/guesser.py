class Guesser:
    """The person guessing the word. 
    
    The responsibility of a Guesser to help the player guess each letter of the randomly selected game.
    
    Attributes:
    _guessed_letter: the variable that will hold the guessed letter given by the user
    """
    def __init__(self):
        """Constructs a new Guesser.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self._guessed_letter = " "

    def get_letter(self):
        """
        Overview: 
            Getter method for the user's letter that is guessed.
        
        Returns:
            string: The current guessed letter
        """
        return self._guessed_letter
        
    def update_new_guessed_letter(self, new_guessed_letter):
        """
        Overview:
            Setter method for the letter that will be guessed. 
        
        Returns:
            N/A
        """
        self._guessed_letter = new_guessed_letter

        
