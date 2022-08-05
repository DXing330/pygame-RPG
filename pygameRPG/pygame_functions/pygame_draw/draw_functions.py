import pygame
import os
import sys
sys.path.append("../..")
sys.path.append("../../Assets")
from pygconstants import PYGConstants
P = PYGConstants()
from rpg2_constants import Constants
C = Constants()
REG_FONT = pygame.font.SysFont("comicsans", 20)
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
width, height = WIN.get_size()
#images used
PLAINS_RAW = pygame.image.load(os.path.join("Assets", "plains.png"))
PLAINS_IMG = pygame.transform.scale(PLAINS_RAW, (width, height))
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (width, height))
CITY_RAW = pygame.image.load(os.path.join("Assets", "city.png"))
CITY_IMG = pygame.transform.scale(CITY_RAW, (width, height))
CLERIC_RAW = pygame.image.load(os.path.join("Assets", "cleric.png"))
CLERIC_IMG = pygame.transform.scale(CLERIC_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
MAGE_RAW = pygame.image.load(os.path.join("Assets", "mage.png"))
MAGE_IMG = pygame.transform.scale(MAGE_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
NINJA_RAW = pygame.image.load(os.path.join("Assets", "ninja.png"))
NINJA_IMG = pygame.transform.scale(NINJA_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
WARRIOR_RAW = pygame.image.load(os.path.join("Assets", "warrior.png"))
WARRIOR_IMG = pygame.transform.scale(WARRIOR_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
TACTICIAN_RAW = pygame.image.load(os.path.join("Assets", "tactician.png"))
TACTICIAN_IMG = pygame.transform.scale(TACTICIAN_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
TOTEM_RAW = pygame.image.load(os.path.join("Assets", "totem.png"))
TOTEM_IMG = pygame.transform.scale(TOTEM_RAW, (P.SMALL_SPRITE//2, P.SMALL_SPRITE//2))
BOMB_RAW = pygame.image.load(os.path.join("Assets", "bomb.png"))
BOMB_IMG = pygame.transform.scale(BOMB_RAW, (P.SMALL_SPRITE//2, P.SMALL_SPRITE//2))
HERO_RAW = pygame.image.load(os.path.join("Assets", "hero.png"))
HERO_IMG = pygame.transform.scale(HERO_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SUMMONER_RAW = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER_IMG = pygame.transform.scale(SUMMONER_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
KNIGHT_RAW = pygame.image.load(os.path.join("Assets", "knight.png"))
KNIGHT_IMG = pygame.transform.scale(KNIGHT_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
HUNTER_RAW =pygame.image.load(os.path.join("Assets", "hunter.png"))
HUNTER_IMG = pygame.transform.scale(HUNTER_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
ANGEL_RAW = pygame.image.load(os.path.join("Assets", "angel.png"))
ANGEL_IMG = pygame.transform.scale(ANGEL_RAW, (P.SPRITE_WIDTH//2, P.SPRITE_HEIGHT//2))
GUARDIAN_RAW = pygame.image.load(os.path.join("Assets", "chimera.png"))
GUARDIAN_IMG = pygame.transform.scale(GUARDIAN_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
MON_RAW = pygame.image.load(os.path.join("Assets", "g_mon.png"))
MON_IMG = pygame.transform.scale(MON_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SLIME_RAW = pygame.image.load(os.path.join("Assets", "slime.png"))
SLIME_IMG = pygame.transform.scale(SLIME_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
BEAST_RAW = pygame.image.load(os.path.join("Assets", "beast.png"))
BEAST_IMG = pygame.transform.scale(BEAST_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
GOBLIN_RAW = pygame.image.load(os.path.join("Assets", "goblin.png"))
GOBLIN_IMG = pygame.transform.scale(GOBLIN_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
ELEMENTAL_RAW = pygame.image.load(os.path.join("Assets", "elemental.png"))
ELEMENTAL_IMG = pygame.transform.scale(ELEMENTAL_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
DEMON_RAW = pygame.image.load(os.path.join("Assets", "demon.png"))
DEMON_IMG = pygame.transform.scale(DEMON_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SKELETON_RAW = pygame.image.load(os.path.join("Assets", "skeleton.png"))
SKELETON_IMG = pygame.transform.scale(SKELETON_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
TROLL_RAW = pygame.image.load(os.path.join("Assets", "troll.png"))
TROLL_IMG = pygame.transform.scale(TROLL_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
#function that will draw characters in battle
def draw_heroes(h_p, h_ally):
	width, height = WIN.get_size()
	x = 1
	y = 2
	z = 2
	for player in h_p:
		if "Hunter" in player.name:
			WIN.blit(HUNTER_IMG,
				 (width - (P.SPRITE_WIDTH * x),
				 height - (P.BIG_SPRITE * y)))
		if "Hero" in player.name:
			WIN.blit(HERO_IMG,
				 (width - (P.SPRITE_WIDTH * x),
				 height - (P.BIG_SPRITE * y)))
		if "Summoner" in player.name:
			WIN.blit(SUMMONER_IMG,
				 (width - (P.SPRITE_WIDTH * x),
				 height - (P.BIG_SPRITE * y)))
		if "Knight" in player.name:
			WIN.blit(KNIGHT_IMG,
				 (width - (P.SPRITE_WIDTH * x),
				 height - (P.BIG_SPRITE * y)))
		if "Defender" in player.name:
			WIN.blit(KNIGHT_IMG,
				 (width//2 + P.SPRITE_WIDTH,
				  height//2))
		if "Cleric" in player.name:
			WIN.blit(CLERIC_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.BIG_SPRITE * y)))
		if "Mage" in player.name:
			WIN.blit(MAGE_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.BIG_SPRITE * y)))
		if "Ninja" in player.name:
			WIN.blit(NINJA_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.BIG_SPRITE * y)))
		if "Warrior" in player.name:
			WIN.blit(WARRIOR_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.BIG_SPRITE * y)))
		if "Tactician" in player.name:
			WIN.blit(TACTICIAN_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.BIG_SPRITE * y)))
		if "Totem" in player.name:
			WIN.blit(TOTEM_IMG, (width//2 + (P.SPRITE_HEIGHT), height - (P.SPRITE_HEIGHT * x)))
		x += 0.2
		y += 1
		
	for ally in h_ally:
		if "Angel" in ally.name:
			WIN.blit(ANGEL_IMG,
				 (width - (P.SPRITE_WIDTH * 1),
				 height//3))
		if "Spirit" in ally.name:
			WIN.blit(GUARDIAN_IMG,
				 (width//2 + (P.SPRITE_WIDTH * 2),
				 height//2 + (P.SPRITE_HEIGHT * 2)))

	pygame.display.update()
#draws only the heroes
def draw_just_hero(h_p):
	width, height = WIN.get_size()
	x = 1
	y = 2
	for player in h_p:
		if "Hunter" in player.name:
			WIN.blit(HUNTER_IMG,
				 (width - (P.SPRITE_WIDTH * x),
				 height - (P.SPRITE_HEIGHT * y)))
		if "Hero" in player.name:
			WIN.blit(HERO_IMG,
				 (width - (P.SPRITE_WIDTH * x),
				 height - (P.SPRITE_HEIGHT * y)))
		if "Summoner" in player.name:
			WIN.blit(SUMMONER_IMG,
				 (width - (P.SPRITE_WIDTH * x),
				 height - (P.SPRITE_HEIGHT * y)))
		if "Knight" in player.name:
			WIN.blit(KNIGHT_IMG,
				 (width - (P.SPRITE_WIDTH * x),
				 height - (P.SPRITE_HEIGHT * y)))
		if "Defender" in player.name:
			WIN.blit(KNIGHT_IMG,
				 (width//2 + P.SPRITE_WIDTH,
				  height//2))
		if "Cleric" in player.name:
			WIN.blit(CLERIC_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.SPRITE_HEIGHT * y)))
		if "Mage" in player.name:
			WIN.blit(MAGE_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.SPRITE_HEIGHT * y)))
		if "Ninja" in player.name:
			WIN.blit(NINJA_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.SPRITE_HEIGHT * y)))
		if "Warrior" in player.name:
			WIN.blit(WARRIOR_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.SPRITE_HEIGHT * y)))
		if "Tactician" in player.name:
			WIN.blit(TACTICIAN_IMG, (width - (P.SPRITE_HEIGHT * x), height - (P.SPRITE_HEIGHT * y)))
		x += 0.5
		y += 1
#draw a single hero
def draw_hero(hero):
	width, height = WIN.get_size()
	x, y = WIN.get_size()
	if "Hunter" in hero.name:
		WIN.blit(HUNTER_IMG, (x//2, y//2))
	elif "Hero" in hero.name:
		WIN.blit(HERO_IMG, (x//2, y//2))
	elif "Summoner" in hero.name:
		WIN.blit(SUMMONER_IMG, (x//2, y//2))
	elif "Knight" in hero.name:
		WIN.blit(KNIGHT_IMG, (x//2, y//2))
	elif "Defender" in hero.name:
		WIN.blit(KNIGHT_IMG, (x//2, y//2))
	elif "Cleric" in hero.name:
		WIN.blit(CLERIC_IMG, (x//2, y//2))
	elif "Mage" in hero.name:
		WIN.blit(MAGE_IMG, (x//2, y//2))
	elif "Ninja" in hero.name:
		WIN.blit(NINJA_IMG, (x//4, y//2))
	elif "Warrior" in hero.name:
		WIN.blit(WARRIOR_IMG, (x//2, y//2))
	elif "Tactician" in hero.name:
		WIN.blit(TACTICIAN_IMG, (x//2, y//2))
def draw_ally(ally):
	width, height = WIN.get_size()
	x, y = WIN.get_size()
	if "Spirit" in ally.name:
		WIN.blit(GUARDIAN_IMG, (x//2, y//2))
#function that will draw monster stats
def draw_monster_stats(m_p):
	width, height = WIN.get_size()
	x = 2
	for mon in m_p:
		if mon.buff == None:
			stats_text = REG_FONT.render((mon.name+" HP: "+str(mon.health)+
						      " ATK: "+str(mon.atk)+" DEF: "+str(mon.defense)+
						      " SKL: "+str(mon.skill)+" ELMT: "+mon.element+
						      " PSN: "+str(mon.poison)),
						     1, P.RED)
		elif mon.buff != None:
			stats_text = REG_FONT.render((mon.name+" HP: "+str(mon.health)+
						      " ATK: "+str(mon.atk)+" DEF: "+str(mon.defense)+
						      " SKL: "+str(mon.skill)+" ELMT: "+mon.element+
						      " BUFF: "+mon.buff+" PSN: "+str(mon.poison)),
						     1, P.RED)
		WIN.blit(stats_text, (P.PADDING, P.PADDING + stats_text.get_height() * x))
		pygame.display.update()
		x += 1
#hero stats
def draw_hero_stats(hero):
	width, height = WIN.get_size()
	hero_stat_text = REG_FONT.render("Hero: " + hero.name + " ATK: " + str(hero.atk)
					 + " ATKBONUS: " + str(hero.atkbonus)
					 , 1, P.RED)
	hero_def_stat = REG_FONT.render("HP: " + str(hero.health) + " MAX HP: " + str(hero.maxhealth) +
					" DEF: " + str(hero.defense) + (" DEFBONUS: ") + str(hero.defbonus),
					1, P.RED)
	hero_other_stat = REG_FONT.render("SKILL: " + str(hero.skill) + " MANA: " + str(hero.mana)
					  + " MAX MANA: " + str(hero.maxmana),
					  1, P.RED)
	WIN.blit(hero_stat_text, (width - hero_stat_text.get_width() - P.PADDING,
					  P.PADDING + hero_stat_text.get_height()))
	WIN.blit(hero_def_stat, (width - hero_def_stat.get_width() - P.PADDING,
				 P.PADDING + hero_def_stat.get_height() * 2))
	WIN.blit(hero_other_stat, (width - hero_other_stat.get_width() - P.PADDING,
				   P.PADDING + hero_other_stat.get_height() * 3))
	
def draw_all_stats(h_p, h_ally, h_wpn, h_amr):
	width, height = WIN.get_size()
	x = 1
	for hero in h_p:
		stat_text = REG_FONT.render("Hero: "+hero.name+" ATK: "+str(hero.atk+hero.atkbonus)+
					    " DEF: "+str(hero.defense+hero.defbonus)+" HP%: "+str((round(hero.health/hero.maxhealth, 2))*100)+
					    " MP: "+str(hero.mana)+" SKL: "+str(hero.skill)+" PSN: "+str(hero.poison), 1, P.RED)
		WIN.blit(stat_text, ((width - stat_text.get_width() - P.PADDING), P.PADDING * x))
		x +=1
	for ally in h_ally:
		stat_text = REG_FONT.render("Ally: "+ally.name+" ATK: "+str(ally.atk)+" STAGE: "+str(ally.stage), 1, P.RED)
		WIN.blit(stat_text, ((width - stat_text.get_width() - P.PADDING), P.PADDING * x))
		x +=1
	for wpn in h_wpn:
		if wpn.user != "None":
			stat_text = REG_FONT.render("User: "+wpn.user+" Effect: "+wpn.effect+" Strength: "+str(wpn.strength)+
						    " ATK: "+str(wpn.atk)+" Element: "+wpn.element, 1, P.RED)
			WIN.blit(stat_text, ((width - stat_text.get_width() - P.PADDING), P.PADDING * x))
			x += 1
	for amr in h_amr:
		if amr.user != "None":
			stat_text = REG_FONT.render("User: "+amr.user+" Effect: "+amr.effect+" Strength: "+str(amr.strength)+
						    " DEF: "+str(amr.defense)+" Element: "+amr.element, 1, P.RED)
			WIN.blit(stat_text, ((width - stat_text.get_width() - P.PADDING), P.PADDING * x))
			x += 1
#function that will draw monsters in battle
def draw_monsters(m_p):
	width, height = WIN.get_size()
	x = 2
	y = 0
	z = 1
	for mon in m_p:
		if "Slime" in mon.name:
			WIN.blit(SLIME_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Beast" in mon.name:
			WIN.blit(BEAST_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Bomb" in mon.name:
			WIN.blit(BOMB_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Goblin" in mon.name:
			if "Champion" in mon.name:
				GOBLIN_IMG = pygame.transform.scale(GOBLIN_RAW, (P.BIG_SPRITE, P.BIG_SPRITE))
			elif "Hob" in mon.name:
				GOBLIN_IMG = pygame.transform.scale(GOBLIN_RAW, (P.SPRITE_WIDTH, P.SPRITE_WIDTH))
			else:
				GOBLIN_IMG = pygame.transform.scale(GOBLIN_RAW, (P.SMALL_SPRITE, P.SMALL_SPRITE))
			WIN.blit(GOBLIN_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Elemental" in mon.name:
			WIN.blit(ELEMENTAL_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Demon" in mon.name:
			WIN.blit(DEMON_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Skeleton" in mon.name:
			WIN.blit(SKELETON_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		elif "Troll" in mon.name:
			WIN.blit(TROLL_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		else:
			WIN.blit(MON_IMG,
				 (P.PADDING//5 * x + (P.SPRITE_WIDTH//2 * y),
				  height - (P.BIG_SPRITE * x)))
		x += 1
		if x * P.BIG_SPRITE > height - P.PADDING:
			x = 1
			y += 1

#function that draws a single monster
def draw_monster(mon):
	width, height = WIN.get_size()
	x, y = WIN.get_size()
	if "Slime" in mon.name:
		WIN.blit(SLIME_IMG, (x//3, y//2))
	elif "Beast" in mon.name:
		WIN.blit(BEAST_IMG, (x//3, y//2))
	elif "Bomb" in mon.name:
		WIN.blit(BOMB_IMG, (x//3, y//2))
	elif "Elemental" in mon.name:
		WIN.blit(ELEMENTAL_IMG, (x//3, y//2))
	elif "Golbin" in mon.name:
		WIN.blit(GOBLIN_IMG, (x//3, y//2))
	elif "Demon" in mon.name:
		WIN.blit(DEMON_IMG, (x//3, y//2))
	elif "Skeleton" in mon.name:
		WIN.blit(SKELETON_IMG, (x//3, y//2))
	elif "Troll" in mon.name:
		WIN.blit(TROLL_IMG, (x//3, y//2))
	else:
		WIN.blit(MON_IMG, (x//3, y//2))
def draw_monster2(mon):
	width, height = WIN.get_size()
	x, y = WIN.get_size()
	if "Slime" in mon.name:
		WIN.blit(SLIME_IMG, (x//2, y//2))
	elif "Beast" in mon.name:
		WIN.blit(BEAST_IMG, (x//2, y//2))
	elif "Bomb" in mon.name:
		WIN.blit(BOMB_IMG, (x//2, y//2))
	elif "Elemental" in mon.name:
		WIN.blit(ELEMENTAL_IMG, (x//2, y//2))
	elif "Golbin" in mon.name:
		WIN.blit(GOBLIN_IMG, (x//2, y//2))
	elif "Demon" in mon.name:
		WIN.blit(DEMON_IMG, (x//2, y//2))
	elif "Skeleton" in mon.name:
		WIN.blit(SKELETON_IMG, (x//2, y//2))
	elif "Troll" in mon.name:
		WIN.blit(TROLL_IMG, (x//2, y//2))
	else:
		WIN.blit(MON_IMG, (x//2, y//2))
		
#function that lists what monsters there are
def draw_monster_menu_list(m_p):
	width, height = WIN.get_size()
	x = 2
	for mon in m_p:
		mon_info = REG_FONT.render(str(mon.name), 1, P.RED)
		WIN.blit(mon_info, ((width - mon_info.get_width())//2, P.PADDING * x))
		x += 2
#draws items
def draw_item_menu(h_b):
	width, height = WIN.get_size()
	potions_text = REG_FONT.render("HEAL(H): "+str(h_b.heal)+"MANA(M): "+str(h_b.mana)+
				       "BOOST(B): "+str(h_b.buff),
				       1, P.RED)
	WIN.blit(potions_text, ((width - potions_text.get_width())//2, P.PADDING))
#draws skill list
def draw_skill_menu(hero):
	width, height = WIN.get_size()
	observe_text = REG_FONT.render("OBSERVE monsters: O", 1, P.RED)
	WIN.blit(observe_text, ((width - observe_text.get_width())//2,
				P.PADDING))
	buff_text = REG_FONT.render("BUFF: B", 1, P.RED)
	WIN.blit(buff_text, ((width - buff_text.get_width())//2,
			     P.PADDING * 2))
	debuff_text = REG_FONT.render("DEBBUFF enemies: D", 1, P.RED)
	WIN.blit(debuff_text, ((width - debuff_text.get_width())//2,
			       P.PADDING * 3))
	heal_text = REG_FONT.render("HEAL ally: H", 1, P.RED)
	WIN.blit(heal_text, ((width - heal_text.get_width())//2, P.PADDING * 4))
	if "Summoner" in hero.name:
		command_text = REG_FONT.render("COMMAND ally: C", 1, P.RED)
		WIN.blit(command_text, ((width - command_text.get_width())//2,
					P.PADDING * 6))
		summon_totem_text = REG_FONT.render("Summon TOTEM: T", 1, P.RED)
		WIN.blit(summon_totem_text, ((width - summon_totem_text.get_width())//2,
					     P.PADDING * 7))
		if "Grand" in hero.name:
			summon_golem = REG_FONT.render("Summon GOLEM: G", 1, P.RED)
			WIN.blit(summon_golem, ((width - summon_golem.get_width())//2,
						P.PADDING * 8))
	if "Tactician" in hero.name:
		command_text = REG_FONT.render("COMMAND ally: C", 1, P.RED)
		WIN.blit(command_text, ((width - command_text.get_width())//2,
					P.PADDING * 6))
	if "Hunter" in hero.name:
		command_text = REG_FONT.render("COMMAND ally: C", 1, P.RED)
		WIN.blit(command_text, ((width - command_text.get_width())//2,
					P.PADDING * 6))
		explode_text = REG_FONT.render("Use EXPLOSIVE: E", 1, P.RED)
		WIN.blit(explode_text, ((width - explode_text.get_width())//2,
					P.PADDING * 7))
	if "Knight" in hero.name:
		protect_text = REG_FONT.render("PROTECT Allies: P", 1, P.RED)
		WIN.blit(protect_text, ((width - protect_text.get_width())//2, P.PADDING * 7))
	if "Ninja" in hero.name:
		sneak_text = REG_FONT.render("Go for a Sneak ATTACK: A", 1, P.RED)
		WIN.blit(sneak_text, ((width - sneak_text.get_width())//2, P.PADDING * 7))
		
		
def draw_totem_menu():
	width, height = WIN.get_size()
	totem_text = REG_FONT.render("ATTACK: A / BOOST: B / DEBUFF: D / HEAL: H", 1, P.RED)
	WIN.blit(totem_text, ((width - totem_text.get_width())//2, height//3))
def draw_bomb_menu():
	width, height = WIN.get_size()
	bomb_text = REG_FONT.render("EXPLOSIVE: E / POISON: P", 1, P.RED)
	WIN.blit(bomb_text, ((width - bomb_text.get_width())//2, height//3))
#function that will draw the options in battle
def draw_battle_menu(hero):
	width, height = WIN.get_size()
	attack_text = REG_FONT.render("ATTACK monsters: A", 1, P.RED)
	WIN.blit(attack_text, (width//2 - attack_text.get_width(), P.PADDING))
	skill_text = REG_FONT.render("Use SKILL: S", 1, P.RED)
	WIN.blit(skill_text, (width//2 - skill_text.get_width(), P.PADDING * 2))
	item_text = REG_FONT.render("Use ITEM: I", 1, P.RED)
	WIN.blit(item_text, (width//2 - item_text.get_width(), P.PADDING * 3))
	if hero.mana > 0:
		magic_text = REG_FONT.render("Use MAGIC: M", 1, P.RED)
		WIN.blit(magic_text, (width//2 - magic_text.get_width(), P.PADDING * 4))


#function that will list options in the city
def draw_city_menu():
	width, height = WIN.get_size()
	inn_text = REG_FONT.render("Go to INN: I", 1, P.BLACK)
	WIN.blit(inn_text, ((width - inn_text.get_width())//2,
			    P.PADDING))
	store_text = REG_FONT.render("FORGE: F", 1, P.BLACK)
	WIN.blit(store_text, ((width - store_text.get_width())//2, P.PADDING * 2))
	practice_text = REG_FONT.render("PRACTICE arena: P", 1, P.BLACK)
	WIN.blit(practice_text, ((width - practice_text.get_width())//2, P.PADDING * 3))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.BLACK)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 4))
	
def draw_inn_menu():
	width, height = WIN.get_size()
	sleep_text = REG_FONT.render("SLEEP: S", 1, P.WHITE)
	WIN.blit(sleep_text, ((width - sleep_text.get_width())//2, P.PADDING))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 2))
	talk_text = REG_FONT.render("RECRUIT: R", 1, P.WHITE)
	WIN.blit(talk_text, ((width - talk_text.get_width())//2, P.PADDING * 3))
	privacy_text = REG_FONT.render("PRIVATE Room: P", 1, P.WHITE)
	WIN.blit(privacy_text, ((width - privacy_text.get_width())//2, P.PADDING * 4))
def draw_proom_menu():
	width, height = WIN.get_size()
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 2))
	adjust_party_text = REG_FONT.render("Change PARTY order: P", 1, P.WHITE)
	WIN.blit(adjust_party_text, ((width - adjust_party_text.get_width())//2, P.PADDING * 3))
	remove_party_text = REG_FONT.render("REMOVE from party: R", 1, P.RED)
	WIN.blit(remove_party_text, ((width - remove_party_text.get_width())//2, P.PADDING * 4))
	adjust_weapon_text = REG_FONT.render("Change WEAPONS: W", 1, P.WHITE)
	WIN.blit(adjust_weapon_text, ((width - adjust_weapon_text.get_width())//2, P.PADDING * 5))
	adjust_armor_text = REG_FONT.render("Change ARMORS: A", 1, P.WHITE)
	WIN.blit(adjust_armor_text, ((width - adjust_armor_text.get_width())//2, P.PADDING * 6))

def draw_prreorder_menu(h_p):
	width, height = WIN.get_size()
	#list out the heroes and ask the player who should act last
	x = 1
	last_text = REG_FONT.render("Who should act last?", 1, P.WHITE)
	WIN.blit(last_text, ((width - last_text.get_width())//2, P.PADDING))
	for hero in h_p:
		hero_text = REG_FONT.render(str(x) + " " + hero.name, 1, P.WHITE)
		WIN.blit(hero_text, ((width - hero_text.get_width())//2, P.PADDING * (x + 1)))
		x += 1
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 7))
def draw_hero_list(h_p):
	width, height = WIN.get_size()
	x = 1
	for hero in h_p:
		hero_text = REG_FONT.render(str(x) + " " + hero.name, 1, P.WHITE)
		WIN.blit(hero_text, ((width - hero_text.get_width())//2, P.PADDING * (x + 1)))
		x += 1
def draw_forge_menu():
	width, height = WIN.get_size()
	new_wpn = REG_FONT.render("Buy WEAPON: W", 1, P.RED)
	WIN.blit(new_wpn, ((width - new_wpn.get_width())//2, P.PADDING))
	new_amr = REG_FONT.render("Buy ARMOR: A", 1, P.RED)
	WIN.blit(new_amr, ((width - new_amr.get_width())//2, P.PADDING * 2))
	wpn_atk = REG_FONT.render("SHARPEN Weapon: S", 1, P.RED)
	WIN.blit(wpn_atk, ((width - wpn_atk.get_width())//2, P.PADDING * 3))
	wpn_effect = REG_FONT.render("INCREASE Weapon Effect: I", 1, P.RED)
	WIN.blit(wpn_effect, ((width - wpn_effect.get_width())//2, P.PADDING * 4))
	amr_def = REG_FONT.render("ENHANCE Armor: E", 1, P.RED)
	WIN.blit(amr_def, ((width - amr_def.get_width())//2, P.PADDING * 5))
	amr_effect = REG_FONT.render("BOOST Armor Effect: B", 1, P.RED)
	WIN.blit(amr_effect, ((width - amr_effect.get_width())//2, P.PADDING * 6))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.RED)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 7))
	
	
def draw_reorder_eqp_menu(h_e):
	width, height = WIN.get_size()
	#list out the equipment
	x = 1
	ask_text = REG_FONT.render("Which one?", 1, P.RED)
	WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING))
	for eqp in h_e:
		eqp_text = REG_FONT.render(str(x) + " USER: " + eqp.user + " EFFECT: " +
					   eqp.effect + " POWER: " + str(eqp.strength),
					   1, P.RED)
		WIN.blit(eqp_text, ((width - eqp_text.get_width())//2, P.PADDING * (x + 1)))
		x += 1
	leave_text = REG_FONT.render("LEAVE: L", 1, P.RED)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * (x + 1)))
	
def draw_prremove_menu(h_p):
	width, height = WIN.get_size()
	#lists out the heroes and asks who should be removed
	x = 1
	remove_text = REG_FONT.render("Who should leave the party?", 1, P.WHITE)
	WIN.blit(remove_text, ((width - remove_text.get_width())//2, P.PADDING))
	warning_text = REG_FONT.render("You may never see them again.", 1, P.WHITE)
	WIN.blit(warning_text, ((width - warning_text.get_width())//2, P.PADDING * 2))
	for hero in h_p:
		hero_text = REG_FONT.render(str(x) + " " + hero.name, 1, P.WHITE)
		WIN.blit(hero_text, ((width - hero_text.get_width())//2, P.PADDING * (x + 2)))
		x += 1
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 7))
	
def draw_recruit_menu(h_p):
	width, height = WIN.get_size()
	#this should show the text and the sprite
	#need to edit this later
	knight = None
	summoner = None
	tactician = None
	#check for duplicates
	for hero in h_p:
		if "Knight" in hero.name:
			knight = hero
		if "Summoner" in hero.name:
			summoner = hero
		if "Tactician" in hero.name:
			tactician = hero
	warrior_text = REG_FONT.render("WARRIOR: W", 1, P.RED)
	WIN.blit(warrior_text, ((width - warrior_text.get_width())//2, P.PADDING))
	cleric_text = REG_FONT.render("CLERIC: C", 1, P.GREEN)
	WIN.blit(cleric_text, ((width - cleric_text.get_width())//2, P.PADDING * 2))
	mage_text = REG_FONT.render("MAGE: M", 1, P.RED)
	WIN.blit(mage_text, ((width - mage_text.get_width())//2, P.PADDING * 3))
	ninja_text = REG_FONT.render("NINJA: N", 1, P.RED)
	WIN.blit(ninja_text, ((width - ninja_text.get_width())//2, P.PADDING * 5))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 8))
	if knight == None:
		knight_text = REG_FONT.render("KNIGHT: K", 1, P.GREEN)
		WIN.blit(knight_text, ((width - knight_text.get_width())//2, P.PADDING * 6))
	if tactician == None:
		tactician_text = REG_FONT.render("TACTICIAN: T", 1, P.BLUE)
		WIN.blit(tactician_text, ((width - tactician_text.get_width())//2, P.PADDING * 7))
	if summoner == None:
		summoner_text = REG_FONT.render("SUMMONER: S", 1, P.BLUE)
		WIN.blit(summoner_text, ((width - summoner_text.get_width())//2, P.PADDING * 4))
	
#function that will list options in the mage tower
def draw_mage_menu():
	width, height = WIN.get_size()
	train_magic = REG_FONT.render("TRAIN Magic: T", 1, P.BLACK)
	WIN.blit(train_magic, ((width - train_magic.get_width())//2, P.PADDING * 1))
	summoning_fields = REG_FONT.render("SUMMONING Fields: S", 1, P.BLACK)
	WIN.blit(summoning_fields, ((width - summoning_fields.get_width())//2, P.PADDING * 2))
	enchanter = REG_FONT.render("ENCHANT Equipment: E", 1, P.BLACK)
	WIN.blit(enchanter, ((width - enchanter.get_width())//2, P.PADDING * 3))
	library = REG_FONT.render("BOOKSTORE: B", 1, P.BLACK)
	WIN.blit(library, ((width - library.get_width())//2, P.PADDING * 4))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.BLACK)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 5))
	
def draw_summon_menu(h_ally):
	width, height = WIN.get_size()
	angel = None
	for ally in h_ally:
		if "Angel" in ally.name:
			angel = ally
	if angel == None:
		summon_text = REG_FONT.render("SUMMON Angel: S", 1, P.BLACK)
		WIN.blit(summon_text, ((width - summon_text.get_width())//2, P.PADDING * 1))
	elif angel != None:
		stat_text = REG_FONT.render("STAGE: " + str(angel.stage) + " ATK: " + str(angel.atk), 1, P.BLACK)
		WIN.blit(stat_text, ((width - stat_text.get_width())//2, P.PADDING * 1))
		if angel.stage < C.STAGE_LIMIT:
			train_text = REG_FONT.render("Train SUMMON: S", 1, P.BLACK)
			WIN.blit(train_text, ((width - train_text.get_width())//2, P.PADDING * 2))
			price_text = REG_FONT.render("PRICE: "+str(angel.atk**angel.stage), 1, P.BLACK)
			WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 3))
			leave_text = REG_FONT.render("LEAVE: L", 1, P.BLACK)
			WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 4))
		elif angel.stage >= C.STAGE_LIMIT:
			train_text = REG_FONT.render("Train SUMMON: S", 1, P.BLACK)
			WIN.blit(train_text, ((width - train_text.get_width())//2, P.PADDING * 2))
			price_text = REG_FONT.render("PRICE: "+str((angel.atk * angel.stage) ** C.INCREASE_EXPONENT), 1, P.BLACK)
			WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 3))
			leave_text = REG_FONT.render("LEAVE: L", 1, P.BLACK)
			WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 4))
	
def draw_spell_list(h_magic):
	width, height = WIN.get_size()
	x = 2
	ask_text = REG_FONT.render("Which one?", 1, P.RED)
	WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING))
	for spell in h_magic:
		stat_text = REG_FONT.render(str(x-1) + " " + spell.name +
					    " ELEMENT: " + spell.element + " POWER: " + str(spell.power) +
					    " COST: " + str(spell.cost) + " TARGETS: " + str(spell.targets),
					    1, P.RED)
		WIN.blit(stat_text, ((width - stat_text.get_width())//2, P.PADDING * x))
		x += 1
def draw_train_spell_menu(spell, h_b):
	width, height = WIN.get_size()
	stat_text = REG_FONT.render("POWER: " + str(spell.power) + "  COST: " + str(spell.cost) +
				    "  COINS: " + str(h_b.coins), 1, P.RED)
	WIN.blit(stat_text, ((width - stat_text.get_width())//2, P.PADDING))
	if spell.targets == 1:
		target_text = REG_FONT.render("AOE: NO", 1, P.RED)
	elif spell.targets >= 1:
		target_text = REG_FONT.render("AOE: YES", 1, P.RED)
	WIN.blit(target_text, ((width - target_text.get_width())//2, P.PADDING * 2))
	ask_text = REG_FONT.render("What do you want to train?", 1, P.RED)
	WIN.blit(ask_text, ((width - ask_text.get_width())//2, P.PADDING * 3))
	power_text = REG_FONT.render("P/POWER  PRICE: " + str(spell.power**C.INCREASE_EXPONENT)
				     , 1, P.RED)
	WIN.blit(power_text, ((width - power_text.get_width())//2, P.PADDING * 4))
	if spell.cost > 1:
		cupgrade_text = REG_FONT.render("C/COST  PRICE: " + str(spell.power**C.INCREASE_EXPONENT),
						1, P.RED)
		WIN.blit(cupgrade_text, ((width - cupgrade_text.get_width())//2, P.PADDING * 5))
	if spell.targets == 1:
		tupgrade_text = REG_FONT.render("A/AOE  PRICE: 100", 1, P.RED)
		WIN.blit(tupgrade_text, ((width - tupgrade_text.get_width())//2, P.PADDING * 6))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.RED)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 7))
	
		
def draw_enchanter_menu():
	width, height = WIN.get_size()
	amr_enchant = REG_FONT.render("Enchant ARMOR: A", 1, P.WHITE)
	WIN.blit(amr_enchant, ((width - amr_enchant.get_width())//2, P.PADDING * 1))
	wpn_enchant = REG_FONT.render("Enchant WEAPON: W", 1, P.WHITE)
	WIN.blit(wpn_enchant, ((width - wpn_enchant.get_width())//2, P.PADDING * 2))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 3))
	
def draw_equip_enchant_menu(equip, h_b):
	width, height = WIN.get_size()
	equip_stats = REG_FONT.render("ENCHANTMENT: " + equip.effect +
				    " ELEMENT: " + equip.element,
				    1, P.WHITE)
	WIN.blit(equip_stats, ((width - equip_stats.get_width())//2, P.PADDING * 1))
	coins_stats = REG_FONT.render("COINS: " + str(h_b.coins), 1, P.WHITE)
	#WIN.blit(coins_stats, ((width - coins_stats.get_width())//2, P.PADDING * 2))
	choice_text = REG_FONT.render("Change ELEMENT: E, Change eFFECT: F", 1, P.WHITE)
	WIN.blit(choice_text, ((width - choice_text.get_width())//2, P.PADDING * 2))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 3))

def draw_element_enchant(eqp, h_b):
	width, height = WIN.get_size()
	coins_stats = REG_FONT.render("ELEMENT: " + eqp.element + " COINS: " + str(h_b.coins),
				      1, P.WHITE)
	WIN.blit(coins_stats, ((width - coins_stats.get_width())//2, P.PADDING * 1))
	pick_element_text = REG_FONT.render("AIR: A / EARTH: E / FIRE: F / WATER: W",
					    1, P.WHITE)
	WIN.blit(pick_element_text, ((width - pick_element_text.get_width())//2, P.PADDING * 2))
	reg_price_text = REG_FONT.render("PRICE: " + str(C.ENCHANT_PRICE), 1, P.WHITE)
	WIN.blit(reg_price_text, ((width - reg_price_text.get_width())//2, P.PADDING * 3))
	adv_element_text = REG_FONT.render("DARK: D / LIGHT: I", 1, P.WHITE)
	WIN.blit(adv_element_text, ((width - adv_element_text.get_width())//2, P.PADDING * 4))
	price_text = REG_FONT.render("PRICE: " + str(C.ENCHANT_PRICE ** C.INCREASE_EXPONENT), 1, P.WHITE)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 5))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 6))

def draw_armor_enchant_menu(amr, h_b):
	width, height = WIN.get_size()
	coins_stats = REG_FONT.render("ENCHANTMENT: " + amr.effect + " COINS: " + str(h_b.coins),
				      1, P.WHITE)
	WIN.blit(coins_stats, ((width - coins_stats.get_width())//2, P.PADDING * 1))
	pick_effect_text = REG_FONT.render("ABSORB: A / BLOCK: B",
					    1, P.WHITE)
	WIN.blit(pick_effect_text, ((width - pick_effect_text.get_width())//2, P.PADDING * 2))
	reg_price_text = REG_FONT.render("PRICE: " + str(C.ENCHANT_PRICE), 1, P.WHITE)
	WIN.blit(reg_price_text, ((width - reg_price_text.get_width())//2, P.PADDING * 3))
	adv_effect_text = REG_FONT.render("POISON: P", 1, P.WHITE)
	WIN.blit(adv_effect_text, ((width - adv_effect_text.get_width())//2, P.PADDING * 4))
	price_text = REG_FONT.render("PRICE: " + str(C.ENCHANT_PRICE ** C.INCREASE_EXPONENT), 1, P.WHITE)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 5))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 6))

def draw_weapon_enchant_menu(wpn, h_b):
	width, height = WIN.get_size()
	coins_stats = REG_FONT.render("ENCHANTMENT: " + wpn.effect + " COINS: " + str(h_b.coins),
				      1, P.WHITE)
	WIN.blit(coins_stats, ((width - coins_stats.get_width())//2, P.PADDING * 1))
	pick_effect_text = REG_FONT.render("ATTACK: A / LIFESTEAL: I",
					    1, P.WHITE)
	WIN.blit(pick_effect_text, ((width - pick_effect_text.get_width())//2, P.PADDING * 2))
	reg_price_text = REG_FONT.render("PRICE: " + str(C.ENCHANT_PRICE), 1, P.WHITE)
	WIN.blit(reg_price_text, ((width - reg_price_text.get_width())//2, P.PADDING * 3))
	adv_effect_text = REG_FONT.render("MANADRAIN: M / POISON: P / SKILLDRAIN: S",
					  1, P.WHITE)
	WIN.blit(adv_effect_text, ((width - adv_effect_text.get_width())//2, P.PADDING * 4))
	price_text = REG_FONT.render("PRICE: " + str(C.ENCHANT_PRICE ** C.INCREASE_EXPONENT), 1, P.WHITE)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 5))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 6))

def draw_bookstore_menu():
	width, height = WIN.get_size()
	choice_text = REG_FONT.render("BUY New Spellbooks: B / EDIT Spellbooks : E / SELL Spellbooks: S",
				      1, P.WHITE)
	WIN.blit(choice_text, ((width - choice_text.get_width())//2, P.PADDING * 1))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 2))

def draw_buy_spell_menu(h_b):
	width, height = WIN.get_size()
	coins_text = REG_FONT.render("COINS: " + str(h_b.coins), 1, P.WHITE)
	WIN.blit(coins_text, ((width - coins_text.get_width())//2, P.PADDING * 1))
	pick_element_text = REG_FONT.render("AIR: A / EARTH: E / FIRE: F / WATER: W",
					    1, P.WHITE)
	WIN.blit(pick_element_text, ((width - pick_element_text.get_width())//2, P.PADDING * 2))
	reg_price_text = REG_FONT.render("PRICE: " + str(C.ENCHANT_PRICE), 1, P.WHITE)
	WIN.blit(reg_price_text, ((width - reg_price_text.get_width())//2, P.PADDING * 3))
	adv_element_text = REG_FONT.render("DARK: D", 1, P.WHITE)
	WIN.blit(adv_element_text, ((width - adv_element_text.get_width())//2, P.PADDING * 4))
	price_text = REG_FONT.render("PRICE: " + str(C.ENCHANT_PRICE ** C.INCREASE_EXPONENT), 1, P.WHITE)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 5))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 6))
def draw_sell_spell_menu(spell, h_b):
	width, height = WIN.get_size()
	coins_text = REG_FONT.render("COINS: " + str(h_b.coins), 1, P.WHITE)
	WIN.blit(coins_text, ((width - coins_text.get_width())//2, P.PADDING * 1))
	spell_stat = REG_FONT.render("POWER: " + str(spell.power), 1, P.WHITE)
	WIN.blit(coins_text, ((width - coins_text.get_width())//2, P.PADDING * 2))
	price_text = REG_FONT.render("PRICE: " + str(spell.power ** C.INCREASE_EXPONENT) + " SELL? Y/N",
				     1, P.WHITE)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 3))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 4))
	
#texts inside the monster hunter guild
def draw_guild_menu(qi_npc, a_npc):
	width, height = WIN.get_size()
	currency_text = REG_FONT.render("Packages: "+str(qi_npc.package)+
					" Reciepts: "+str(qi_npc.rpackage)+
					" Mana Crystal: "+str(qi_npc.managem), 1, P.WHITE)
	WIN.blit(currency_text, ((width - currency_text.get_width())//2, P.PADDING * 1))
	package_text = REG_FONT.render("Accept QUEST: Q", 1, P.WHITE)
	WIN.blit(package_text, ((width - package_text.get_width())//2, P.PADDING * 2))
	return_text = REG_FONT.render("Claim REWARDS: R", 1, P.WHITE)
	WIN.blit(return_text, ((width - return_text.get_width())//2, P.PADDING * 3))
	armor_text = REG_FONT.render("Visit ARMORER: A", 1, P.WHITE)
	WIN.blit(armor_text, ((width - armor_text.get_width())//2, P.PADDING * 4))
	tinkerer_text = REG_FONT.render("Visit TINKERER: T", 1, P.WHITE)
	WIN.blit(tinkerer_text, ((width - tinkerer_text.get_width())//2, P.PADDING * 5))
	enchanter_text = REG_FONT.render("Enter ENCHANTER Garden: E", 1, P.WHITE)
	WIN.blit(enchanter_text, ((width - enchanter_text.get_width())//2, P.PADDING * 6))
	if a_npc.rank >= 20:
		grandmaster_text = REG_FONT.render("Enter GRANDMASTER Hall: G", 1, P.WHITE)
		WIN.blit(grandmaster_text, ((width - grandmaster_text.get_width())//2, P.PADDING * 7))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 8))

def draw_armorer_menu(h_bag, qi_npc, a_npc):
	width, height = WIN.get_size()
	currency_text = REG_FONT.render("Coins: "+str(h_bag.coins)+
					" Mana Gems: "+str(qi_npc.managem), 1, P.WHITE)
	WIN.blit(currency_text, ((width - currency_text.get_width())//2, P.PADDING * 1))
	sell_amr_text = REG_FONT.render("Sell ARMOR: A", 1, P.WHITE)
	WIN.blit(sell_amr_text, ((width - sell_amr_text.get_width())//2, P.PADDING * 2))
	sell_wpn_text = REG_FONT.render("Sell WEAPONS: W", 1, P.WHITE)
	WIN.blit(sell_wpn_text, ((width - sell_wpn_text.get_width())//2, P.PADDING * 3))
	if a_npc.rank > 10:
		buy_text = REG_FONT.render("BUY: B", 1, P.WHITE)
		WIN.blit(buy_text, ((width - buy_text.get_width())//2, P.PADDING * 4))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 5))
def draw_equip_price(equip, price):
	width, height = WIN.get_size()
	equip_text = REG_FONT.render("EFFECT: "+equip.effect+" POWER: "+str(equip.strength)+
				     " UPGRADES: "+str(equip.upgrade), 1, P.WHITE)
	WIN.blit(equip_text, ((width - equip_text.get_width())//2, P.PADDING * 1))
	price_text = REG_FONT.render("PRICE: "+str(price), 1, P.WHITE)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 2))
	choice_text = REG_FONT.render("YES/NO : Y/N", 1, P.WHITE)
	WIN.blit(choice_text, ((width - choice_text.get_width())//2, P.PADDING * 3))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 5))

def draw_unique_equip(h_wpn, qi_npc):
	width, height = WIN.get_size()
	price_text = REG_FONT.render("They all cost "+str(C.ENCHANT_PRICE)+
				     " mana gems. MANA GEMS: "+str(qi_npc.managem), 1, P.WHITE)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 1))
	observer_text = REG_FONT.render("Buy an OBSERVER: O", 1, P.WHITE)
	WIN.blit(observer_text, ((width - observer_text.get_width())//2, P.PADDING * 2))
	for wpn in h_wpn:
		if "Ninja" in wpn.user:
			ninja_text = REG_FONT.render("Buy a HIDDEN DAGGER for a NINJA: N", 1, P.WHITE)
			WIN.blit(ninja_text, ((width - ninja_text.get_width())//2, P.PADDING * 3))
		if "Summoner" in wpn.user:
			summon_text = REG_FONT.render("Buy a SUMMONING STAFF: S", 1, P.WHITE)
			WIN.blit(summon_text, ((width - summon_text.get_width())//2, P.PADDING * 4))
		if "Cleric" in wpn.user:
			heal_text = REG_FONT.render("Buy a HEALING Staff for a CLERIC: C", 1, P.WHITE)
			WIN.blit(heal_text, ((width - heal_text.get_width())//2, P.PADDING * 5))
		if "Knight" in wpn.user:
			shield_text = REG_FONT.render("Buy a SHIELD for a KNIGHT: K", 1, P.WHITE)
			WIN.blit(shield_text, ((width - shield_text.get_width())//2, P.PADDING * 6))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 10))

def draw_tinkerer_menu(qi_npc, a_npc):
	width, height = WIN.get_size()
	currency_text = REG_FONT.render("Mana Gems: "+str(qi_npc.managem), 1, P.WHITE)
	WIN.blit(currency_text, ((width - currency_text.get_width())//2, P.PADDING * 1))
	upgrade_text = REG_FONT.render("Upgrade ARMOR: A / Upgrade WEAPONS: W", 1, P.WHITE)
	WIN.blit(upgrade_text, ((width - upgrade_text.get_width())//2, P.PADDING * 2))
	if a_npc.rank > 15:
		combine_text = REG_FONT.render("COMBINE ARMOR: C / FUSE WEAPONS: F (PRICE: "+str(C.ENCHANT_PRICE)+")", 1, P.WHITE)
		WIN.blit(combine_text, ((width - combine_text.get_width())//2, P.PADDING * 3))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 5))
def draw_henchanter_menu():
	width, height = WIN.get_size()
	amr_enchant = REG_FONT.render("Enchant ARMOR: A", 1, P.GREEN)
	WIN.blit(amr_enchant, ((width - amr_enchant.get_width())//2, height//3 + P.PADDING * 1))
	wpn_enchant = REG_FONT.render("Enchant WEAPON: W", 1, P.RED)
	WIN.blit(wpn_enchant, ((width - wpn_enchant.get_width())//2, height//3 + P.PADDING * 2))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.BLUE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, height//3 + P.PADDING * 3))
def hunter_armor_enchant(qi_npc, a_npc):
	width, height = WIN.get_size()
	currency_text = REG_FONT.render("Mana Gems: "+str(qi_npc.managem), 1, P.GREEN)
	WIN.blit(currency_text, ((width - currency_text.get_width())//2, P.PADDING * 1))
	price_text = REG_FONT.render("PRICE: "+str(C.ENCHANT_PRICE), 1, P.GREEN)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 2))
	if a_npc.rank > 20:
		revive_text = REG_FONT.render("REVIVE ARMOR: R", 1, P.GREEN)
		WIN.blit(revive_text, ((width - revive_text.get_width())//2, P.PADDING * 3))
	if a_npc.rank > 15:
		ethereal_text = REG_FONT.render("ETHEREAL ARMOR: E", 1, P.GREEN)
		WIN.blit(ethereal_text, ((width - ethereal_text.get_width())//2, P.PADDING * 4))
	if a_npc.rank > 10:
		bomb_text = REG_FONT.render("BURST ARMOR: B", 1, P.GREEN)
		WIN.blit(bomb_text, ((width - bomb_text.get_width())//2, P.PADDING * 5))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.GREEN)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 10))
def hunter_weapon_enchant(qi_npc, a_npc):
	width, height = WIN.get_size()
	currency_text = REG_FONT.render("Mana Gems: "+str(qi_npc.managem), 1, P.RED)
	WIN.blit(currency_text, ((width - currency_text.get_width())//2, P.PADDING * 1))
	price_text = REG_FONT.render("PRICE: "+str(C.ENCHANT_PRICE), 1, P.RED)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 2))
	if a_npc.rank > 20:
		death_text = REG_FONT.render("DEATH: D", 1, P.RED)
		WIN.blit(death_text, ((width - death_text.get_width())//2, P.PADDING * 3))
	if a_npc.rank > 15:
		necro_text = REG_FONT.render("NECROMANCER: N", 1, P.RED)
		WIN.blit(necro_text, ((width - necro_text.get_width())//2, P.PADDING * 4))
	if a_npc.rank > 10:
		explode_text = REG_FONT.render("EXPLODE: E", 1, P.RED)
		WIN.blit(explode_text, ((width - explode_text.get_width())//2, P.PADDING * 5))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.RED)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 10))
def draw_grandmaster_menu():
	width, height = WIN.get_size()
	greeting_text = REG_FONT.render("I continue to hear of your great exploits. ", 1, P.WHITE)
	WIN.blit(greeting_text, ((width - greeting_text.get_width())//2, P.PADDING * 1))
	choice_text = REG_FONT.render("Would you like to REST: R here?", 1, P.WHITE)
	WIN.blit(choice_text, ((width - choice_text.get_width())//2, P.PADDING * 2))
	choice2_text = REG_FONT.render("I can also help you TRAIN: T beyond your limits.", 1, P.WHITE)
	WIN.blit(choice2_text, ((width - choice2_text.get_width())//2, P.PADDING * 3))
	train_text = REG_FONT.render("Of course, you'll need a lot of mana to go through my training.", 1, P.WHITE)
	WIN.blit(train_text, ((width - train_text.get_width())//2, P.PADDING * 4))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 8))

def draw_prestige_price(hero, price):
	width, height = WIN.get_size()
	hero_text = REG_FONT.render("HERO: "+hero.name+" LEVEL: "+str(hero.level), 1, P.WHITE)
	WIN.blit(hero_text, ((width - hero_text.get_width())//2, P.PADDING * 1))
	price_text = REG_FONT.render("PRICE: "+str(price), 1, P.WHITE)
	WIN.blit(price_text, ((width - price_text.get_width())//2, P.PADDING * 2))
	choice_text = REG_FONT.render("YES/NO : Y/N", 1, P.WHITE)
	WIN.blit(choice_text, ((width - choice_text.get_width())//2, P.PADDING * 3))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
	WIN.blit(leave_text, ((width - leave_text.get_width())//2, P.PADDING * 5))
	
#function that will tell the player they don't have enough money
def poor_text():
	width, height = WIN.get_size()
	poor_text = REG_FONT.render("You can't afford that. ", 1, P.WHITE)
	WIN.blit(poor_text, ((width - poor_text.get_width())//2, P.PADDING))
	pygame.display.update()
	pygame.time.delay(P.SMALLDELAY)
	
def poor_text_2():
	width, height = WIN.get_size()
	poor_text = REG_FONT.render("I don't talk to poor people. ", 1, P.BLACK)
	WIN.blit(poor_text, ((width - poor_text.get_width())//2, P.PADDING))
	pygame.display.update()
	pygame.time.delay(P.SMALLDELAY)
	
def poor_text_3():
	width, height = WIN.get_size()
	poor_text = REG_FONT.render("Leave. ", 1, P.RED)
	WIN.blit(poor_text, ((width - poor_text.get_width())//2, P.PADDING))
	pygame.display.update()
	pygame.time.delay(P.SMALLDELAY)
	
#function will list options for the player
def draw_menu(qi_npc):
	width, height = WIN.get_size()
	talk_text = REG_FONT.render("TALK to nearby man: T", 1, P.BLACK)
	WIN.blit(talk_text, (width//3 - talk_text.get_width(), P.PADDING * 1))
	save_text = REG_FONT.render("RECORD journey: R", 1, P.GREEN)
	WIN.blit(save_text, (width//3 - save_text.get_width(), P.PADDING * 2))
	mage_text = REG_FONT.render("Visit WIZARD Tower: W", 1, P.BLACK)
	WIN.blit(mage_text, (width//3 - mage_text.get_width(), P.PADDING * 5))
	city_text = REG_FONT.render("Return to CITY: C", 1, P.BLACK)
	WIN.blit(city_text, (width//3 - city_text.get_width(), P.PADDING * 4))
	leave_text = REG_FONT.render("Stop Adventuring and SLEEP: S", 1, P.GREEN)
	WIN.blit(leave_text, (width//3 - leave_text.get_width(), P.PADDING * 3))
	attack_text = REG_FONT.render("ATTACK monsters: A", 1, P.RED)
	WIN.blit(attack_text, (width//3 - attack_text.get_width(), P.PADDING * 6))
	explore_text = REG_FONT.render("Visit remote VILLAGES: V", 1, P.RED)
	WIN.blit(explore_text, (width//3 - explore_text.get_width(), P.PADDING * 7))
	hunter_text = REG_FONT.render("Enter MONSTER Hunter Guild: M", 1, P.BLACK)
	WIN.blit(hunter_text, (width//3 - hunter_text.get_width(), P.PADDING * 8))
	if qi_npc.package > 0:
		quest_text = REG_FONT.render("Deliver PACKAGES: P", 1, P.RED)
		WIN.blit(quest_text, (width//3 - quest_text.get_width(), P.PADDING * 9))

