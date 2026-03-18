"""
Laboratory Work №1
Author: Masalova Lolita Dmitrievna
Date: 08.03.2026
"""

from modules.task1 import sin_taylor, math_sin
from modules.task2 import process_task2
from modules.task3 import count_punc
from Services.output import print_result_task2, print_table_row, print_table_footer, print_table_header
from Services.input import get_input_integers, get_int_input, get_natural_input, generate_random_list, get_float_input, get_input_string

import modules

def run_task2():
    print("\n--- Task 2 Menu ---")
    print("\n1. Manual input")
    print("\n2. Generate random sequence")

    choice = get_natural_input("\nChoice:")

    if choice == 1:
        lst = get_input_integers()

    else:
        size = get_natural_input("\nEnter sequence size: " )
        lst = generate_random_list(size)

    print(f"Sequence: {lst}")
    total_sum, count = process_task2(lst)

    print_result_task2(total_sum, count)

def run_task1():
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

    print("\n--- Task 3 ---")
    str1 = get_input_string("Input a text:")

    print(f"Total punctuation marks found:{count_punc(str1)}")



def main():
    """Main menu of the program"""
    while True:
        print("\n=== Laboratory Work №1 ===")
        print("1. Run Task 1 (Taylor sin)")
        print("2. Run Task 2 (Sequence analysis)")
        print("3. Run Task 3 (Text analysis)")
        print("0. Exit")

        cmd = get_int_input("\nSelected task:")
        if cmd == 1:
            run_task1()
        elif cmd == 2:
            run_task2()
        elif cmd == 3:
            run_task3()
        elif cmd == 0:
            break

if __name__ == "__main__":
    main()

