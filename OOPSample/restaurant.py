class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    
my_restaurant = Restaurant("Qin","Chinese Food")

# print(my_restaurant.restaurant_name)
# print(my_restaurant.cuisine_type)

my_2nd_restaurant = Restaurant("Sirloing","Steak House")
my_3rd_restaurant = Restaurant("Ali Corner", "Indian")


my_restaurant.open_restaurant()
my_2nd_restaurant.describe_restaurant()
my_3rd_restaurant.describe_restaurant()


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def describe_user(self):
        print(f"Your user request first name is {self.first_name} and his last name is {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome !")


first_user = User("Ricardo", "Conchas")

print(first_user.first_name)
print(first_user.last_name)

first_user.describe_user()
first_user.greet_user()

