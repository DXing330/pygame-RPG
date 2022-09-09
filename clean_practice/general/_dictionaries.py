from _simple_classes import *

class Dictionaries:
    def __init__(self):
        self.STATUSES = {
        "Burn" : Passive_Effect_NPC("Decrease_Stats", "Attack", 1, "Every_Turn", "Status"),
        "Bleed" : Passive_Effect_NPC("Decrease_Stats", "Health", 1, "Every_Turn", "Status"),
        "Corrode" : Passive_Effect_NPC("Decrease_Stats", "Defense", 1, "Every_Turn", "Status"),
        "Curse" : Passive_Effect_NPC("Decrease_Stats", "ALL", 1, "Every_Turn", "Status"),
        "Silence" : Passive_Effect_NPC("Disable", "Magic", 1, "Always", "Status"),
        "Forget" : Passive_Effect_NPC("Disable", "Skills", 1, "Always", "Status"),
        "Stun" : Passive_Effect_NPC("Disable", "ALL", 1, "Always", "Status")
        }
        self.BUFFS = {
        "Burner" : Passive_Effect_NPC("Inflict_Status", "Burn", 1, "Attack", "Buff"),
        "Bleeder" : Passive_Effect_NPC("Inflict_Status", "Bleed", 1, "Attack", "Buff"),
        "Corroder" : Passive_Effect_NPC("Inflict_Status", "Corrode", 1, "Attack", "Buff"),
        "HP+" : Passive_Effect_NPC("Increase_Stats", "Health", 1, "Every_Turn", "Buff"),
        "ATK+" : Passive_Effect_NPC("Increase_Stats", "Attack", 1, "Every_Turn", "Buff"),
        "DEF+" : Passive_Effect_NPC("Increase_Stats", "Defense", 1, "Every_Turn", "Buff"),
        "Bless" : Passive_Effect_NPC("Increase_Stats", "ALL", 1, "Every_Turn", "Buff")
        }
        self.STATUS_HEALTH = {
        "Health" : 1, "Attack" : 0, "Defense" : 0, "ALL" : 1
        }
        self.STATUS_ATTACK = {
        "Health" : 0, "Attack" : 1, "Defense" : 0, "ALL" : 1
        }
        self.STATUS_DEFENSE = {
        "Health" : 0, "Attack:" : 0, "Defense" : 1, "ALL" : 1
        }
        self.BUFF_HEALTH = {
        "Health" : 1, "Attack" : 0, "Defense" : 0, "ALL" : 1
        }
        self.BUFF_ATTACK = {
        "Health" : 0, "Attack" : 1, "Defense" : 0, "ALL+" : 1
        }
        self.BUFF_DEFENSE = {
        "Health" : 0, "Attack" : 0, "Defense" : 1, "ALL+" : 1
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
        self.SUMMONER_SKILLS = {
        0 : Skill_PC("Command Ally", 1, "Command", "Command", "Summoned_Ally", -1),
        2 : Skill_PC("Enchance Ally", 1, "Increase_Stats", "Attack", "Summoned_Ally", 3),
        4 : Skill_PC("Summon Golem", 1, "Summon", "Golem", "None", 10)
        }
        self.CLERIC_SKILLS = {
        0 : Skill_PC("Heal", 1, "Increase_Stats", "Health", "Ally", -1),
        2 : Skill_PC("Mass_Heal", 1, "Increase_Stats", "Health", "All_Ally", 2),
        4 : Skill_PC("Cure", 1, "Cure_Status", "Cure_Status", "Ally", 2),
        6 : Skill_PC("Bless", 1, "Add_Buff", "Bless", "Ally", 5)
        }
        self.SUMMONER_SPELLS = {
        1 : Spell_PC("Fire", 1, Elements_NPC("Fire", "Air", "Water"), "Inflict_Status", "Burn", "ALL_ENEMIES", 1),
        3 : Spell_PC("Fire Ball", 3, Elements_NPC("Fire", "Air", "Water"), "Inflict_Status", "Burn", "ALL_ENEMIES", 5)
        }
        self.HERO_SKILL_LIST = {
        "Summoner" : self.SUMMONER_SKILLS,
        "Cleric" : self.CLERIC_SKILLS
        }
        self.HERO_SPELL_LIST = {
        "Summoner" : self.SUMMONER_SPELLS
        }
        
        
class Summon_Dictionary:
    def __init__(self):
        self.SUMMON_TYPE = {
        }
        self.SUMMON_BASE_HEALTH = {
        "Golem" : 10
        }
        self.SUMMON_BASE_ATTACK = {
        "Golem" : 4
        }
        self.SUMMON_BASE_DEFENSE = {
        "Golem" : 4
        }