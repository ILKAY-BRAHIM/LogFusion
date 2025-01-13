import itertools
import os

class Spinner:
    def __init__(self):
        if os.name == 'nt':
            self.frames = [
                "- ", "\\ ", "| ", "/ "
            ]
        else:
            self.frames = [
                "⠋ ", "⠙ ", "⠹ ", "⠸ ", "⠼ ", "⠴ ", "⠦ ", "⠧ ", "⠇ ", "⠏ "
            ]
        self.cycle = itertools.cycle(self.frames)

    def next_frame(self):
        return next(self.cycle)
    def get_first_frame(self):
        return self.frames[0]