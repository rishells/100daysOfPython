import math
import os
import random
import re
import sys


s = "abcac"
n = int(input("Number of characters to consider: "))

def repeatedString():
    # Write your code here
    final_string = ""
    # if len(s) < 10:
    #     final_string

def countA(s):
    counter = 0
    for letter in s:
        if letter == 'a':
            counter += 1
    print(f"Total number of a's in the string are {counter}")

def completeString(s):
    newString = ""
    if len(s) < n:
        newString = s + s
    return newString

if __name__ == '__main__':
    
    print(completeString(s))
    # s = input()

    # n = int(input().strip())

    # #result = repeatedString(s, n)
    # result = "hello"
    # print(result)
    