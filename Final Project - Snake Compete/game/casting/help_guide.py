from game.casting.actor import Actor
from game.shared.point import Point


class HelpGuide(Actor):
    """
    This class helps to add the 'Hold for Help' display in the bottom right corner of the HUD. 

    """

    def __init__(self):
        super().__init__()

        # Bottom right position
        self._position = Point(760, 580)

        # Call for the help text method
        self.help()
       

    def help(self):
        """
        Sets the message for the class instance 
        """
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
    
    