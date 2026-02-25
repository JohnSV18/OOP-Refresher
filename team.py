import random
from hero import Hero

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)        

    def remove_hero(self, name):
        foundHero = False
        
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    
    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths = 1
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths: {kd}")

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    
    def attack(self, other_team):

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)
        
        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents) > 0:
            random_hero = random.choice(living_heroes)
            random_opp = random.choice(living_opponents)
            random_hero.fight(random_opp)

            if random_hero.current_health <= 0:
                living_heroes.remove(random_hero)
            elif random_opp.current_health <= 0:
                living_opponents.remove(random_opp)
            elif random_hero <=0 and random_opp <= 0:
                living_opponents.remove(random_opp)
                living_heroes.remove(random_hero)
        if len(living_heroes) <= 0:
            print('Team two wins!')
        elif len(living_opponents) <= 0:
            print('Team one wins!')
        elif len(living_opponents) <= 0 and len(living_heroes) <= 0:
            print('ITS A DRAW!')