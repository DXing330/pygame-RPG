
class Constants:
    def __init__(self):
        # Player Constants

        # Ally Constants
        self.ANGEL_BASE_ATTACK = 3
        self.ANGEL_BUFF_LIST = ["HP+", "ATK+"]
        # Pygame Constants
        self.SLOW_FPS = 10
        self.FPS = 30
        self.FAST_FPS = 60
        self.WIDTH = 1400
        self.HEIGHT = 600
        self.PADDING = 25
        self.PLAYER_SIZE = 50
        self.MONSTER_SIZE = 60
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        # General Gameplay Constants
        self.INCREASE_EXPONENT = 2
        self.DECREASE_EXPONENT = 0.5
        self.LARGE_DECREASE_EXPONENT = 0.25
        self.ELEMENTAL_ADVANTAGE = 2
