class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    """
    Game class stores events of entering or leaving creatures from the game.
    Also stores notifying events for other creatures about that.
    """
    def __init__(self):
        self.enters = Event()
        self.dies = Event()
        self.notify = Event()
