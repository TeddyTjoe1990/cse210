import random

class Hider:
    def __init__(self):
        self._location = random.randint(1, 1000)
        self._distance = [0, 0] # start with two so get_hint always works
    
    def get_hint(self):
        hint = "(-.-) Nap time."
        if self._distance[-1] == 0:
            hint = "(;.;) You got me!"
        elif self._distance[-1] > self._distance[-2]:
            hint = "(^.^) Colder!"
        elif self._distance[-1] < self._distance[-2]:
            hint = "(>.<) Warmer!"
        return hint

    def is_found(self):
        return (self._distance[-1] == 0)
        
    def watch_seeker(self, seeker):
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)