class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service

        self._total_score = 0
        self._gain_or_loose_point_display = ""
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        banner.set_text("Total points are: " + str(self._total_score))

        # Displaying the gain point or loose point
        banner_gain_or_lose_display = cast.get_first_actor("points_banners")
        banner_gain_or_lose_display.set_text(self._gain_or_loose_point_display)

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)



        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                
                if(artifact.get_text() == "*"):
                    self._total_score = self._total_score + 1
                else:
                    self._total_score = self._total_score - 1

                display_score = self._total_score
                display_score_as_string = str(display_score)

                message = artifact.get_message()
                cast.remove_actor("artifacts", artifact)

                # To print gained or lost a point
                self._gain_or_loose_point_display = message
                banner.set_text(message)
                # banner.set_text(message + " .Total points are: " + str(self._total_score))

            current_artifact_position = artifact.get_position()
            artifact.position = artifact.falling_artifact(current_artifact_position)
            artifact.move_next(900, 600)
            




    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()