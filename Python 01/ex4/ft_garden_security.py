class SecurePlant:
    def __init__(self, name, height , age):
        self.__name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)
    def set_height(self, height):
        if height < 0 :
            print(f"Invalid operation attempted: height {height} cm [REJECTED]\nSecurity: Negative height rejected\n")
        else :
            self.__height = height
            print(f"Height updated: {height}cm [OK]")
    def set_age(self, age):
        if age < 0 :
            print(f"Invalid operation attempted: age {age} [REJECTED]\nSecurity: Negative height rejected\n")
        else :
            self.__age = age
            print(f"Age updated: {age} days [OK]\n")
    def get_height(self):
        return self.__height
    def get_age(self):
        return self.__age
    def get_info(self):
        return f"Current plant: {self.__name} ({self.__height}cm, {self.__age} days)"

if __name__ == "__main__":
    print("=== Garden Security System ===")
    p = SecurePlant("Rose", 13, 3)
    p.set_height(-1)
    print(p.get_info())
