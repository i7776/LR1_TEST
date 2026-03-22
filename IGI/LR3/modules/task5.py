"""
Task №5: Calculates the sum of positive elements
and the product of elements located between the maximum and minimum
elements by absolute value.
"""

def sum_of_positive(lst):
    """
    Find sum of positive elements
    :param lst: list of integers
    :return: sum of positive elements
    """

    total_sum = 0.0

    for elem in lst:
        if elem > 0:
            total_sum += elem

    return total_sum

def product_elements(lst):
    """
    Find product of elements between min and max elements by absolute value
    :param lst: list of integers
    :return: product
    """

    if len(lst) < 3:
        return 0

    min_mod_idx = 0
    max_mod_idx = 0

    min_mod_val = abs(lst[0])
    max_mod_val = abs(lst[0])

    for i in range(1, len(lst)):
        current_mod = abs(lst[i])

        if current_mod < min_mod_val:
            min_mod_val = current_mod
            min_mod_idx = i

        if current_mod > max_mod_val:
            max_mod_val = current_mod
            max_mod_idx = i

    start = min(min_mod_idx, max_mod_idx)
    end = max(min_mod_idx, max_mod_idx)

    if end - start <= 1:
        return 0

    product = 1.0
    for i in range(start + 1, end):
        product *= lst[i]

    return product