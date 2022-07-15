from game.scripting.action import Action

class HandleHelpGuide(Action):
    """
    The HandleHelpGuide class handles the input of the user when they hold down the 'H' key 
    to display the help menu that explains the controls and the purpose of the game.

    """

    def __init__(self, keyboard_service, video_service):
        # instance of KeyboardService class
        self._keyboard_service = keyboard_service

        # instance of VideoService class
        self._video_service = video_service


        self._is_menu_open = False

    def execute(self, cast, script):

        # executes method call if the 'H' is held down and the menu is not open
        if self._keyboard_service.is_key_down('h') and self._is_menu_open == False:

            # draws a rectangle with the appropriate help menu information
            self._video_service.draw_rectangle_menu()
                