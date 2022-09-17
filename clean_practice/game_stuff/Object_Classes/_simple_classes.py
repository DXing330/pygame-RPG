# _simple_classes are classes that have little to no methods by themselves

# Effects that do something without the player's input.
class Passive_Effect_NPC:
    def __init__(self, name, effect, effect_specifics, power, timing, variety):
        self.name = name
        # What the effect does.
        self.effect = effect
        self.effect_specifics = effect_specifics
        # How strong the effect is.
        self.power = power
        # When it takes effect, ex. damage_step, every_turn, etc.
        self.timing = timing
        # What kind of passive it is, ex. buff, or status.
        self.variety = variety


class Elements_NPC:
    def __init__(self, name, strength, weakness):
        self.name = name
        self.strength = strength
        self.weakness = weakness


# Stores things that the heroes can use
class Item_Bag_PC:
    def __init__(self, coins, potions):
        self.coins = coins
        self.potions = potions
        

# Skills are effects cast by the player, usually costing skill.
class Skill_PC(object):
    def __init__(self, name, power, effect, effect_specifics,
    target, cost, cooldown = 0, cooldown_counter = 0):
        self.name = name
        self.power = power
        self.effect = effect
        self.effect_specifics = effect_specifics
        self.target = target
        self.cost = cost
        self.cooldown = cooldown
        self.cooldown_counter = cooldown_counter


# Spells are generally AOE effects that are cast by the player and cost mana.
class Spell_PC(Skill_PC):
    def __init__(self, name, power, element: Elements_NPC,
    effect, effect_specifics, target, cost, cooldown = 0, cooldown_counter = 0):
        self.name = name
        self.power = power
        self.element = element
        self.effect = effect
        self.effect_specifics = effect_specifics
        self.target = target
        self.cost = cost
        self.cooldown = cooldown
        self.cooldown_counter = cooldown_counter