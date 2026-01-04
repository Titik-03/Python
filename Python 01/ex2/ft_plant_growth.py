class Plant:
    def __init__(self, name, height, aged):
        self.name = name
        self.height = height
        self.aged = aged

    def grow(self):
        self.height += 1

    def age(self):
        self.aged += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm tall, {self.aged} days old"


if __name__ == "__main__":
    plant = Plant("carrot", 12, 1)
    print("=== Day 1 ===")
    print(plant.get_info())
    print("=== Day 7 ===")
    for i in range(6):
        plant.grow()
        plant.age()
    print(plant.get_info())
    g = 12 - 7
    print(f"Growth this week: +{g}cm")
