from _simple_classes import Passive_Effect_NPC, Skill_PC

class Dictionaries:
    def __init__(self):
        self.STATUSES = {
        "Burn" : Passive_Effect_NPC("Burn", "Burn", 1, "every_turn", "Status"),
        "Bleed" : Passive_Effect_NPC("Bleed", "Bleed", 1, "every_turn", "Status"),
        "Corrode" : Passive_Effect_NPC("Corrode", "Corrode", 1, "every_turn", "Status")
        }
        self.BUFFS = {
        "Burner" : Passive_Effect_NPC("Inflict_Status", "Burn", 1, "Attack", "Buff"),
        "Bleeder" : Passive_Effect_NPC("Inflict_Status", "Bleed", 1, "Attack", "Buff")
        }
        self.STATUS_HEALTH = {
        "Bleed" : 1, "Burn" : 0, "Corrode" : 0
        }
        self.STATUS_ATTACK = {
        "Bleed" : 0, "Burn" : 1, "Corrode" : 0
        }
        self.STATUS_DEFENSE = {
        "Bleed" : 0, "Burn:" : 0, "Corrode" : 1
        }
        self.BUFF_HEALTH = {
        "HP+" : 1, "ATK+" : 0, "DEF+" : 0, "ALL+" : 1
        }
        self.BUFF_ATTACK = {
        "HP+" : 0, "ATK+" : 1, "DEF+" : 0, "ALL+" : 1
        }
        self.BUFF_DEFENSE = {
        "HP+" : 0, "ATK+" : 0, "DEF+" : 1, "ALL+" : 1
        }
        self.HERO_BASE_HEALTH = {
        "Summoner" : 10, "Warrior" : 15, "Mage" : 10, "Cleric" : 15,
        "Knight" : 20, "Ninja" : 10, "Tactician" : 10, "Hunter" : 15, "Hero" : 15
        }
        self.HERO_BASE_ATTACK = {
        "Summoner" : 3, "Warrior" : 5, "Mage" : 3, "Cleric" : 4,
        "Knight" : 4, "Ninja" : 3, "Tactician" : 3, "Hunter" : 4, "Hero" : 5
        }
        self.HERO_BASE_DEFENSE = {
        "Summoner" : 2, "Warrior" : 3, "Mage" : 2, "Cleric" : 3,
        "Knight" : 4, "Ninja" : 2, "Tactician" : 2, "Hunter" : 3, "Hero" : 3
        }
        self.HERO_BASE_MANA = {
        "Summoner" : 5, "Warrior" : 0, "Mage" : 10, "Cleric" : 5,
        "Knight" : 0, "Ninja" : 0, "Tactician" : 0, "Hunter" : 0, "Hero" : 5
        }
        self.HERO_BASE_SKILL = {
        "Summoner" : 5, "Warrior" : 5, "Mage" : 5, "Cleric" : 5,
        "Knight" : 5, "Ninja" : 10, "Tactician" : 10, "Hunter" : 10, "Hero" : 5
        }
        self.SUMMONS = {
        
        }
        self.SUMMONER_SKILLS = {
        0 : Skill_PC("Command Ally", "Command", "Command", "Ally", -1),
        2 : Skill_PC("Enchance Ally", "Buff", "Attack", "Ally", 5),
        4 : Skill_PC("Summon Golem", "Summon", "Golem", "Hero_Party", 10)
        }
        self.HERO_SKILL_LIST = {
        "Summoner" : self.SUMMONER_SKILLS
        }