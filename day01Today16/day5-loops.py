# fruits = ["apple","pear","banana"]
# colors = ["red, green, blue"]
# for fruit in fruits:
#     for color in colors:
#         print(fruit + " " + color)
#-------------------------Average Heights ---------------------------------
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# print(student_heights)
#average_heights = sum(student_heights) / len(student_heights)
#print(round(average_heights))
# sum_of_heights = 0
# counter = 0
# for height in student_heights:
#     sum_of_heights += height
#     counter += 1

# print("Sum of heights " + str(sum_of_heights))
# print("elements in the heights lists " + str(counter))
# print(f"Average of the heights:  {round(int(sum_of_heights)/int(counter))}")
#-------------------------Highest Score ---------------------------------
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score

# print(f"The highest score in the class is: {highest_score}")
# print(f"The highest score in the class is: {max(student_scores)}")
#-------------------------Range for loop ---------------------------------
# total = 0
# for number in range(1,101):
#     total += number
# print(total)
#-------------------------Sum of the even numbers from 1 to 100 ---------------------------------
# 2 + 4 + 6 ... + 100
# sum_of_even_numbers = 0
# for number in range(1,101):
#     if number % 2 == 0:
#         sum_of_even_numbers += number
# print(sum_of_even_numbers)

# sum_of_even_numbers2 = 0
# for number in range(2,101,2):
#     sum_of_even_numbers2 += number
# print(sum_of_even_numbers2)
#-------------------------FizzBuzz---------------------------------
#Count from 1 to 100 and when it's divisible by 3 print Fizz, when it's divisible by 5 print Buzz and when it's divisible by both print FizzBuzz
# for number in range(1,101):
#     if  number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)
#-------------------------Password Generator---------------------------------
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#password_generated = letters
letters_module = ""
for i in range(0,nr_letters):
    letters_module += letters[random.randint(0,len(letters)-1)] # random.choice(letters)

symbols_module = ""
for i in range(0,nr_symbols):
    symbols_module += symbols[random.randint(0,len(symbols)-1)]

numbers_module = ""   
for i in range(0,nr_numbers):
    numbers_module += numbers[random.randint(0,len(numbers)-1)]

concatenated_modules = letters_module + symbols_module + numbers_module
final_password = ''.join(random.sample(concatenated_modules,(len(concatenated_modules))))
print(f"Here's your password: {final_password}")

# >>> print(''.join(letters))
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ


#-------------------------Password Generator 2nd solution---------------------------------
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")
