#from cgitb import text
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# QUIZ DB https://opentdb.com/api_config.php

# Write a for loop to iterate over the dictionary question_data
# Create a Question object from each entry in question_data
# Append each Question object to the question bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

    # print(question)
    # question_n = Question(question_bank[text],question_bank[answer])
    # question_bank.append(question_n)

# print(question_bank[0].text)
# print(question_bank[0].answer)

# Initialize the QuizBrain

# Create a new quiz object and initialize it
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    

print(f"You've completed the quiz\nYour final score was {quiz.score}")
    