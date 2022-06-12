# Greed Game

### Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Rules
* Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
* The player (#) can move left or right along the bottom of the screen.
* If the player touches a gem they earn a point.
* If the player touches a rock they lose a point.
* Gems and rocks are removed when the player touches them.
* The game continues until the player closes the window.

## Greed Project Structure
---
The project files and folders are organized as follows:
```
root                           (project root folder)
 +-- Greed                     (source code for game)
  +-- game                     (complete game folder)
    +-- casting                (specific game folder)
      +-- actor.py             (python game class)
      +-- artifact.py          (python game class)
      +-- cast.py              (python game class)
    +-- directing              (specific game folder)
      +-- director.py          (python game class)
    +-- shared                 (specific game folder)
      +-- point.py             (python game class)
      +-- color.py             (python game class)
    +-- services               (specific game folder)
      +-- keyboard_service.py  (python game class)
      +-- video_service.py     (python game class)
  +-- __main__.py              (entry point for program)
  +-- data                     (specific game classes)
    +-- messages.txt           (text file)
  +-- README.md                (general info)
  ```
  
## Required Software

* Visual Studio Code or similar IDE
* Python 3.8.0 or newer

<hr>

## Authors

* Mikhail Cedras (mikhail.cedras@gmail.com | *mickym23*)
* Simon Mule (simycodes@gmail.com | *simycodes*)
