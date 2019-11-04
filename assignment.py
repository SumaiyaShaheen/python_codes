import math
import sys
from datetime import datetime
def assignment1():
    print("Q1-> Write a Python program to print the following string in a specific format \n Q2-> Write a Python program to get the Python version you are using \n Q3-> Write a Python program to display the current date and time. \n Q4-> Write a Python program which accepts the radius of a circle from the user and compute the area. \n Q5-> Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. \n Q6-> Write a python program which takes two inputs from user and print them addition")
    choice = int(input(" my choice is   "))
    if choice==1:
        print("Twinkle, twinkle, little star, \n \t How I wonder what you are! \n \t \t Up above the world so high, \n \t \t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n \t How I wonder what you are")
    elif choice==2:
        print (sys.version)
    elif choice==3:
        now = datetime.now()
        print("Today's date:", now)
        curretH=now.time()
        print(curretH)

    elif choice==4:
        radius = int(input("Enter the radius of circle"))
        area = math.pi *radius *radius
        print(area)
    elif choice==5:
        first_name = input(" Enter you'r first name     ")
        second_name = input(" Enter you'r second name      ")
        name = second_name + " " + first_name
        print(name)
    elif choice==6:
        num_1 = int(input("Enter first number   "))
        num_2 = int(input("Enter Second number  "))
        result = num_1 + num_2
        print("The addition of ", num_1, " and ", num_2, " is ", result)


assignment1()

