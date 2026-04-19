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