from _basic_classes import Hero_PC

class Advanced_Hero(Hero_PC):
    def __init__(self, name, level, exp):
        self.name = name
        self.level = level
        self.exp = exp