"""
Task №2: Sum of sequence and counting even natural numbers.
"""
from Services.decorator import log_decorator

def count_even_natural(arr):

    """
    Counts and returns the number of even natural numbers in the list.
    :param arr: list of integers
    :return: count of even natural numbers
    """
    count = 0
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




