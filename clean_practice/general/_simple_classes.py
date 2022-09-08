# _simple_classes are classes that have little to no methods by themselves

# Effects that do something without the player's input.
class Passive_Effect_NPC:
    def __init__(self, effect, effect_specifics, power, timing, variety):
        # What the effect does.
        self.effect = effect
        self.effect_specifics = effect_specifics
        # How strong the effect is.
        self.power = power
        # When it takes effect, ex. damage_step, every_turn, etc.
        self.timing = timing
        # What kind of passive it is, ex. buff, or status.
        self.variety = variety

    def add_power(self):
        self.power += 1


class Elements_NPC:
    def __init__(self, name, strength, weakness):
        self.name = name
        self.strength = strength
        self.weakness = weakness
        # Base effectiveness is 1, can go higher or lower depending on elemental advantage.
        self.effectiveness = 1



# Stores things that the heroes can use
class Item_Bag_PC:
    def __init__(self, coins, potions):
        self.coins = coins
        self.potions = potions



class Equipment_NPC:
    def __init__(self, power, effect: Passive_Effect_NPC, element: Elements_NPC, variety):
        self.power = power
        # What kind of effect the equipment has
        self.effect = effect
        self.element = element
        # What kind of equipment it is, ex. weapon, armor, acc.
        self.variety = variety

    def add_power(self):
        self.power += 1


# Spells are generally AOE effects that are cast by the player and cost mana.
class Spell_PC:
    def __init__(self, name, power, element: Elements_NPC, effect, effect_specifics, target, cost):
        self.name = name
        self.power = power
        self.element = element
        self.effect = effect
        self.effect_specifics = effect_specifics
        self.target = target
        self.cost = cost
        

# Skills are effects cast by the player, usually costing skill.
class Skill_PC:
    def __init__(self, name, effect, effect_specifics, target, cost):
        self.effect = effect
        self.effect_specifics = effect_specifics
        self.target = target
        self.cost = cost