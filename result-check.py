# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 02:24:31 2023

@author: user
"""

student_scores = list(range(101))

#Ask for user's name
def input_name():
    # Add your custom input name here
    user_name = input("Enter your name: ")
    return user_name

# Use the input name function
input_func = input_name

# Prompt the user for input
user_name = input_func()

# Print the input
print(f"Welcome {user_name}!")


#Ask for user's score
def input_score():
    user_score = int(input("Please enter your score: "))
    return user_score

#Use the input score function
input_func = input_score

#Prompt the user for score
user_score = input_func()

print(f"Your score is: {user_score}")

#To check whether the student passed, failed or had an excellent result
def result_check(user_score):
    if user_score > 70:
        return "Excellent!"
    elif user_score >= 60:
        return "Very good!"
    elif user_score >= 50:
        return "Fair!"
    elif user_score >= 45:
        return "Pass!"
    else:
        return "Fail!"
    
##Utilize the result checker function to print the result
result = result_check(user_score)
print(f"Score: {user_score} --> Result: {result}")