"""
Main entry point for the program. Provides a menu
to execute tasks 1 through 5 of the laboratory work.

Laboratory Work №1
python 3.14
Version: 1.0
Author: Masalova Lolita Dmitrievna
Date: 08.03.2026
"""
from itertools import product

from modules.task1 import sin_taylor, math_sin
from modules.task2 import process_task2
from modules.task3 import count_punc
from Services.output import print_result_task2, print_table_row, print_table_footer, print_table_header, print_result_task4, print_result_task5
from Services.input import get_input_integers, get_int_input, get_natural_input, generate_random_list, get_float_input, get_input_string, get_integers_until_zero

import modules

def run_task2():
    """
    Executes Task 2 with the 'stop at 0' logic.
    """
    print("\n--- Task 2 Menu ---")
    print("1. Manual input (stop by entering 0)")
    print("2. Generate random sequence")

    choice = get_natural_input("\nChoice: ")

    if choice == 1:
        lst = get_integers_until_zero()
    else:
        size = get_natural_input("\nEnter sequence size for random generation: ")
        lst = list(generate_random_list(size))

    if not lst:
        print("The sequence is empty.")
        return

    print(f"Sequence: {lst}")
    total_sum, count = process_task2(lst)

    print_result_task2(total_sum, count)


def run_task1():

    """
    Executes Task 1
    """
    print("--- Task 1 ---")

    x = get_float_input("Enter value for x: ")

    eps_choice = input("Enter precision eps (press Enter to use default 0.0001): ")
    if eps_choice.strip() == "":
        eps = 0.0001
    else:
        try:
            eps = float(eps_choice)
        except ValueError:
            print("Invalid input for eps. Using default 0.0001")
            eps = 0.0001

    taylor_result, n_iterations = sin_taylor(x, eps)
    math_result = math_sin(x)

    print_table_header()
    print_table_row(x, n_iterations, taylor_result, math_result, eps)
    print_table_footer()


def run_task3():

    """
    Executes Task 3
    """
    print("\n--- Task 3 ---")
    str1 = get_input_string("Input a text:")

    print(f"Total punctuation marks found:{count_punc(str1)}")

def run_task4():

    """
    Executes Task 4
    """
    print("\n --- Task 4 ---")
    print_result_task4()

def run_task5():

    """
    Executes Task 5
    """
    print("\n--- Task 5 Menu ---")
    print("1. Manual input")
    print("2. Generate random sequence")

    choice = get_natural_input("\nChoice:")

    if choice == 1:
        lst = get_input_integers()

    else:
        size = get_natural_input("\nEnter sequence size: " )
        lst = list(generate_random_list(size))

    print(f"Sequence: {lst}")
    print_result_task5(lst)


def main():
    """
    Main menu of the program
    """
    while True:
        print("\n=== Laboratory Work №1 ===")
        print("1. Run Task 1 (Taylor sin)")
        print("2. Run Task 2 (Sequence analysis)")
        print("3. Run Task 3 (Text analysis)")
        print("4. Run Task 4 (Text analysis)")
        print("5. Run Task 5 (Sequence analysis)")
        print("0. Exit")

        cmd = get_int_input("\nSelected task:")
        if cmd == 1:
            run_task1()
        elif cmd == 2:
            run_task2()
        elif cmd == 3:
            run_task3()
        elif cmd == 4:
            run_task4()
        elif cmd == 5:
            run_task5()
        elif cmd == 0:
            break
        else:
            print("Please, choose the number of the task(from 0 to 5)")


if __name__ == "__main__":
    main()

