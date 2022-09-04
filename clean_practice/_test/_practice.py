class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    
    def get_damage(self, damage):
        self.health -= damage

class Hero:
    def __init__(self, damage, monster: Monster):
        self.damage = damage
        self.monster = monster
    
    def attack(self):
        self.monster.get_damage(self.damage)

monster = Monster(100, 50)
hero = Hero(50, monster)
print(hero.monster.health)
print(monster.health)
hero.attack()
print (hero.monster.health)
print (monster.health)