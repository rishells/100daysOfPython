# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
import random

names = ["Ricardo", "Axel", "Yadira", "Perla", "Abraham"]
students_scores = {student:random.randint(1,100) for student in names}

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

##### Exercise # 1 By using dictionary comprehension print the number of characters of each word of a string ######

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence_list = sentence.split(" ")

# for word in sentence.split():
#     print(word)
#sentence_word_counter = {}
sentence_word_counter = {word:len(word) for word in sentence.split()} # Dictionary comprehension statement
#print(sentence_word_counter)

##### Exercise # 2 By using dictionary comprehension convert a dictionary temperatures from C to F

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# (temp_c * 9/5) + 32 = temp_f
weather_f = {day:(temp_c* 9/5 + 32) for (day, temp_c) in weather_c.items()}

print(weather_f)