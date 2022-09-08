import json
from _constants import Constants
C = Constants
from _basic_classes import *
from ally_classes import *


class Save_Functions:
    def __init__(self):
        self.party = Party_PC()

    def add_party(self, party: Party_PC):
        self.party = party

    def write_object(self, object, filename):
        jsonP = json.dumps(object.__dict__)
        outfile = open(filename, "w")
        outfile.write(jsonP)
        outfile.flush
        outfile.close

    def write_object_list(self, list, filename):
        jsonP = json.dumps([object.__dict__ for object in list])
        outfile = open(filename, "w")
        outfile.write(jsonP)
        outfile.flush
        outfile.close

    def save(self):
        self.write_object_list(self.party.heroes, "heroes")
        self.write_object_list(self.party.allies, "allies")
        self.write_object_list(self.party.equipment, "equipment")
        self.write_object(self.party.items, "items")

    def read_hero_objects(self, filename):
        load_heroes_list = []
        jsonFile = open(filename, "r")
        heroes_list = json.load(jsonFile)
        for character in heroes_list:
            hero = Hero_PC(**character)
            load_heroes_list.append(hero)
        return load_heroes_list

    def read_ally_objects(self, filename):
        load_allies_list = []
        jsonFile = open(filename, "r")
        allies_list = json.load(jsonFile)
        for summon in allies_list:
            ally = Angel_NPC(**summon)
            load_allies_list.append(ally)
        return load_allies_list

    def read_equipment_objects(self, filename):
        load_equip_list = []
        jsonFile = open(filename, "r")
        equip_list = json.load(jsonFile)
        for equip in equip_list:
            equipment = Equipment_NPC(**equip)
            load_equip_list.append(equipment)
        return load_equip_list

    def load(self):
        heroes_list = self.read_hero_objects("heroes")
        self.party.heroes = heroes_list
        ally_list = self.read_ally_objects("allies")
        self.party.allies = ally_list
        equipment_list = self.read_equipment_objects("equipment")
        self.party.equipment = equipment_list
        jsonFile = open("items", "r")
        item_bag = json.load(jsonFile)
        item_bag_object = Item_Bag_PC(**item_bag)
        self.party.items = item_bag_object