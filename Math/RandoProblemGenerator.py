from audioop import add
import random
"""Author: @Austin Repine

This program asks the user how many problems the user would like to do. Once it has the amount of problems, it then-
-creates two random integers, then asks the user to solve the various math problems from Addition to Division. 

Future math equations/functionality are in the works.
"""

# This function creates a random integer from 1 - 10 and returns that value.
def randomFunction():
    return random.randint(1, 10)

# This function takes the two random integers and returns the two values added together.
def addFunction(num1, num2): 
    return num1 + num2

# This function takes the two random integers and returns the two values subtracted.
def subFunction(num1, num2):
    return num1 - num2

# This is a reverse function of the subtraction function for when the second integer is larger than the first integer.
def reverseSub(num1, num2):
    return num2 - num1

# This function takes the two random integers and multiplies them, then returns that value.
def multiplyFunction(num1, num2):
    return num1 * num2

# This function takes the two random integers and divides them, then returns that value.
def divideFunction(num1, num2):
    return round(num1 / num2, 2)

# This function takes two random integers, and tells which one is greater than the other one and by how much.
def is_greater(num1, num2):
    if num1 > num2:
        num_diff = subFunction(num1, num2)
        print(f'{num1} > {num2} by {num_diff}')
    else:
        num_diff = reverseSub(num1, num2)
        print(f'{num2} > {num1} by {num_diff}')
    return num_diff



i = 0
problems = int(input("How many problems would you like to do? "))

print (f"Ok, you will do {problems} problems in which you must do all four functions (Addition, Subtraction, Multiplication, and Division).")
while i < problems:
    num1 = randomFunction()
    num2 = randomFunction()
    myNums = []
    myNums.append(num1)
    myNums.append(num2)
    # This anonymous function squares the random integers added to the lists to be used in conjunction with other functions.
    lst = list(map(lambda num: num**2, myNums))
    is_greater(num1, num2)

    print("What are the two variables ", num1, ", ", num2, " added together? ", num1, " + ", num2, "= ")
    userAnswer = int(input())
    a_answer = addFunction(num1, num2)
    if userAnswer == a_answer:
        print("You are correct!")
    elif userAnswer != a_answer:
        print("Sorry, your answer is incorrect. The correct answer is: ", a_answer)

    print("What are the two variables ", num1, ", ", num2, " subtracted from each other? ", num1, " - ", num2, "= ")
    userAnswer = int(input())
    s_answer = subFunction(num1, num2)
    if userAnswer == s_answer:
        print("You are correct!")
    else:
        print("Sorry, your answer is incorrect. The correct answer is: ", s_answer)

    print("What are the two variables ", num1, ", ", num2, " multiplied together? ", num1, " * ", num2, "= ")
    userAnswer = int(input())
    m_answer = multiplyFunction(num1, num2)
    if userAnswer == m_answer:
        print("You are correct!")
    elif userAnswer != m_answer:
        print("Sorry, your answer is incorrect. The correct answer is: ", m_answer)

    print("What are the two variables ", num1, ", ", num2, " divided by each other? (Round to the one hundredth place) ", num1, " / ", num2, "= ")
    userAnswer = float(input())
    d_Answer =  divideFunction(num1, num2)
    if userAnswer == d_Answer:
        print("You are correct!")
    elif userAnswer != d_Answer:
        print("Sorry, your answer is incorrect. The correct answer is: ", d_Answer)

    
    i += 1

