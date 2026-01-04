class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def get_info(self):
        return f"Created: {self.name} ({self.height}cm, {self.days} days)"


if __name__ == "__main__":
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = []
    for i in range(len(plant_data)):
        name = plant_data[i][0]
        height = plant_data[i][1]
        days = plant_data[i][2]
        plants.append(Plant(name, height, days))
    print("=== Plant Factory Output ===")
    for j in plants:
        print(j.get_info())
    print(f"\nTotal plants created: {len(plants)}")
