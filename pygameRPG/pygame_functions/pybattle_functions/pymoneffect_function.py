import copy
import random
import sys
from rpg2_classdefinitions import (Player_PC, Monster_NPC, Armor_PC)
from rpg2_constants import Constants
import pyparty_functions as party_func
from rpg2_constant_lists import List_Constants
L = List_Constants()
C = Constants()
sys.path.append(".")
import pyelement_function as element_func
import pyeqpeffect_function as ee_func
#function that checks what kind of buffs the monster has
def monster_def_buff_effect(m_npc, atk, p_pc, h_p, wpn, h_a, m_p):
	new_atk = max(atk - m_npc.defense, 1)
	if m_npc.buff == None:
		new_atk = new_atk
	else:
		if "AA" in m_npc.buff:
			if wpn.element in m_npc.buff:
				new_atk = -new_atk
				print (m_npc.name, "absorbs the attack of", p_pc.name)
		if "PoisonHeal" in m_npc.buff:
			m_npc.health += m_npc.poison * C.INCREASE_EXPONENT
			m_npc.poison -= new_atk
			new_atk -= m_npc.poison
			print (m_npc.name, "seems to regenerate from poison. ")
		if "DmgVoid" in m_npc.buff:
			if "DmgVoidA" in m_npc.buff:
				if new_atk > C.DMG_A:
					new_atk = 0
				print (m_npc.name, "negates the attack of ", p_pc.name)
			elif "DmgVoidB" in m_npc.buff:
				if new_atk > C.DMG_B:
					new_atk = 0
				print (m_npc.name, "negates the attack of ", p_pc.name)
			
	return new_atk
#function that checks monster
def monster_buff_check_spell(m_npc, p_pc, spell, atk):
	new_atk = atk + p_pc.mana
	if m_npc.buff == None:
		new_atk = new_atk
	else:
		if "AA" in m_npc.buff:
			if spell.element in m_npc.buff:
				new_atk = -new_atk
				print (m_npc.name, "absorbs the attack of", p_pc.name)
		if "DmgVoid" in m_npc.buff:
			if "DmgVoidA" in m_npc.buff:
				if new_atk > C.DMG_A:
					new_atk = 0
				print (m_npc.name, "negates the attack of ", p_pc.name)
			elif "DmgVoidB" in m_npc.buff:
				if new_atk > C.DMG_B:
					new_atk = 0
				print (m_npc.name, "negates the attack of ", p_pc.name)
		if "PoisonHeal" in m_npc.buff:
			new_atk -= m_npc.poison
			m_npc.health += m_npc.poison * C.INCREASE_EXPONENT
			m_npc.poison -= p_pc.mana + atk
			print (m_npc.name, "seems to regenerate from poison. ")
		if "MagicResist" in m_npc.buff:
			if "MagicResistA" in m_npc.buff:
				new_atk = new_atk//2
			elif "MagicResistB" in m_npc.buff:
				new_atk = new_atk//4
	return new_atk
#function that checks what kind of passives a monster has
def monster_passive_effect(m_npc, p_pc, h_p, m_p):
	for passive in L.MONSTER_PASSIVE_LIST:
		if passive in m_npc.name:
			if passive == "Fire":
				p_pc.health -= m_npc.skill
				print (p_pc.name, "is burned by", m_npc.name)
				num = random.randint(0, p_pc.health)
				if num <= m_npc.skill:
					if p_pc.status == None:
						p_pc.status = "Burn"
					elif "Burn" not in p_pc.status:
						p_pc.status += " Burn"
			if passive == "Water":
				p_pc.atkbonus -= min(m_npc.skill, p_pc.atkbonus)
				print (p_pc.name, "is bogged down by", m_npc.name)
			if passive == "Air":
				p_pc.skill -= 1
				print (p_pc.name, "is distracted by", m_npc.name)
			if passive == "Earth":
				m_npc.defense += m_npc.skill//4
				print (m_npc.name, "hardens. ")
			if passive == "Dark":
				m_npc.skill += 1
				print ("Darkness swirls around", m_npc.name)
			if passive == "Demon":
				for mon in m_p:
					m_npc.skill += 1
				print (m_npc.name, "empowers its allies. ")
			if passive == "Slime":
				if m_npc.health > m_npc.skill + m_npc.atk:
					x = random.randint(0, len(m_p))
					if x == 0:
						m_npc.health = m_npc.health//3
						copy_mon = copy.copy(m_npc)
						m_p.append(copy_mon)
						print (m_npc.name, "splits! ")
			if passive == "Skeleton":
				p_pc.defbonus -= min(m_npc.skill//4, p_pc.defbonus)
				print (p_pc.name+" feels the decaying power of "+m_npc.name)
			if passive == "Beast":
				m_npc.atk += m_npc.skill//2
				print (m_npc.name, "howls.")
			if passive == "Elemental":
				x = random.randint(0, 3)
				if x == 0:
					m_npc.health += m_npc.skill
				elif x == 1:
					m_npc.atk += m_npc.skill
				elif x == 2:
					m_npc.defense += m_npc.skill
				elif x == 3:
					m_npc.skill += 1
				print (m_npc.name, "pulses erratically. ")
			if passive == "Troll":
				if m_npc.poison == 0 and "Burn" not in m_npc.status:
					m_npc.health += m_npc.skill
					print (m_npc.name, "regenerates. ")
			if passive == "Goblin":
				x = random.randint(0, 2)
				if x == 0:
					p_pc.health -= m_npc.skill
					print ("The goblin stabs", p_pc.name, "with a hidden dagger. ")
				elif x == 1:
					p_pc.atkbonus -= min(m_npc.skill, p_pc.atkbonus)
					print ("The goblin trips", p_pc.name, "with a hidden stick. ")
				elif x == 2:
					p_pc.defbonus -= min(m_npc.skill, p_pc.defbonus)
					print ("The goblin blinds", p_pc.name, "with a handful of dirt. ")
			if passive == "Orc":
				m_npc.atk += len(m_p)
				m_npc.defense += len(m_p)
				print (m_npc.name, "roars. ")
			if passive == "Bomb":
				m_npc.health -= m_npc.skill
				if m_npc.health > 0:
					if m_npc.element == "Poison":
						for mon in m_p:
							mon.poison += 1
					elif m_npc.element == "Blast":
						for mon in m_p:
							mon.health -= m_npc.skill
				elif m_npc.health <= 0:
					print (m_npc.name, "explodes! ")
					if m_npc.element == "Poison":
						for mon in m_p:
							mon.poison += m_npc.skill
						print ("Poison gas surrounds the monsters. ")
					elif m_npc.element == "Blast":
						for mon in m_p:
							mon.health -= C.BOMB_DAMAGE
							mon.health -= m_npc.skill
						print ("Shrapnel pieces fly at the monsters. ")

			if passive == "Giant":
				m_npc.atk += m_npc.skill
				m_npc.skill += 1
				print (m_npc.name, "begins to warm up. ")
