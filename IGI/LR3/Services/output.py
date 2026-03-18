"""
Service: Output handlers
"""

"""
Output for Task1
"""

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
    print(f"\n Result for Task 2")
    print(f" Sum of sequence: {summa}")
    print(f"Count of even natural numbers: {count}")



