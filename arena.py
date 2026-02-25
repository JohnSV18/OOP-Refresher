from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
import random

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input('What is the ability name? ')
        max_damage = int(input('What is the max damage of the ability? '))

        return Ability(name, max_damage)
    
    def create_weapon(self):
        # random_value = random.randint(self.max_damage // 2, self.max_damage)
        name = input('What is the name of your weapon? ')
        max_damage = int(input('What is the max damage of the weapon? '))
        weapon_max_damage = random.randint(max_damage // 2, max_damage)

        return Weapon(name, weapon_max_damage)
    
    def create_armor(self):
        name = input('What is the name of your armor? ')
        max_block = int(input('What is the max block for your armor? '))

        return Armor(name, max_block)
    
    def create_hero(self):
        hero_name = input('What is your heros name? ')
        hero = Hero(hero_name)

        add_item = None
        while add_item != '4':
            add_item = input ('[1] add ability \n[2] Add Weapon\n[3] Add Armor\n[4]Done adding items\n\n Your Choice: ')
            if add_item == "1":
            # TODO add an ability to the hero
            # HINT: First create the ability, then add it to the hero
                new_ability = self.create_ability()
                hero.add_ability(new_ability)

            elif add_item == "2":
                # TODO add a weapon to the hero
                # HINT: First create the weapon, then add it to the hero
                new_weapon = self.create_weapon()
                hero.add_weapon(new_weapon)
            elif add_item == "3":
                # TODO add an armor to the hero
                # HINT: First create the armor, then add it to the hero
                new_armor = self.create_armor()
                hero.add_armor(new_armor)
        return hero
        
    def build_team_one(self):
        team_one_name = input('What is your teams name? ')
        self.team_one = Team(team_one_name)
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.heroes.append(hero)
    
    def build_team_two(self):
        team_two_name = input('What is your teams name? ')
        self.team_two = Team(team_two_name)
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.heroes.append(hero)
    
    def team_battle(self):
        self.team_one.attack(self.team_two)
    
    def show_stats(self):

        alive_heroes = 0
        alive_opponents = 0
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f'{hero.name} Survives!')
                alive_heroes += 1
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f'{hero.name} Survives!')
                alive_opponents += 1

    
        if alive_heroes > alive_opponents:
            print("TEAM ONE IS THE WINNER!")
        elif alive_heroes < alive_opponents:
            print("TEAM TWO IS THE WINNER!")

        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

          # TODO: Now display the average K/D for Team Two
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

      

        # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        #TODO: Now list the heroes from Team Two that survived
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()