# la famila el del planto
class Plant:
    x = 0
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
    def grow(self, size=1):
        self.height += size
        print(f"{self.name} grew {size}cm")
class FloweringPlant(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, days, color, points):
        super().__init__(name, height, days, color)
        self.points = points
    
# el final boss
class GardenManager:
    total_manager = 0
    class Garden_Stats:
        def numbers_of_plants(self, plants):
            return len(plants)
        def plants_types(self, plants):
            regular = 0
            flowering = 0
            prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                elif isinstance(p, Plant):
                    regular += 1
            return f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers"
        def points_count(self, plants):
            score = 0
            for p in plants:
                score += p.height
                if isinstance(p, PrizeFlower):
                    score += p.point
            return score
    def __init__(self):
        self.gardens = {}
        GardenManager.total_manager += 1
    def add_plant(self, garden_name, plant):
            if garden_name not in self.gardens:
                self.gardens[garden_name] = []
            self.gardens[garden_name].append(plant)
            print(f"Added {plant.name} to {garden_name}'s garden")
    def grow_all(self, garden_name):
            print(f"{garden_name} is helping all plants grow...")
            if garden_name in self.gardens:
                plants_to_grow = self.gardens[garden_name]
                for p in plants_to_grow:
                    p.grow()
                else:
                    print("Garden not found!")
    @classmethod
    def create_garden_manager(cls, capacity):
        return cls











if __name__ == "__main__":
    my_manager = GardenManager.create_garden_network(5)

    p1 = Plant("Oak Tree", 100, 50)
    p2 = FloweringPlant("Rose", 25, 30, "Red")
    p3 = PrizeFlower("Sunflower", 80, 60, "Yellow", 10)
    p4 = Plant("Cactus", 91, 10)

    my_manager.add_plant("Alice", p1)
    my_manager.add_plant("Alice", p2)
    my_manager.add_plant("Alice", p3)
    my_manager.add_plant("bob", p4)

    my_manager.grow_all("Alice")

    test_height = 15
    is_valid = GardenManager.validate_height(test_height)
    print(f"Height validation test ({test_height}cm): {is_valid}")