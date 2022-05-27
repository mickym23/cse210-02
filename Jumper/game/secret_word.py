import random

from game.terminal_service import TerminalService as _ts
class Secret_word:
    """The randomly picked word. 

    The responsibility of SecretWord is to randomly select the secret word. 

    Attributes:
        words (list): List of words to pick the random secret word.
        secret_word: The randomly picked secret word
        self._words: List of words to randomly pick the secret word from
        self.final_display: The word to be displayed after the letter guesses of the secret word
        self._chances: The number of times of play time the user has - helps determine type of parachute stick man to display
        _is_playing: Keeps track if the game is still in play or not and feeds back this information to the director class
    """

    def __init__(self):
        """Constructs a new Secret_word.

        Args:
            self (SecretWord): An instance of Secret_word.
        """
        self._words = ["one", "two", "four", "five", "six", "eight", "nine", "ten", "blue", "red", "green", "purple", "yellow", "black", "rugby", "golf", "cricket", "football", "soccer", "pool", "darts", "poker", "dominoes", "cards", "joker", "ace", "spades", "gray", "grey", "orange", "violet"]
        self._secret_word = random.choice(self._words)
        self._chances = 4
        self.final_display = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]
        self._is_playing = True

    def check_letter(self, guesser):
        """
        Overview: 
            Checks if the picked letter is in the randomly picked secret word

        Args:
            self (Secret_word): An instance of Secret_word.
            guesser: An instance of the guesser class.
        Returns:
            A display of the selected word and closes the game if all letters are guessed right
            or when the players chances/parachute wings are completed
        """
        guessed_letter = guesser.get_letter()

        # making a copy of the secret word that will displayed and changed as game flows
        secret_word2 = self._secret_word

        length = len(self._secret_word)

        show_word = []

        i = 0
        while i < length:
            show_word.append("_") 
            i = i + 1

        if guessed_letter in self._secret_word:
            
            # Creates a list with the indices of characters that match the guessed letter
            letter_indexes = self._find_index(guessed_letter, self._secret_word)

            # Running a loop which fills the list blanks for each index that matches
            for i in letter_indexes:
                show_word[i] = guessed_letter
                self.final_display[i] = guessed_letter

            # Shorten the list to match the word
            f_d = self.final_display[:length]
            
            word_secret_output = '' 

            # Word output, initially with blanks
            for blank in f_d:
              word_secret_output += ' ' + blank
            print(f'Word: {word_secret_output}')

            # list of phrases to output when the user wins
            win_phrases = ['Congratulations! You won!', 'You are a Jumper guru. Well done!', 'You\'re amazing! You won!', 'You make it look easy, congrats! You won!']

            # Print phrase when user wins
            if (f_d == list(self._secret_word)):
                print(f'\n{random.choice(win_phrases)}')
                self._is_playing = False
            else:
                if (self._chances == 4):
                    print()
                    print("   ___  ")
                    print(" / ___ \\")
                    print(" \     /")
                    print("  \   /")
                    print("    0        ")
                    print("  / | \ ")
                    print("   / \ ")
                    print("\n^^^^^^^^^")
                elif (self._chances == 3):
                    print()
                    print(" / ___ \\")
                    print(" \     /")
                    print("  \   /")
                    print("    0        ")
                    print("  / | \ ")
                    print("   / \ ")
                    print("\n^^^^^^^^^")
                elif (self._chances == 2):
                    print()
                    print(" \     /")
                    print("  \   /")
                    print("    0        ")
                    print("  / | \ ")
                    print("   / \ ")
                    print("\n^^^^^^^^^")
                elif(self._chances == 1):
                    print()
                    print("  \   /")
                    print("    0        ")
                    print("  / | \ ")
                    print("   / \ ")
                    print("\n^^^^^^^^^")
                else:
                    print()
                    print("    x")
                    print("  / | \ ")
                    print("   / \ ")
                    print("\n^^^^^^^^^")

                    self._is_playing = False

        else:
            f_d = self.final_display[:length]
            
            word_secret_output = '' 

            # Word output initially, with blanks
            for space in f_d:
              word_secret_output += ' ' + space + ' '
            
            print(f'Word: {word_secret_output}')

            print("\nNo! The your guessed letter is not in the secret word.")

            # reduces chances by 1
            self._chances = self._chances - 1
            if(self._chances == 0):
                print("You have run out of your guesses.")
            elif(self._chances == 1):
                print(f"You have {self._chances} more guess remaining.")
            else:
                print(f"You have {self._chances} more guesses remaining.")

            if (self._chances == 4 ):
                print()
                print("   ___  ")
                print(" / ___ \\")
                print(" \     /")
                print("  \   /")
                print("    0        ")
                print("  / | \ ")
                print("   / \ ")
                print("\n^^^^^^^^^")

            elif (self._chances == 3):
                print()
                print(" / ___ \ ")
                print(" \     /")
                print("  \   /")
                print("    0        ")
                print("  / | \ ")
                print("   / \ ")
                print("\n^^^^^^^^^")

            elif (self._chances == 2):
                print()
                print(" \     /")
                print("  \   /")
                print("    0        ")
                print("  / | \ ")
                print("   / \ ")
                print("\n^^^^^^^^^")

            elif(self._chances == 1):
                print()
                print("  \   /")
                print("    0        ")
                print("  / | \ ")
                print("   / \ ")
                print("\n^^^^^^^^^")
            else:
                print()
                print("    x")
                print("  / | \ ")
                print("   / \ ")
                print("\n^^^^^^^^^")

                self._is_playing = False

              
    def _find_index(self, letter, word):
        """
        Overview: 
            Finds the characters in a word that matches a given letter.

        Args:
            self (Secret_word): An instance of Secret_word.
            letter: An input letter that will be checked.
            word: The given word that will be checked for the relevant letter
        
        Returns:
            A list of indices that match the letter
        """

        lst = []

        # Creates variables, i, ch, and creates an object of the word 
        for i,ch in enumerate(word):

            # If the input letter equals a character of
            #  the word, it's index is added to the list
            if letter == ch:
                lst.append(i)
        return lst

    def _reset(self):
        """
        Overview: 
            Resets the class to its initial values - used when players want to play again

        Args:
            self (Secret_word): An instance of Secret_word.
        """
        self._secret_word = random.choice(self._words)
        self._chances = 4
        self.final_display = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]
        self._is_playing = True


    