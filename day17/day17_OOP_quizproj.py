# A class is a blueprint

class User:
    # Constructor initialize an object with the __init__ function and then initialize the attributes
    # This function is called every time a new object is created

    def __init__(self,user_id,username): # define the object and the attributes 
        self.id = user_id
        self.username = username
        self.followers = 0 # default values can be put in the constructor to asign this value to all the new objects created
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "conchasp")
user_2 = User("002", "mendozay3")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)






# user_2 = User("002","mendozay3")
# print(user_2.followers)

# attributes are added with (.) dot notation after the name of the object

# creation of objects without constructor initialization
# user_1 = User()
# user_1.id = "001"
# user_1.username = "conchasp"





