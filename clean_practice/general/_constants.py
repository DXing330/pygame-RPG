
class Constants:
    def __init__(self):
        # Player Constants
        self.summoner_base_health = 10
        self.summoner_base_attack = 2
        self.summoner_base_defense = 1
        self.summoner_base_mana = 5
        self.summoner_base_skill = 5
        # Ally Constants
        self.angel_base_attack = 3
        # Monster Constants
        self.monster_base_attack = 4
        self.monster_base_defense = 2
        self.monster_base_health = 15
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
        self.ELEMENTAL_ADVANTAGE = 2


class Monster_Constants:
    def __init__(self):
        self.monster_base_attack = 4
        self.monster_base_defense = 2
        self.monster_base_health = 15
        self.MONSTER_HEALTH_DICTIONARY = {
        "Werewolf" : 10, "Goblin" : 5
        }
        self.MONSTER_ATTACK_DICTIONARY = {
        "Werewolf" : 6, "Goblin" : 2
        }
        self.MONSTER_DEFENSE_DICTIONARY = {
        "Werewolf" : 2, "Goblin" : 1
        }
