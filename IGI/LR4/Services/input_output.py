"""
Service: Input and Output handlers
"""

def get_int_input(value):
    """
    Integer input validation
    :param value: message to display
    :return: validated integer
    """
    while True:
        try:
            return int(input(value))
        except ValueError:
            print ("Error: Please enter a valid integer.")

def get_natural_input(value):
    """
    Natural integer input validation
    :param value:  message to display
    :return: validated positive integer
    """
    while True:
        num = get_int_input(value)
        if num > 0:
            return num
        else:
            print("Error: Natural number must be greater than 0.")

# Output for Task 1
def print_table_header():
    """
    Prints table header
    """
    print("\n" + "="*70)
    print(f"| {'x':^10} | {'n':^6} | {'F(x)':^15} | {'Math F(x)':^15} | {'eps':^10} |")
    print("="*70)

def print_table_row(x, n, f_x, math_f_x, eps):
    """
    Prints a single row of data in the Taylor series table.
    :param x: input value
    :param n: number of iterations
    :param f_x: calculated Taylor value
    :param math_f_x: math library value
    :param eps: precision
    """
    print(f"| {x:^10.4f} | {n:^6} | {f_x:^15.10f} | {math_f_x:^15.10f} | {eps:^10.2e} |")

def print_table_footer():
    """Prints table footer"""
    print("="*70)

def get_float_input(value):
    """
    Float input validation
    :param value: message to display
    :return: validated float
    """
    while True:
        try:
            return float(input(value))
        except ValueError:
            print("Error: Please enter a valid floating-point number.")