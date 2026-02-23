import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block(self):
        block_amount = random.randint(0, self.max_block)

        return block_amount


if __name__ == '__main__':
    armor = Armor('Golden Shield', 7)
    print(armor.name)
    print(armor.block())