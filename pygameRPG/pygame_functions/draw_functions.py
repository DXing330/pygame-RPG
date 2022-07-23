import pygame
import os
import sys
sys.path.append("..")
sys.path.append("../Assets")
from pygconstants import PYGConstants
P = PYGConstants()
REG_FONT = pygame.font.SysFont("comicsans", 20)
WIN = pygame.display.set_mode((P.WIDTH, P.HEIGHT))
pygame.display.set_caption("RPG")
#images used
PLAINS_RAW = pygame.image.load(os.path.join("Assets", "plains.png"))
PLAINS_IMG = pygame.transform.scale(PLAINS_RAW, (P.WIDTH, P.HEIGHT))
FOREST_RAW = pygame.image.load(os.path.join("Assets", "forest.png"))
FOREST_IMG = pygame.transform.scale(FOREST_RAW, (P.WIDTH, P.HEIGHT))
CITY_RAW = pygame.image.load(os.path.join("Assets", "city.png"))
CITY_IMG = pygame.transform.scale(CITY_RAW, (P.WIDTH, P.HEIGHT))
HERO_RAW = pygame.image.load(os.path.join("Assets", "hero.png"))
HERO_IMG = pygame.transform.scale(HERO_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SUMMONER_RAW = pygame.image.load(os.path.join("Assets", "summoner.png"))
SUMMONER_IMG = pygame.transform.scale(SUMMONER_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
KNIGHT_RAW = pygame.image.load(os.path.join("Assets", "knight.png"))
KNIGHT_IMG = pygame.transform.scale(KNIGHT_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
HUNTER_RAW =pygame.image.load(os.path.join("Assets", "hunter.png"))
HUNTER_IMG = pygame.transform.scale(HUNTER_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
ANGEL_RAW = pygame.image.load(os.path.join("Assets", "angel.png"))
ANGEL_IMG = pygame.transform.scale(ANGEL_RAW, (P.SPRITE_WIDTH//2, P.SPRITE_HEIGHT//2))
MON_RAW = pygame.image.load(os.path.join("Assets", "g_mon.png"))
MON_IMG = pygame.transform.scale(MON_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
SLIME_RAW = pygame.image.load(os.path.join("Assets", "slime.png"))
SLIME_IMG = pygame.transform.scale(SLIME_RAW, (P.SPRITE_WIDTH, P.SPRITE_HEIGHT))
#function that will draw characters in battle
def draw_heroes(h_p, h_ally):
	for player in h_p:
		if "Hunter" in player.name:
			WIN.blit(HUNTER_IMG,
				 (P.WIDTH - (P.SPRITE_WIDTH * 2),
				 P.HEIGHT - (P.SPRITE_HEIGHT * 4)))
		if "Hero" in player.name:
			WIN.blit(HERO_IMG,
				 (P.WIDTH - (P.SPRITE_WIDTH * 1),
				 P.HEIGHT - (P.SPRITE_HEIGHT * 2)))
		if "Summoner" in player.name:
			WIN.blit(SUMMONER_IMG,
				 (P.WIDTH - (P.SPRITE_WIDTH * 1.5),
				 P.HEIGHT - (P.SPRITE_HEIGHT * 3)))
		if "Knight" in player.name:
			WIN.blit(KNIGHT_IMG,
				 (P.WIDTH - (P.SPRITE_WIDTH * 2.5),
				 P.HEIGHT - (P.SPRITE_HEIGHT * 5)))
		
	for aly in h_ally:
		if "Angel" in aly.name:
			WIN.blit(ANGEL_IMG,
				 (P.WIDTH - (P.SPRITE_WIDTH * 2),
				 P.HEIGHT - (P.SPRITE_HEIGHT * 3)))

	pygame.display.update()
#function that will draw monster stats
def draw_monster_stats(m_p):
	x = 2
	for mon in m_p:
		if mon.buff == None:
			stats_text = REG_FONT.render((mon.name+" ATK: "+str(mon.atk)+" DEF: "+str(mon.defense)+
						 " SKILL: "+str(mon.skill)+" ELEMENT: "+mon.element),
						1, P.RED)
		elif mon.buff != None:
			stats_text = REG_FONT.render((mon.name+" ATK: "+str(mon.atk)+" DEF: "+str(mon.defense)+
						 " SKILL: "+str(mon.skill)+" ELEMENT: "+mon.element+
						 " BUFF: "+mon.buff),
						1, P.RED)
		WIN.blit(stats_text, (P.PADDING,
				      P.PADDING + stats_text.get_height() * x))
		pygame.display.update()
		x += 1
	pygame.time.delay(P.TIMEDELAY)
#function that will draw monsters in battle
def draw_monsters(m_p):
	x = 2
	for mon in m_p:
		if "Slime" in mon.name:
			WIN.blit(SLIME_IMG,
				 (P.PADDING//2 * x,
				  P.HEIGHT - (P.SPRITE_HEIGHT * x)))
		else:
			WIN.blit(MON_IMG,
				 (P.PADDING//2 * x,
				  P.HEIGHT - (P.SPRITE_HEIGHT * x)))
		x += 1
		
#function that lists what monsters there are
def draw_monster_menu_list(m_p):
	x = 2
	for mon in m_p:
		mon_info = REG_FONT.render(str(mon.name), 1, P.BLACK)
		WIN.blit(mon_info, (P.WIDTH//2 - mon_info.get_width(), P.PADDING * x))
		x += 2
#draws skill list
def draw_skill_menu(hero):
	observe_text = REG_FONT.render("OBSERVE monsters: O", 1, P.RED)
	WIN.blit(observe_text, ((P.WIDTH - observe_text.get_width())//2,
				P.PADDING))
	buff_text = REG_FONT.render("BUFF: B", 1, P.RED)
	WIN.blit(buff_text, ((P.WIDTH - buff_text.get_width())//2,
			     P.PADDING * 2))
	debuff_text = REG_FONT.render("DEBBUFF enemies: D", 1, P.RED)
	WIN.blit(debuff_text, ((P.WIDTH - debuff_text.get_width())//2,
			       P.PADDING * 3))
	heal_text = REG_FONT.render("HEAL ally: H", 1, P.RED)
	WIN.blit(heal_text, ((P.WIDTH - heal_text.get_width())//2, P.PADDING * 4))
	if "Summoner" in hero.name:
		command_text = REG_FONT.render("COMMAND ally: C", 1, P.RED)
		WIN.blit(command_text, ((P.WIDTH - command_text.get_width())//2,
					P.PADDING * 6))
		summon_totem_text = REG_FONT.render("Summon TOTEM: T", 1, P.RED)
		WIN.blit(summon_totem_text, ((P.WIDTH - summon_totem_text.get_width())//2,
					     P.PADDING * 7))
	if "Tactician" in hero.name:
		command_text = REG_FONT.render("COMMAND ally: C", 1, P.RED)
		WIN.blit(command_text, ((P.WIDTH - command_text.get_width())//2,
					P.PADDING * 6))
	if "Hunter" in hero.name:
		command_text = REG_FONT.render("COMMAND ally: C", 1, P.RED)
		WIN.blit(command_text, ((P.WIDTH - command_text.get_width())//2,
					P.PADDING * 6))
		explode_text = REG_FONT.render("Use EXPLOSIVE: E", 1, P.RED)
		WIN.blit(explode_text, ((P.WIDTH - explode_text.get_width())//2,
					P.PADDING * 7))
		
		
#function that will draw the options in battle
def draw_battle_menu(h_p, m_p, h_ally, h_m, h_w, h_a):
	attack_text = REG_FONT.render("ATTACK monsters: A", 1, P.RED)
	WIN.blit(attack_text, (P.WIDTH//2 - attack_text.get_width(), P.PADDING))
	skill_text = REG_FONT.render("Use SKILL: S", 1, P.RED)
	WIN.blit(skill_text, (P.WIDTH//2 - skill_text.get_width(),
			    P.PADDING * 2))

#function that will list options in the city
def draw_city_menu():
	inn_text = REG_FONT.render("Go to INN: I", 1, P.BLACK)
	WIN.blit(inn_text, ((P.WIDTH - inn_text.get_width())//2,
			    P.PADDING))
	store_text = REG_FONT.render("FORGE: F", 1, P.BLACK)
	WIN.blit(store_text, ((P.WIDTH - store_text.get_width())//2, P.PADDING * 2))
	practice_text = REG_FONT.render("PRACTICE arena: P", 1, P.BLACK)
	WIN.blit(practice_text, ((P.WIDTH - practice_text.get_width())//2, P.PADDING * 3))
	leave_text = REG_FONT.render("LEAVE: L", 1, P.BLACK)
	WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 4))
	
def draw_inn_menu():
        sleep_text = REG_FONT.render("SLEEP: S", 1, P.WHITE)
        WIN.blit(sleep_text, ((P.WIDTH - sleep_text.get_width())//2, P.PADDING))
        leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
        WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 2))
        talk_text = REG_FONT.render("RECRUIT: R", 1, P.WHITE)
        WIN.blit(talk_text, ((P.WIDTH - talk_text.get_width())//2, P.PADDING * 3))
        privacy_text = REG_FONT.render("PRIVATE Room: P", 1, P.WHITE)
        WIN.blit(privacy_text, ((P.WIDTH - privacy_text.get_width())//2, P.PADDING * 4))
def draw_proom_menu():
        leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
        WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 2))
        adjust_party_text = REG_FONT.render("Change PARTY order: P", 1, P.WHITE)
        WIN.blit(adjust_party_text, ((P.WIDTH - adjust_party_text.get_width())//2, P.PADDING * 3))
        remove_party_text = REG_FONT.render("REMOVE from party: R", 1, P.RED)
        WIN.blit(remove_party_text, ((P.WIDTH - remove_party_text.get_width())//2, P.PADDING * 4))
        adjust_weapon_text = REG_FONT.render("Change WEAPONS: W", 1, P.WHITE)
        WIN.blit(adjust_weapon_text, ((P.WIDTH - adjust_weapon_text.get_width())//2, P.PADDING * 5))
        adjust_armor_text = REG_FONT.render("Change ARMORS: A", 1, P.WHITE)
        WIN.blit(adjust_armor_text, ((P.WIDTH - adjust_armor_text.get_width())//2, P.PADDING * 6))

def draw_prreorder_menu(h_p):
        #list out the heroes and ask the player who should act last
        x = 1
        last_text = REG_FONT.render("Who should act last?", 1, P.WHITE)
        WIN.blit(last_text, ((P.WIDTH - last_text.get_width())//2, P.PADDING))
        for hero in h_p:
                hero_text = REG_FONT.render(str(x) + " " + hero.name, 1, P.WHITE)
                WIN.blit(hero_text, ((P.WIDTH - hero_text.get_width())//2, P.PADDING * (x + 1)))
                x += 1
        leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
        WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 7))
def draw_hero_list(h_p):
        x = 1
        for hero in h_p:
                hero_text = REG_FONT.render(str(x) + " " + hero.name, 1, P.WHITE)
                WIN.blit(hero_text, ((P.WIDTH - hero_text.get_width())//2, P.PADDING * (x + 1)))
                x += 1
def draw_forge_menu():
        new_wpn = REG_FONT.render("Buy WEAPON: W", 1, P.WHITE)
        WIN.blit(new_wpn, ((P.WIDTH - new_wpn.get_width())//2, P.PADDING))
        new_amr = REG_FONT.render("Buy ARMOR: A", 1, P.WHITE)
        WIN.blit(new_amr, ((P.WIDTH - new_amr.get_width())//2, P.PADDING * 2))
        wpn_atk = REG_FONT.render("SHARPEN Weapon: S", 1, P.WHITE)
        WIN.blit(wpn_atk, ((P.WIDTH - wpn_atk.get_width())//2, P.PADDING * 3))
        wpn_effect = REG_FONT.render("INCREASE Weapon Effect: I", 1, P.WHITE)
        WIN.blit(wpn_effect, ((P.WIDTH - wpn_effect.get_width())//2, P.PADDING * 4))
        amr_def = REG_FONT.render("ENHANCE Armor: E", 1, P.WHITE)
        WIN.blit(amr_def, ((P.WIDTH - amr_def.get_width())//2, P.PADDING * 5))
        amr_effect = REG_FONT.render("BOOST Armor Effect: B", 1, P.WHITE)
        WIN.blit(amr_effect, ((P.WIDTH - amr_effect.get_width())//2, P.PADDING * 6))
        leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
        WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 7))
        
        
def draw_reorder_eqp_menu(h_e):
        #list out the heroes and ask the player who should act last
        x = 1
        ask_text = REG_FONT.render("Which one?", 1, P.WHITE)
        WIN.blit(ask_text, ((P.WIDTH - ask_text.get_width())//2, P.PADDING))
        for eqp in h_e:
                eqp_text = REG_FONT.render(str(x) + " USER: " + eqp.user + " EFFECT: " + eqp.effect + " POWER: " + str(eqp.strength), 1, P.WHITE)
                WIN.blit(eqp_text, ((P.WIDTH - eqp_text.get_width())//2, P.PADDING * (x + 1)))
                x += 1
        leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
        WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * (x + 1)))
        
def draw_prremove_menu(h_p):
        #lists out the heroes and asks who should be removed
        x = 1
        remove_text = REG_FONT.render("Who should leave the party?", 1, P.WHITE)
        WIN.blit(remove_text, ((P.WIDTH - remove_text.get_width())//2, P.PADDING))
        warning_text = REG_FONT.render("You may never see them again.", 1, P.WHITE)
        WIN.blit(warning_text, ((P.WIDTH - warning_text.get_width())//2, P.PADDING * 2))
        for hero in h_p:
                hero_text = REG_FONT.render(str(x) + " " + hero.name, 1, P.WHITE)
                WIN.blit(hero_text, ((P.WIDTH - hero_text.get_width())//2, P.PADDING * (x + 2)))
                x += 1
        leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
        WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 7))
        
def draw_recruit_menu(h_p):
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
        WIN.blit(warrior_text, ((P.WIDTH - warrior_text.get_width())//2, P.PADDING))
        cleric_text = REG_FONT.render("CLERIC: C", 1, P.GREEN)
        WIN.blit(cleric_text, ((P.WIDTH - cleric_text.get_width())//2, P.PADDING * 2))
        mage_text = REG_FONT.render("MAGE: M", 1, P.RED)
        WIN.blit(mage_text, ((P.WIDTH - mage_text.get_width())//2, P.PADDING * 3))
        ninja_text = REG_FONT.render("NINJA: N", 1, P.RED)
        WIN.blit(ninja_text, ((P.WIDTH - ninja_text.get_width())//2, P.PADDING * 5))
        leave_text = REG_FONT.render("LEAVE: L", 1, P.WHITE)
        WIN.blit(leave_text, ((P.WIDTH - leave_text.get_width())//2, P.PADDING * 8))
        if knight == None:
                knight_text = REG_FONT.render("KNIGHT: K", 1, P.GREEN)
                WIN.blit(knight_text, ((P.WIDTH - knight_text.get_width())//2, P.PADDING * 6))
        if tactician == None:
                tactician_text = REG_FONT.render("TACTICIAN: T", 1, P.BLUE)
                WIN.blit(tactician_text, ((P.WIDTH - tactician_text.get_width())//2, P.PADDING * 7))
        if summoner == None:
                summoner_text = REG_FONT.render("SUMMONER: S", 1, P.BLUE)
                WIN.blit(summoner_text, ((P.WIDTH - summoner_text.get_width())//2, P.PADDING * 4))
        
#function will list options for the player
def draw_menu():
	attack_text = REG_FONT.render("ATTACK monsters: A", 1, P.RED)
	WIN.blit(attack_text, (P.WIDTH//2 - attack_text.get_width(), P.PADDING))
	save_text = REG_FONT.render("RECORD journey: R", 1, P.BLACK)
	WIN.blit(save_text, (P.WIDTH//2 - save_text.get_width(),
			     P.PADDING * 2))
	city_text = REG_FONT.render("return to CITY: C", 1, P.BLACK)
	WIN.blit(city_text, (P.WIDTH//2 - city_text.get_width(),
			     P.PADDING * 3))
	leave_text = REG_FONT.render("SLEEP: S", 1, P.RED)
	WIN.blit(leave_text, (P.WIDTH//2 - leave_text.get_width(),
			      P.PADDING * 4))
	
