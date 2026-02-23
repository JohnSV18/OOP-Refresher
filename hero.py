import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health = 100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def add_armor  (self, armor):
        self.armors.append(armor)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            ability_damage = ability.attack()
            total_damage += ability_damage
        return total_damage

    def defend(self):
        total_block = 0

        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        if defense > damage:
            damage_recieved = 0
        else:
            damage_recieved  = damage - defense
        
        if self.current_health - damage_recieved < 0:
            self.current_health = 0
        else:
            self.current_health -= damage_recieved


    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        if not self.abilities and not opponent.abilities:
            print("Draw")
        else:
            while self.current_health > 0 and opponent.current_health > 0:
                hero_attack = self.attack()
                opponent.take_damage(hero_attack)
                opponent_attack = opponent.attack()
                self.take_damage(opponent_attack)
            if self.current_health > 0:
                print(f'{self.name} Wins!')
            elif opponent.current_health > 0:
                print(f'{opponent.name} Wins!')
            else:
                print("It's a draw!")
        

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    ability = Ability("force field", 35)
    hero.add_ability(ability)
    hero.add_weapon(weapon)
    print(hero.attack())
