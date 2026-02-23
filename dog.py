class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print('Dog initialized!')

    def bark(self):
        print('woof!')
    
    def sit(self):
        print(f'{self.name} sits')

    def roll_over(self):
        print(f'{self.name} rolls over')


