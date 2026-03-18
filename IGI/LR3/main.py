"""
Laboratory Work №1
Author: Masalova Lolita Dmitrievna
Date: 08.03.2026
"""

from modules.task2 import process_task2
from Services.output import print_result_task2
from Services.input import get_input_integers, get_int_input, get_natural_input, generate_random_list
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

def main():
    """Main menu of the program"""
    while True:
        print("\n=== Laboratory Work №1 ===")
        print("1. Run Task 1 (Taylor sin)")
        print("2. Run Task 2 (Sequence analysis)")
        print("0. Exit")

        cmd = get_int_input("\nSelected task:")
        if cmd == 1:
            pass
        elif cmd == 2:
            run_task2()
        elif cmd == 0:
            break

if __name__ == "__main__":
    main()

