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
        self.SUMMONER_SKILLS = {
        0 : Skill_PC("Command Ally", 1, "Command", "Command", "Summon", -1),
        2 : Skill_PC("Enchance Ally", 1, "Change_Stats", "Attack", "Summon", 3),
        4 : Skill_PC("Summon Golem", 1, "Summon", "Golem", "None", 10)
        }
        self.CLERIC_SKILLS = {
        0 : Skill_PC("Heal", 1, "Change_Stats", "Health", "Ally", -1),
        2 : Skill_PC("Mass_Heal", 1, "Change_Stats", "Health", "All_Ally", 2),
        4 : Skill_PC("Cure", 1, "Cure_Status", "Cure_Status", "Ally", 2),
        6 : Skill_PC("Bless", 1, "Add_Buff", "Bless", "Ally", 5),
        8 : Skill_PC("Weaken", -1, "Change_Stats", "Attack", "Enemy", 5)
        }
        self.SUMMONER_SPELLS = {
        1 : Spell_PC("Fire", 1, Elements_NPC("Fire", "Air", "Water"), "Inflict_Status", "Burn", "All_Enemy", 1),
        3 : Spell_PC("Fire Ball", 3, Elements_NPC("Fire", "Air", "Water"), "Inflict_Status", "Burn", "All_Enemy", 5)
        }
        self.CLERIC_SPELLS = {
        1 : Spell_PC("Light", 1, Elements_NPC("Light", "Dark", "None"), "None", "None", "All_Enemy", 5)
        }
        self.HERO_SKILL_LIST = {
        "Summoner" : self.SUMMONER_SKILLS,
        "Cleric" : self.CLERIC_SKILLS
        }
        self.HERO_SPELL_LIST = {
        "Summoner" : self.SUMMONER_SPELLS,
        "Cleric" : self.CLERIC_SPELLS
        }
        
        
class Summon_Dictionary:
    def __init__(self):
        self.SUMMON_TYPE = {
        }
        self.SUMMON_BASE_HEALTH = {
        "Golem" : 5, "Wolf" : 5
        }
        self.SUMMON_BASE_ATTACK = {
        "Golem" : 3, "Wolf" : 4
        }
        self.SUMMON_BASE_DEFENSE = {
        "Golem" : 3, "Wolf" : 3
        }
        self.SUMMON_BASE_SKILL = {
        "Golem" : 0, "Wolf" : 2
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
        "Attack" : Skill_PC("Basic_Attack", 1, "Attack", "Basic", "Enemy", -1),
        "Double_Hit" : Skill_PC("Double_Hit", 2, "Attack", "Basic", "Enemy", 5),
        "Pierce_Defense" : Skill_PC("Pierce", 1, "Attack", "Ignore_Defense", "Enemy", 10),
        "Double_Pierce" : Skill_PC("Double_Pierce", 2, "Attack", "Ignore_Defense", "Enemy", 20),
        "Spinning_Slash" : Skill_PC("Spinning_Slash", 1, "Attack", "Basic", "All_Enemy", 10),
        "Howl" : Skill_PC("Howl", 1, "Add_Buff", "ATK+", "All_Ally", 10),
        "Howl_for_Help" : Skill_PC("Howl", 1, "Summon", "Wolf", "None", 10)
        }