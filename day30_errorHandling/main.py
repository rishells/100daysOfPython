#FileNotFound


# try:
#     file = open("/home/rishells/rcdev/100daysOfPython/day30_errorHandling/a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])

# except FileNotFoundError:
#     file = open("/home/rishells/rcdev/100daysOfPython/day30_errorHandling/a_file.txt","w")
#     file.write("Something")


# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")

# else:
#     contnt = file.read()
#     print(content)

# finally:
#     raise TypeError("This an error that I made up.")
    # file.close()
    # print("File was closed.")

#Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

# 4 key words handling exceptions: try, except, else, finally
# try: something that might cause an exception
# except: Do this if there was an exception
# else: Do this if there were no exceptions
# finally: Do this no matter what happens


# height = float(input("Height in meters: "))
# weight = float(input("Weight in kg: "))
# bmi = round(weight / height ** 2 , 2)
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
# print(bmi)


# Index Error Example
# fruits = ["Apple", "Pear", "Orange"]

# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
   
# make_pie(4)

# Key Error Example

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2}, 
#     {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
#     {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
#     {'Likes': 33, 'Comments': 4, 'Shares': 2}, 
#     {'Comments': 1, 'Shares': 1}, 
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0

# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         total_likes = total_likes
    


# print(total_likes)

