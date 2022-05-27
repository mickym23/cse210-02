# Jumper Game

### Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

## Rules
* The puzzle is a secret word randomly chosen from a list.
* The player guesses a letter in the puzzle.
* If the guess is correct, the letter is revealed.
* If the guess is incorrect, a line is cut on the player's parachute.
* If the puzzle is solved the game is over.
* If the player has no more parachute the game is over.

## Jumper Project Structure
---
The project files and folders are organized as follows:
```
root                         (project root folder)
+-- Jumper                   (source code for game)
  +-- game                   (specific game classes)
    +-- director.py          (python game class)
    +-- guesser.py           (python game class)
    +-- secret_word.py       (python game class)
    +-- terminal_service.py  (python game class)
  +-- __main__.py            (entry point for program)
  +-- README.md              (general info)
  ```
  
## Required Software

* Visual Studio Code or similar IDE
* Python 3.8.0 or newer

<hr>

## Authors

* Mikhail Cedras (mikhail.cedras@gmail.com | *mickym23*)
* Simon Mule (simycodes@gmail.com | *simycodes*)
