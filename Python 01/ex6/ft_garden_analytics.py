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
                    p.points += 1
            return score
    