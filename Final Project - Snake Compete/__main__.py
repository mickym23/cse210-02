import constants

from game.casting.cast import Cast
from game.casting.food import Food

from game.casting.score import Score
from game.casting.score_two import ScoreTwo
from game.casting.game_instructions_display import GameInstructionDisplay
from game.casting.help_guide import HelpGuide

from game.casting.snake import Snake
from game.casting.snake_two import SnakeTwo

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.control_actors_action_two import ControlActorsActionTwo

from game.scripting.move_actors_action import MoveActorsAction

from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.handle_help_guide import HandleHelpGuide
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())

    cast.add_actor("snakes", Snake())
    cast.add_actor("snakesTwo", SnakeTwo())
    
    cast.add_actor("scores", Score())
    cast.add_actor("scoresTwo", ScoreTwo())
    cast.add_actor("GameInstructionDisplay", GameInstructionDisplay())
    cast.add_actor("HelpGuide", HelpGuide())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("input", ControlActorsActionTwo(keyboard_service))
    script.add_action("input", HandleHelpGuide(keyboard_service, video_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()