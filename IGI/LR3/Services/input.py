"""
Service: Input handlers
"""

import random

def get_float_input(value):
    """Float input validation"""
    while True:
        try:
            return float(input(value))
        except ValueError:
            print("Error: Please enter a valid floating-point number.")

def get_int_input(value):
    """Integer input validation"""
    while True:
        try:
            return int(input(value))
        except ValueError:
            print ("Error: Please enter a valid integer.")

def get_natural_input(value):
    """Natural integer input validation"""
    while True:
        num = get_int_input(value)
        if num > 0:
            return num
        else:
            print("Error: Natural number must be greater than 0.")

def get_input_integers():
    lst = []
    n = get_natural_input("\nEnter size of array of integers:")

    for i in range(n):
        num = get_int_input(f"Enter {i+1} number: ")
        lst.append(num)
    return lst

def generate_random_list(size, start=-100, end=100):
    for _ in range(size):
        yield random.randint(start, end)

def get_input_string(str_input):
    while True:
        user_input = input(str_input)

        if len(user_input) > 0:
            return user_input
        else:
            print("Error: Please enter text.")



