"""
Task №2: Sum of sequence and counting even natural numbers.
"""
from Services.decorator import log_decorator
def count_even_natural(arr):
    count = 0
    """
    Reads integers from the user until 0 is entered.
    Counts and returns the number of even natural numbers.
    :param arr: list
    :return: count of even natural number 
    """
    for elem in arr:
        if elem > 0 and elem % 2 == 0:
            count += 1
    return count

def calculate_sum(arr):
    """
    Calculates the sum of all elements in the list.
    :param arr: list of numbers
    :return: sum of elements
    """
    summa = 0

    for elem in arr:
        summa += elem

    return summa

@log_decorator
def process_task2(arr):
    """
    Function that performs all calculations for Task 2.
    :param arr: list of integers
    :return: (sum, count_even)
    """

    s = calculate_sum(arr)
    c = count_even_natural(arr)
    return s, c




