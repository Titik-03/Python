class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
class Vegetables(Plant):
    def __init__(self, name, height, days, harvest_season):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
    def nutritional_value(self):
        print(f"{self.name} is rich in vitamin C\n")
    def get_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.days} days, {self.harvest_season}")
class Flower(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color
    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")
    def get_info(self):
        print(f"{self.name} (Flower):{self.height}cm, {self.days} days, {self.color} color")
class Tree(Plant):
    def __init__(self, name, height, days, trunk_diameter):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        r = self.height * self.trunk_diameter / 320
        print(f"{self.name} provides {r} square meters of shade\n")
    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.days} days, {self.trunk_diameter}cm diameter")
if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    
    rose = Flower("Rose", 25, 30, "red")
    rose.get_info()
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    oak.get_info()
    oak.produce_shade()

    tomato = Vegetables("Tomato", 80, 90, "summer harvest")
    tomato.get_info()
    tomato.nutritional_value()
