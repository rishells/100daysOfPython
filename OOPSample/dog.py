class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initiatilze name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a commmand"""
        return self.name.title() + " is now sitting."

    def roll(self):
        """simulate rolling over in response to a command"""
        return self.name.title() + " rolled over!"


first_dog = Dog("Rac",10)

print(first_dog.sit())
# print(first_dog.roll())
# print(first_dog.age)