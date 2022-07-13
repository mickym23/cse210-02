from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # Preparing the game score for snake 1
        score = cast.get_first_actor("scores")
        scoreTwo = cast.get_first_actor("scoresTwo")
        GameInstructionDisplay = cast.get_first_actor("GameInstructionDisplay")

        # Preparing the game food
        food = cast.get_first_actor("foods")

        # Preparing snake one for display
        snake = cast.get_first_actor("snakes")
        segments = snake.get_segments()

        # Preparing snake two for display
        snakeTwo = cast.get_first_actor("snakesTwo")
        segmentsTwo = snakeTwo.get_segments()

        # Preparing message information for player one
        messages = cast.get_actors("messages")

        # Displaying the snakes,food and messages
        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)

        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segmentsTwo)

        self._video_service.draw_actor(score)
        self._video_service.draw_actor(scoreTwo)
        self._video_service.draw_actor(GameInstructionDisplay)

        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()