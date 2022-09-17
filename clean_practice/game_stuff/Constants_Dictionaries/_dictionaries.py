import sys
sys.path.append("./Object_Classes")
from _simple_classes import *

class Dictionaries:
    def __init__(self):
        self.ELEMENTS = {
        "Fire" : Elements_NPC("Fire", "Air", "Water"),
        "Water" : Elements_NPC("Water", "Fire", "Earth"),
        "Earth" : Elements_NPC("Earth", "Water", "Air"),
        "Air" : Elements_NPC("Air", "Earth", "Fire"),
        "Dark" : Elements_NPC("Dark", "None", "Light"),
        "Light" : Elements_NPC("Light", "Dark", "None")
        }
        self.WEAPON_EFFECTS = {
        "Slay_Fire" : Passive_Effect_NPC("Slay_Fire", "Slay", "Fire",
        2, "Attack", "Buff")
        }
        self.ARMOR_EFFECTS = {
        "Absorb_Fire" : Passive_Effect_NPC("Absorb_Fire", "Absorb", "Fire",
        1, "Defense", "Buff")
        }
        self.ACCESSORY_EFFECTS = {
        
        }
        self.EQUIPMENT_EFFECTS = {
        "Weapon" : self.WEAPON_EFFECTS,
        "Armor" : self.ARMOR_EFFECTS
        }
        self.STATUSES = {
        "Burn" : Passive_Effect_NPC("Burn", "Change_Stats", "Attack", -1, "Every_Turn", "Status"),
        "Bleed" : Passive_Effect_NPC("Bleed", "Change_Stats", "Health", -5, "Every_Turn", "Status"),
        "Corrode" : Passive_Effect_NPC("Corrode", "Change_Stats", "Defense", -1, "Every_Turn", "Status"),
        "Curse" : Passive_Effect_NPC("Curse", "Change_Stats", "ALL", 1, "Every_Turn", "Status"),
        "Silence" : Passive_Effect_NPC("Silence", "Disable", "Magic", 9, "Always", "Status"),
        "Forget" : Passive_Effect_NPC("Forget", "Disable", "Skills", 9, "Always", "Status"),
        "Stun" : Passive_Effect_NPC("Stun", "Disable", "ALL", 1, "Always", "Status")
        }
        self.BUFFS = {
        "Burner" : Passive_Effect_NPC("Burner", "Inflict_Status", "Burn", 1, "Attack", "Buff"),
        "Bleeder" : Passive_Effect_NPC("Bleeder", "Inflict_Status", "Bleed", 1, "Attack", "Buff"),
        "Corroder" : Passive_Effect_NPC("Corroder", "Inflict_Status", "Corrode", 1, "Attack", "Buff"),
        "HP+" : Passive_Effect_NPC("HP+", "Change_Stats", "Health", 5, "Every_Turn", "Buff"),
        "ATK+" : Passive_Effect_NPC("ATK+", "Change_Stats", "Attack", 1, "Every_Turn", "Buff"),
        "DEF+" : Passive_Effect_NPC("DEF+", "Change_Stats", "Defense", 1, "Every_Turn", "Buff"),
        "Bless" : Passive_Effect_NPC("Bless", "Change_Stats", "ALL", 1, "Every_Turn", "Buff"),
        "Block" : Passive_Effect_NPC("Block", "Decrease_Attack", "Flat", 1, "Defense", "Buff"),
        "Thorns" : Passive_Effect_NPC("Thorns", "Change_Stats", "Health", -1, "Defense", "Buff")
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
        "Health" : 0, "Attack" : 1, "Defense" : 0, "ALL" : 1
        }
        self.BUFF_DEFENSE = {
        "Health" : 0, "Attack" : 0, "Defense" : 1, "ALL" : 1
        }


