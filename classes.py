class UncleJoeAnimal:

    dct_obj = {}
    def __init__(self, name, weight, feed, benefit, sound):
        self.name = name
        self.weight = weight
        self.feed = feed
        self.benefit = benefit
        self.sound = sound
        UncleJoeAnimal.dct_obj[self.name] = self.weight

    def get_sound(self):
        print(f'{self.name} cry "{self.sound}"!')
    
    @classmethod
    def total_weight(cls):
        print(f'Общий вес всех животных: {sum(UncleJoeAnimal.dct_obj.values())}кг')

    @classmethod
    def heaviest(cls):
        k = list(UncleJoeAnimal.dct_obj.keys())
        v = list(UncleJoeAnimal.dct_obj.values())
        print(f'Самое тяжелое животное - "{k [v.index(max(v))]}"')

class Animal(UncleJoeAnimal):

    feed_residue = 100
    def animal_feeding(self):
        if Animal.feed_residue >= 5:
            Animal.feed_residue -= self.feed
            if Animal.feed_residue >= 20:
                print(f'"{self.name}" покормлен(а)')
            elif 5 < Animal.feed_residue <20:
                print(f'"{self.name}" покормлена. Корм для животных заканчивается!')
        else:
            print('Кормить птицу нечем. Необходимо пополнить запас корма для животных!')

class Bird(UncleJoeAnimal):

    feed_residue = 6.5
    def bird_feeding(self):
        if Bird.feed_residue > 0.5:
            Bird.feed_residue -= self.feed
            if Bird.feed_residue >= 5:
                print(f'"{self.name}" покормлена')
            elif 0.5 <= Bird.feed_residue <5:
                print(f'"{self.name}" покормлена. Корм для птиц заканчивается!')
        else:
            print('Кормить птицу нечем. Необходимо пополнить запас корма для птиц!')

class Goose(Bird):
    
    egg_store = 0
    def get_egg(self):
        Goose.egg_store += self.benefit
        print(f'Яйцо от "{self.name}" получено. Остаток гусиных яиц: {Goose.egg_store}')
        
goose1 = Goose('Grey', 10, 0.5, 1, 'Ga-ga-ga')
goose2 = Goose('White', 10, 0.5, 1, 'Ga-ga-ga')

class Cow(Animal):
    
    milk_store = 0
    def get_milk(self):
        Cow.milk_store += self.benefit
        print(f'"{self.name}" подоена. Остаток коровьего молока: {Cow.milk_store}л')

cow1 = Cow('Manka', 300, 6, 5, 'Moo')

class Sheep(Animal):

    wool_storage = 0
    def get_wool(self):
        Sheep.wool_storage += self.benefit
        print(f'"{self.name}" острижена. Остаток овечьей шерсти: {Sheep.wool_storage}кг')

sheep1 = Sheep('Barashek', 100, 4, 5, 'Be-e-e')
sheep2 = Sheep('Kudryavy', 100, 4, 5, 'Be-e-e')

class Hens(Bird):
    
    h_egg_store = 0
    def get_egg(self):
        Hens.h_egg_store += self.benefit
        print(f'Яйцо от "{self.name}" получено. Остаток куриных яиц: {Hens.h_egg_store}')

hen1 = Hens('Cococo', 3, 0.2, 1, 'Co-co-co')
hen2 = Hens('Kuckarecoo', 3, 0.2, 1, 'Co-co-co')

class Goat(Animal):

    milk_store = 0
    def get_milk(self):
        Goat.milk_store += self.benefit
        print(f'"{self.name}" подоена. Остаток козьего молока: {Goat.milk_store}л')

goat1 = Goat('Hoof', 50, 3, 4, 'Me-e-e')
goat2 = Goat('Horn', 50, 3, 4, 'Me-e-e')

class Duck(Bird):
    
    egg_store = 0
    def get_egg(self):
        Duck.egg_store += self.benefit
        print(f'Яйцо от "{self.name}" получено. Остаток утиных яиц: {Duck.egg_store}')

duck1 = Duck('Kryakva', 3, 0.2, 1, 'Crya-crya-crya')



goose1.bird_feeding()
goose2.bird_feeding()
hen1.bird_feeding()
hen2.bird_feeding()
duck1.bird_feeding()
cow1.animal_feeding()
sheep1.animal_feeding()
sheep2.animal_feeding()
goat1.animal_feeding()
goat2.animal_feeding()
print()
cow1.get_milk()
goat1.get_milk()
goat2.get_milk()
print()
sheep1.get_wool()
sheep2.get_wool()
print()
goose1.get_egg()
goose2.get_egg()
hen1.get_egg()
hen2.get_egg()
duck1.get_egg()
print()
UncleJoeAnimal.total_weight()
UncleJoeAnimal.heaviest()
print()
