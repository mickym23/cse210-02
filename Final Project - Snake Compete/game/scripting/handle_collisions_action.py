from distutils.util import check_environ
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over_player_one_lose_default = False
        self._is_game_over = False
        
        self._is_game_over_player_two_lose_default = False
        self._is_game_over_two = False
        

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            # self._handle_segment_collision(cast)
            self._handle_snake_collision(cast)
            self._handle_game_over(cast)
            self._handle_game_over_two(cast)
            self._handle_game_over_three(cast)
            self._handle_game_over_four(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        checker_value = 15

        score = cast.get_first_actor("scores")
        scoreTwo = cast.get_first_actor("scoresTwo")

        # if score.get_points > checker_value or scoreTwo.get_points > checker_value:
        #     self._is_game_over = True

        food = cast.get_first_actor("foods")

        snake = cast.get_first_actor("snakes")
        head = snake.get_head()

        snakeTwo = cast.get_first_actor("snakesTwo")
        headTwo = snakeTwo.get_head()

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()

        if headTwo.get_position().equals(food.get_position()):
            points = food.get_points()
            snakeTwo.grow_tail(points)
            scoreTwo.add_points(points)
            food.reset()

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]

        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True

    def _handle_snake_collision(self, cast):
        """Sets the game over flag if the snake collides with the other snake.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        scoreTwo = cast.get_first_actor("scoresTwo")
        # checkerOne = scoreTwo.get_points()
        # checkerTwo = scoreTwo.get_points()

        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]

        snake2 = cast.get_first_actor("snakesTwo")
        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]

        for segment in segments2:
            if head.get_position().equals(segment.get_position()) and score.get_points() < 25:
                self._is_game_over_player_one_lose_default = True

        for segment in segments2:
            if head.get_position().equals(segment.get_position()) and score.get_points() >= 25:
                self._is_game_over = True

        for segment in segments:
            if head2.get_position().equals(segment.get_position()) and scoreTwo.get_points() < 25:
                self._is_game_over_player_two_lose_default = True

        for segment in segments:
            if head2.get_position().equals(segment.get_position()) and scoreTwo.get_points() >= 25:
                self._is_game_over_two = True

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over_player_one_lose_default:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(160)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over! -- Player 2 Wins!! -- ")
            message.set_position(position)
            message.set_font_size(20)
            cast.add_actor("messages", message)
    

            for segment in segments:
                segment.set_color(constants.WHITE)

            food.set_color(constants.WHITE)

    def _handle_game_over_two(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(160)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over! -- Player 1 Wins!! -- ")
            message.set_position(position)
            message.set_font_size(20)
            cast.add_actor("messages", message)


            for segment in segments:
                segment.set_color(constants.WHITE)

            food.set_color(constants.WHITE)

    def _handle_game_over_three(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over_player_two_lose_default:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(160)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over! -- Player 1 Wins!! -- ")
            message.set_position(position)
            message.set_font_size(20)
            cast.add_actor("messages", message)
           

            for segment in segments:
                segment.set_color(constants.WHITE)

            food.set_color(constants.WHITE)

    def _handle_game_over_four(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over_two:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(160)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over! -- Player 2 Wins!! -- ")
            message.set_position(position)
            message.set_font_size(20)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)

            food.set_color(constants.WHITE)

    