class Hero_Dictionary:
    def __init__(self):
        self.HERO_BASE_HEALTH = {
        "Summoner" : 10, "Warrior" : 15, "Mage" : 10, "Cleric" : 15,
        "Knight" : 20, "Ninja" : 10, "Tactician" : 10, "Hunter" : 15, "Hero" : 15
        }
        self.HERO_BASE_ATTACK = {
        "Summoner" : 2, "Warrior" : 4, "Mage" : 2, "Cleric" : 3,
        "Knight" : 3, "Ninja" : 2, "Tactician" : 2, "Hunter" : 3, "Hero" : 4
        }
        self.HERO_BASE_DEFENSE = {
        "Summoner" : 1, "Warrior" : 2, "Mage" : 1, "Cleric" : 2,
        "Knight" : 3, "Ninja" : 1, "Tactician" : 1, "Hunter" : 2, "Hero" : 2
        }
        self.HERO_BASE_MANA = {
        "Summoner" : 3, "Warrior" : 0, "Mage" : 5, "Cleric" : 3,
        "Knight" : 0, "Ninja" : 0, "Tactician" : 0, "Hunter" : 0, "Hero" : 3
        }
        self.HERO_BASE_SKILL = {
        "Summoner" : 3, "Warrior" : 3, "Mage" : 3, "Cleric" : 3,
        "Knight" : 3, "Ninja" : 5, "Tactician" : 5, "Hunter" : 5, "Hero" : 3
        }
        self.ALL_SKILLS = {
        "Heal Self" : Skill_PC("Heal", 1, "Change_Stats", "Health", "Self", 0),
        "Basic Attack" : Skill_PC("Attack", 1, "Attack", "Basic", "Enemy", -1),
        "Command" : Skill_PC("Command Ally", 1, "Command", "Command", "Summon", -1),
        "Command+Attack" : Skill_PC("Command+Attack", 1, "Skill", "Command_Attack", "None", 2),
        "Regenerate" : Skill_PC("Regenerate", 1, "Add_Buff", "HP+", "Ally", 0),
        "Burn" : Skill_PC("Burn", 1, "Inflict_Status", "Burn", "Enemy", 0),
        "Cleanse" : Skill_PC("Cleanse", 1, "Cure_Status", "Cure_Status", "Ally", 0),
        "Golem" : Skill_PC("Summon Golem", 1, "Summon", "Golem", "None", 10, 0, 2),
        "Command+Golem" : Skill_PC("Command+Golem", 1, "Skill", "Command_Golem", "None", 15, 0, 2),
        "Double Command" : Skill_PC("Double Command", 2, "Command", "Command", "Summon", 5),
        "Double Golems" : Skill_PC("Double Golems", 2, "Summon", "Golem", "None", 20, 0, 3),
        "Golem Lord" : Skill_PC("Golem Lord", 1, "Summon", "Golem_Lord", "None", 30, 2, 2),
        "Heal Ally" : Skill_PC("Heal", 1, "Change_Stats", "Health", "Ally", -1),
        "Mass Heal" : Skill_PC("Mass Heal", 1, "Change_Stats", "Health", "All_Ally", 2),
        "Cure" : Skill_PC("Cure", 1, "Cure_Status", "Cure_Status", "Ally", 2),
        "Bless" : Skill_PC("Bless", 1, "Add_Buff", "Bless", "Ally", 5, 0, 2),
        "Weaken" : Skill_PC("Weaken", -1, "Change_Stats", "Attack", "Enemy", 5, 0, 2)
        }
        self.SUMMONER_SKILLS = {
        0 : "Command", 2 : "Command+Attack", 4 : "Golem", 6 : "Double Command",
        8 : "Command+Golem", 10 : "Double Golems", 12 : "Golem Lord"
        }
        self.CLERIC_SKILLS = {
        0 : "Heal Ally", 2 : "Mass Heal", 4 : "Cure", 6 : "Bless",
        8 : "Weaken"
        }
        self.WARRIOR_SKILLS = {
        0 : Skill_PC("Double Swing", 2, "Attack", "Basic", "Enemy", -1),
        2 : Skill_PC("Pierce", 1, "Attack", "Ignore_Defense", "Enemy", 2),
        4 : Skill_PC("Healing Strike", 1, "Skill", "Healing_Strike", "None", 2),
        6 : Skill_PC("Triple Swing", 3, "Attack", "Basic", "Enemy", 4, 0, 2)
        }
        self.SUMMONER_SPELLS = {
        1 : Spell_PC("Fire", 1, Elements_NPC("Fire", "Air", "Water"),
        "Inflict_Status", "Burn", "All_Enemy", 1),
        3 : Spell_PC("Fire Ball", 3, Elements_NPC("Fire", "Air", "Water"),
        "Inflict_Status", "Burn", "All_Enemy", 5)
        }
        self.CLERIC_SPELLS = {
        1 : Spell_PC("Light", 1, Elements_NPC("Light", "Dark", "None"),
        "None", "None", "All_Enemy", 5)
        }
        self.HERO_SKILL_LIST = {
        "Summoner" : self.SUMMONER_SKILLS,
        "Cleric" : self.CLERIC_SKILLS,
        "Warrior" : self.WARRIOR_SKILLS
        }
        self.HERO_SPELL_LIST = {
        "Summoner" : self.SUMMONER_SPELLS,
        "Cleric" : self.CLERIC_SPELLS
        }
        self.COMPOUND_SKILLS = {
        "Command_Attack" : ["Command", "Attack"],
        "Healing_Strike" : ["Heal", "Attack"],
        "Command_Golem" : ["Command", "Golem"]
        }


