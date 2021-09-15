import random
import my_module

#print(my_module.pi) printing a value from a module file
# random_integer = random.randint(1,10)
# print(random_integer)
# random_float = random.random()
# print(random_float)
# randomFloat = random.random() * 5 # to get random Float in a scale larger than 1 you can multilpy by a number
# print(randomFloat)
#--------------------------------heads or tails-------------------------------------------------------
# random_value = random.randint(0,1)
# if random_value == 1:
#     print("heads")
# else:
#     print("tails")
#--------------------------------------Lists -----------------------------------------------------------------
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# states_of_america.append("RicardoLand")
# states_of_america.extend(["Totoland", "RackLand"])
# print(states_of_america)
#--------------------------------------Lists -----------------------------------------------------------------
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# names_len = len(names)
# random_index = random.randint(0,names_len -1)
# print(f"{names[random_index]} is going to buy the meal today!")
# Nested lists
# cats = ["persian", "siames","bald"]
# dogs = ["husky","labrador","chihuahua"]
# animals = [cats,dogs]
# print(animals)
#--------------------------------------Treasure Map -----------------------------------------------------------------
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# # print(position[0])
# # print(type(position))
# column_index = position[0]
# row_index = position[1]
# map[int(row_index)-1][int(column_index)-1] = "X"

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")
#--------------------------------------Rock, Paper, Scissors -----------------------------------------------------------------

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Rock 0
# Paper 1
# Scissors 2

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
if user_choice == 0 and computer_choice == 0: # Rock, Rock
    print(rock,'\n')
    print("Computer chose:\n")
    print(rock,'\n')
    print("Draw")

elif user_choice == 1 and computer_choice == 1: # Paper, Paper
    print(paper)
    print("Computer chose:\n")
    print(paper,'\n')
    print("Draw")

elif user_choice == 2 and computer_choice == 2: # Scissors, Scissors
    print(scissors)
    print("Computer chose:\n")
    print(scissors,'\n')
    print("Draw")

elif user_choice ==0 and computer_choice == 1: # Rock, Paper
    print(rock)
    print("Computer chose:\n")
    print(paper,'\n')
    print("You lose")

elif user_choice == 0 and computer_choice == 2: # Rock, Scissors
    print(rock)
    print("Computer chose:\n")
    print(scissors,'\n')
    print("You win")

elif user_choice == 1 and computer_choice == 2: # Paper, Scissors
    print(paper)
    print("Computer chose:\n")
    print(scissors,'\n')
    print("You lose")

elif user_choice == 1 and computer_choice == 0: # Paper, Rock
    print(paper)
    print("Computer chose:\n")
    print(rock,'\n')
    print("You win")

elif user_choice == 2 and computer_choice == 1: # Scissors, Paper
    print(scissors)
    print("Computer chose:\n")
    print(paper,'\n')
    print("You win")

elif user_choice == 2 and computer_choice == 0: # Scissors, Rock
    print(scissors)
    print("Computer chose:\n")
    print(rock,'\n')
    print("You lose")


else:
    print("Choose a valid option ")
