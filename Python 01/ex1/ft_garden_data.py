class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def display(self):
        print(f"{self.name}: {self.height}cm tall, {self.age} days old")

carrot = Plant("carrot", 12, 32)
sunflower = Plant("sunflower", 4, 344)
Cactus = Plant("Cactus", 34, 57888)
print("=== Garden Plant Registry ===")
carrot.display()
sunflower.display()
Cactus.display()