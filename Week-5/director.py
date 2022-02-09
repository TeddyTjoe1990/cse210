from term import TerminalService
from hider import Hider
from seeker import Seeker


class Director:
    
    def __init__(self):
        
        self._hider = Hider()
        self._is_playing = True
        self._seeker = Seeker()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        new_location = self._terminal_service.read_number("\nEnter a location [1-1000]: ")
        self._seeker.move_location(new_location)
        
    def _do_updates(self):
        self._hider.watch_seeker(self._seeker)
        
    def _do_outputs(self):
        hint = self._hider.get_hint()
        self._terminal_service.write_text(hint)
        if self._hider.is_found():
            self._is_playing = False