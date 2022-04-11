class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self) -> None:
        
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water")

goldie = Fish()
rac = Animal()

goldie.breathe()
rac.breathe()