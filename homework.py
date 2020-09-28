class Birds():
    food = ("Птичий корм")
    def feed(self):
        self.feed = food
    def collect(self):
        self.collect = eggs

class Goose(Birds):
    voice = "Га-га-га"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Chicken(Birds):
    voice = "Ко-ко-ко"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Duck(Birds):
    voice = "Кря-кря"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Animals():
    food = ("Трава")
    def feed(self):
        self.feed = food

class Cow(Animals):
    voice = "Му"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def milk(self):
        self.milk = milk

class Sheep(Animals):
    voice = "Ме"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def cut(self):
        self.cut = wool

class Goat(Animals):
    voice = "Бе"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

Goose1 = Goose("Серый", 4)
Goose2 = Goose("Белый", 3)
Cow1 = Cow("Манька", 30)
Sheep1 = Sheep("Барашек", 5)
Sheep2 = Sheep("Кудрявый", 6)
Chicken1 = Chicken("Ко-ко", 2)
Chicken2 = Chicken("Кукареку", 1.5)
Goat1 = Goat("Рога", 6)
Goat2 = Goat("Копыта", 8)
Duck1 = Duck("Кряква", 3)

Animals = {"Серый": 4, "Белый": 3, "Манька": 30, "Барашек": 5, "Кудрявый": 6, "Ко-ко": 2, "Кукареку": 1.5,
           "Рога": 6, "Копыта": 8, "Кряква": 3}

#for values in Animals:
    #print(f"Общий вес всех животных {sum(Animals.values())} кг")


a = Animals.keys()
b = Animals.values()
Animals1 = zip(a,b)
max_Animals = max(dict(Animals1))
print(f"Самое тяжелое животное - {max_Animals}")











