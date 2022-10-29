class Dog:
    def __init__(self, color): # constructor
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
    


rac = Dog("white")
zombie = Dog("gray")

print(rac.get_color())
print(zombie.color)

zombie.set_color("Caca")
print(zombie.get_color())
        