class Ally_Dictionary:
    def __init__(self):
        self.ANGEL_SKILLS = {
        0 : Skill_PC("Heal", 1, "Change_Stats", "Health", "Ally", 0),
        2 : Skill_PC("Attack", -1, "Change_Stats", "Health", "Enemy", 0),
        4 : Skill_PC("Regenerate", 1, "Add_Buff", "HP+", "Ally", 0),
        6 : Skill_PC("Strengthen", 1, "Add_Buff", "ATK+", "Ally", 0),
        8 : Skill_PC("Cleanse", 1, "Cure_Status", "None", "Ally", 0),
        10 : Skill_PC("Blessed Light", 1, "Change_Stats", "Health", "All_Ally", 0),
        12 : Skill_PC("Holy Rays", 1, "Change_Stats", "Health", "All_Enemy", 0),
        14 : Skill_PC("Holy Fire", 1, "Inflict_Status", "Burn", "Enemy", 0)
        }
        self.WICKED_SKILLS = {
        0 : Skill_PC("Curse", -2, "Change_Stats", "Health", "Enemy", 0),
        2 : Skill_PC("Curse", -1, "Change_Stats", "Health", "Ally", 0),
        4 : Skill_PC("Curse", -2, "Change_Stats", "Attack", "Enemy", 0),
        6 : Skill_PC("Curse", -1, "Change_Stats", "Attack", "Ally", 0),
        8 : Skill_PC("Curse", -2, "Change_Stats", "Defense", "Enemy", 0),
        10 : Skill_PC("Curse", -1, "Change_Stats", "Defense", "Ally", 0),
        12 : Skill_PC("Curse", 2, "Inflict_Status", "Curse", "Enemy", 0),
        14 : Skill_PC("Curse", 1, "Inflict_Status", "Curse", "Ally", 0)
        }
        self.SKILL_LISTS = {
        "Angel" : self.ANGEL_SKILLS,
        "Wicked Angel" : self.WICKED_SKILLS
        }
        
        
class Summon_Dictionary:
    def __init__(self):
        self.SUMMON_TYPE = {
        }
        self.SUMMON_SKILLS = {
        "Golem_Lord" : ["Golem"]
        }
        self.SUMMON_BASE_HEALTH = {
        "Golem" : 5, "Wolf" : 5, "Golem_Lord" : 10
        }
        self.SUMMON_BASE_ATTACK = {
        "Golem" : 3, "Wolf" : 4, "Golem_Lord" : 5
        }
        self.SUMMON_BASE_DEFENSE = {
        "Golem" : 3, "Wolf" : 3, "Golem_Lord" : 5
        }
        self.SUMMON_BASE_SKILL = {
        "Golem" : 0, "Wolf" : 2, "Golem_Lord" : 3
        }


class Monster_Dictionary:
    def __init__(self):
        self.MONSTER_HEALTH = {
        "Werewolf" : 10, "Goblin" : 5
        }
        self.MONSTER_ATTACK = {
        "Werewolf" : 5, "Goblin" : 2
        }
        self.MONSTER_DEFENSE = {
        "Werewolf" : 1, "Goblin" : 1
        }
        self.MONSTER_SKILL_POINTS = {
        "Werewolf" : 2, "Goblin" : 2
        }
        self.MONSTER_SKILL_LISTS = {
        "Werewolf" : ["Attack", "Double_Hit", "Pierce_Defense", "Howl"]
        }
        self.MONSTER_BUFFS = {
        
        }
        self.MONSTER_SKILLS = {
        "Attack" : Skill_PC("Basic Attack", 1, "Attack", "Basic", "Enemy", -1),
        "Double_Hit" : Skill_PC("Double Hit", 2, "Attack", "Basic", "Enemy", 5),
        "Pierce_Defense" : Skill_PC("Pierce", 1, "Attack", "Ignore_Defense", "Enemy", 10),
        "Double_Pierce" : Skill_PC("Double Pierce", 2, "Attack", "Ignore_Defense", "Enemy", 20),
        "Spinning_Slash" : Skill_PC("Spinning Slash", 1, "Attack", "Basic", "All_Enemy", 10),
        "Howl" : Skill_PC("Howl", 1, "Add_Buff", "ATK+", "All_Ally", 10),
        "Howl_for_Help" : Skill_PC("Howl", 1, "Summon", "Wolf", "None", 10)
        }