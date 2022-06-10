from math import *
import random
import time
# Author: @Austin Repine
# This program asks the user how many problems the user would like to do.
# Once it has the amount of problems, it then-
# -creates two random integers.
# It asks the user to solve the various math problems from Addition to Division.
# Future math equations/functionality are in the works.
start_time = time.time()
class MathFunctions():
    def __init__(self) -> None:
        pass

# This function creates a random integer from 1 - 10
# and returns that value.
def random_function():
    return random.randint(1, 10)

# This function takes the two random integers and
# returns the two values added together.
def add_function(num1, num2):
    return num1 + num2

# This function takes the two random integers and returns the two values subtracted.
def sub_function(num1, num2):
    return num1 - num2

# This is a reverse function of the subtraction function
# for when the second integer is larger than the first integer.
def reverse_sub(num1, num2):
    return num2 - num1

# This function takes the two random integers
# and multiplies them, then returns that value.
def multiply_function(num1, num2):
    return num1 * num2

# This function takes the two random integers
# and divides them, then returns that value.
def divide_function(num1, num2):
    return round(num1 / num2, 2)

# This function takes the two random integers
# adds them together, and multiplies them both by pi.
def pi_function(added_number):
    return (added_number)*pi

# This function takes two random integers,
# and tells which one is greater than the other one and by how much.
def is_greater(num1, num2):
    if num1 > num2:
        num_diff = sub_function(num1, num2)
        print(f'{num1} > {num2} by {num_diff}')
    else:
        num_diff = reverse_sub(num1, num2)
        print(f'{num2} > {num1} by {num_diff}')
    return num_diff



i = 0
problems = int(input("How many problems would you like to do? "))

print (f"""Ok, you will do {problems} problems in which you must
do all four functions (Addition, Subtraction, Multiplication, and Division).""")
while i < problems:
    num1 = random_function()
    num2 = random_function()
    myNums = []
    myNums.append(num1)
    myNums.append(num2)
    # This anonymous function squares the random integers added to the lists to be used in conjunction with other functions.
    lst = list(map(lambda num: num**2, myNums))
    is_greater(num1, num2)

    print(f'What are the two variables {num1}, {num2} added together? {num1}+{num2}= ')
    userAnswer = int(input())
    a_answer = add_function(num1, num2)
    if userAnswer == a_answer:
        print("You are correct!")
    elif userAnswer != a_answer:
        print(f'Sorry that was wrong. {a_answer} was the correct answer.')

    print(f'What are the two variables {num1}, {num2} subtracted? {num1}-{num2}= ')
    userAnswer = int(input())
    s_answer = sub_function(num1, num2)
    if userAnswer == s_answer:
        print("You are correct!")
    else:
        print(f'Sorry that was wrong. {s_answer} was the correct answer.')

    print(f'What are the two variables {num1}, {num2} multiplied together? {num1}*{num2}= ')
    userAnswer = int(input())
    m_answer = multiply_function(num1, num2)
    if userAnswer == m_answer:
        print("You are correct!")
    elif userAnswer != m_answer:
        print(f'Sorry that was wrong. {m_answer} was the correct answer.')

    print(f'What are the two variables {num1}, {num2} divided by each other? (Round to the hundredths place) {num1}/{num2}=')
    userAnswer = float(input())
    d_answer =  divide_function(num1, num2)
    if userAnswer == d_answer:
        print("You are correct!")
    elif userAnswer != d_answer:
        print(f'Sorry that was wrong. {d_answer} was the correct answer.')

    print(f'Bonus question!!!!\nThe two numbers have been added to create: {a_answer}. What is {a_answer} multiplied by pi (3.14): ')
    userAnswer = float(input())
    pi_answer = pi_function(a_answer)
    if userAnswer == pi_answer:
        print("You are fantastically correct!")
    else:
        print(f"Wrong, the correct answer was: {pi_answer}...\nGo learn bro...")

    i += 1
end_time = time.time() - start_time
print(end_time)
