from game.casting.actor import Actor
from game.shared.point import Point


class GameInstructionDisplay(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """

    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)
        self._position = Point(225, 0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score ATLEAST 25 POINTS & COLLIDE into you opponent to WIN!")

    def get_points(self, points):
        """Gets the current score
        
        Returns:
            Score: The current score.
        """
        return self._points

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
