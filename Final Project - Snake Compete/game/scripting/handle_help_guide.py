from game.scripting.action import Action

class HandleHelpGuide(Action):

    def __init__(self, keyboard_service, video_service):
         self._keyboard_service = keyboard_service
         self._video_service = video_service
         self._is_menu_open = False

    def execute(self, cast, script):
        if self._keyboard_service.is_key_down('h') and self._is_menu_open == False:
            self._video_service.draw_rectangle_menu()
                