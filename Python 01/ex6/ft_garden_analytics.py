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
                    score += p.points
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
    def create_garden_network(cls, capacity):
        return cls()
    
    @staticmethod
    def validate_height(height):
        return 10 <= height
    
    def garden_report(self, garden_name):
        if garden_name not in self.gardens:
            print("Garden not found!")
            return
        
        plants = self.gardens[garden_name]
        stats = self.Garden_Stats()
        
        print(f"\n=== {garden_name}'s Garden Report ===")
        print("Plants in garden:")
        for p in plants:
            if isinstance(p, PrizeFlower):
                print(f"- {p.name}: {p.height}cm, {p.color.lower()} flowers (blooming), Prize points: {p.points}")
            elif isinstance(p, FloweringPlant):
                print(f"- {p.name}: {p.height}cm, {p.color.lower()} flowers (blooming)")
            else:
                print(f"- {p.name}: {p.height}cm")
        
        num_plants = stats.numbers_of_plants(plants)
        total_growth = sum(1 for p in plants)
        print(f"Plants added: {num_plants}, Total growth: {total_growth}cm")
        print(stats.plants_types(plants))
    


if __name__ == "__main__":

    bob_manager = GardenManager.create_garden_network(3)
    p4 = Plant("Cactus", 92, 10)
    bob_manager.gardens["Bob"] = [p4]
    
    print("=== Garden Management System Demo ===")
    
    my_manager = GardenManager.create_garden_network(5)

    p1 = Plant("Oak Tree", 100, 50)
    p2 = FloweringPlant("Rose", 25, 30, "red")
    p3 = PrizeFlower("Sunflower", 80, 60, "yellow", 10)

    my_manager.add_plant("Alice", p1)
    my_manager.add_plant("Alice", p2)
    my_manager.add_plant("Alice", p3)
    my_manager.grow_all("Alice")

    my_manager.garden_report("Alice")

    test_height = 15
    is_valid = GardenManager.validate_height(test_height)
    print(f"Height validation test: {is_valid}")

    stats = GardenManager.Garden_Stats()
    alice_score = stats.points_count(my_manager.gardens["Alice"])
    bob_score = stats.points_count(bob_manager.gardens["Bob"])
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    
    print(f"Total gardens managed: {GardenManager.total_manager}")