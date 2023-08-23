#Write your code below this line 👇
import math
import os
os.system('cls')


# def paint_calc(height,width,cover):
    
#     number_of_cans = (test_h * test_w) / coverage
#     print(f"You'll need {math.ceil(number_of_cans)} cans of paint")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#--------------------------------------- Prime numbers -------------------------------
#Write your code below this line 👇

# def prime_checker(number):
#     counter = 1
#     for i in range(1,number):
#         if number % i == 0:
#             counter +=1
#     if counter > 2:
#         print("It's not a prime number.")
#     else:
#         print("It's a prime number.")
# def prime_checker2(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)
#--------------------------------------- Caesar Cipher -------------------------------
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def caesar(text, direction, shift):
#     if direction == 'encode':
#         cipher_text = ""
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position + shift
#             cipher_text += alphabet[new_position]
#         print(f"The encoded text is {cipher_text}")

#     elif direction == 'decode':
#         decrypted_text =""
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position - shift
#             decrypted_text += alphabet[new_position]
#         print(f"The decoded text is {decrypted_text}")
#     else:
#         print("Provide a proper option")

# caesar(text, direction, shift)
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")


# def decrypt(cypher_text, shift_amount):
#     decrypted_text =""
#     for letter in cypher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         decrypted_text += alphabet[new_position]
#     print(f"The decoded text is {decrypted_text}")

################################### second solution ########################################
from day8_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 



should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    shift = shift % 26



    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type no.\n" )
    if result == "no":
        print("Bye.")
        should_continue = False
