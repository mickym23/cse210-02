from msilib.schema import ServiceControl
import random


class Secret_word:
    """The randomly picked word. 

    The responsibility of SecretWord is to randomly select the secret word. 

    Attributes:
        words (list): list of words to pick the random secret word.
        secret_word: the randomly picked secret word
        self._words: list of words to randomly pick the secret word from
        self.final_display:The word to be displayed after the letter guesses of the secret word
        self._chances:The number of times of play time the user has - helps determine type of parachute stick man to display
        _is_playing:keeps track if the game is still in play or not and feeds back this information to the director class
    """

    def __init__(self):
        """Constructs a new Secret_word.

        Args:
            self (SecretWord): An instance of Secret_word.
        """
        self._words = ["one", "two", "four", "five", "six", "eight", "nine", "ten"]
        # self._secret_word = random.choice(self._words)
        self._secret_word = "one"
        self._chances = 4
        self.final_display = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]
        self._is_playing = True

    def check_letter(self, guesser):
        """checks if the picked letter is in the randomly picked secret word

        Args:
            self (Hider): An instance of Hider.
        Returns:
            a display of the selected word and closes the game if all letters are guessed right
            or when the players chances/parachute wings are completed
        """
        guessed_letter = guesser.get_letter()

        # making a copy of the secret word that will displayed and changed as game flows
        secret_word2 = self._secret_word
        secret_word_as_list = list(secret_word2)

        length = len(self._secret_word)
        # print(f"length of guess word is {length}")
        show_word = []

        i = 0
        while i < length:
            show_word.append("_") 
            i = i + 1
            
        # print(show_word)

        if guessed_letter in self._secret_word:
            # print("The guessed letter is in secret word")

            index_of_guessed_letter = secret_word_as_list.index(guessed_letter)
            # print(index_of_guessed_letter)
            show_word[index_of_guessed_letter] = guessed_letter
            self.final_display[index_of_guessed_letter] = guessed_letter

            f_d = self.final_display[:length]
            print(f_d)

            if (f_d == list(self._secret_word)):
                print()
                print("you won!")
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
            print("\nThe guessed letter is not is in secret word.")

            # print the current word containing the already guesses letters
            f_d = self.final_display[:length]
            print(f_d)

            # reduces chances by 1
            self._chances = self._chances - 1
            if(self._chances == 0):
                print("You have run out of your guesses(chances).")
            elif(self._chances == 1):
                print(f"{self._chances} more guess(chance) remaining.")
            else:
                print(f"{self._chances} more guesses(chances) remaining.")

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

                # print(" / ___  \")
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
                
 



        # debugging code
        # if guesser.get_letter() == "a":
        #     print("a is here")
        #     if guessed_letter in self._secret_word:
        #         print("guessed letter is in secret word")
        #     else:
        #         print("guessed letter is not is in secret word")
        # else:
        #     print("not here!!")
