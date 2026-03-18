"""
Service: Input handlers
"""

import random

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
    n = get_natural_input("\n Enter size of array of integers:")

    for i in range(n):
        num = get_int_input(f"Enter {i+1} number: ")
        lst.append(num)
    return lst

def generate_random_list(size):
    """Random generator"""
    lst = []
    for _ in range(size):
        num = random.randint(-100, 100)
        lst.append(num)
    return lst
