class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f'{self.name} is eating')
         
    def drink(self):
        print(f'{self.name} is drinking')

class Frog(Animal):
    def jump(self):

        print(f'{self.name} is jumping')


if __name__ == '__main__':
    horse = Animal("Larry the Horse")
    horse.eat()
    horse.drink()

    froggy = Frog("Prince")
    froggy.jump()
    froggy.eat()
    froggy.drink()
