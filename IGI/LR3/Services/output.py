"""
Service: Output handlers
"""

"""
Output for Task1
"""

from modules.task4 import correction_text, seventh_words, words_with_consonants_at_the_end,  average_length
from modules.task5 import sum_of_positive, product_elements

def print_table_header():
    """Prints table header"""
    print("\n" + "="*70)
    print(f"| {'x':^10} | {'n':^6} | {'F(x)':^15} | {'Math F(x)':^15} | {'eps':^10} |")
    print("="*70)

def print_table_row(x, n, f_x, math_f_x, eps):
    """Prints one table row"""
    print(f"| {x:^10.4f} | {n:^6} | {f_x:^15.10f} | {math_f_x:^15.10f} | {eps:^10.2e} |")

def print_table_footer():
    """Prints table footer"""
    print("="*70)

"""
Output for Task2
"""

def print_result_task2(summa, count):
    print(f"\nResult for Task 2")
    print(f"Sum of sequence: {summa}")
    print(f"Count of even natural numbers: {count}")

def print_result_task4():
    text = correction_text()

    print(f"Words end with a consonant letter: {words_with_consonants_at_the_end(text)}")
    print(f"Average length and words with average length: {average_length(text)}")
    print(f"Every seventh word: {seventh_words(text)}")

def print_result_task5(lst):
    print(f"Sum of positive elements: {sum_of_positive(lst)}")

    product_el = product_elements(lst)

    if product_el == 0 and len(lst) >= 3:
        print(f"Product of elements between min and max: 0 (no elements between them or product is 0)")
    elif len(lst) < 3:
        print(f"Product of elements between min and max: Not enough elements (need at least 3)")
    else:
        print(f"Product of elements between min and max: {product_el}")