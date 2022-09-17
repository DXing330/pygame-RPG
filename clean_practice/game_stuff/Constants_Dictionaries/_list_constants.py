from _simple_classes import *

class LConstants:
    def __init__(self):
        self.MONSTER_TYPES = ["Werewolf", "Goblin"]
        self.ELEMENTS = [Elements_NPC("Fire", "Air", "Water"),
        Elements_NPC("Water", "Fire", "Earth"),
        Elements_NPC("Earth", "Water", "Air"),
        Elements_NPC("Air", "Earth", "Fire"),
        Elements_NPC("Dark", "Dark", "Light")]