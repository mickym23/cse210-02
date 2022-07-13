from game.casting.actor import Actor
from game.shared.point import Point


class HelpGuide(Actor):

    def __init__(self):
        super().__init__()
        self._position = Point(760, 580)
        self.help()
       

    def help(self):
        self.set_text('Hold \'H\' for help')
        
    
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
    
    