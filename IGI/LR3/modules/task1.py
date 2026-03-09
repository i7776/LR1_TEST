"""
Labolatory Work №1: Series Expansion
Author: Masalova Lolita Dmitrievna
Date: 08.03.2026
"""

import math

def sin_taylor(x, eps = 1e-4, max_iter = 500):
    """
    Calculate sin(x)
    :param x: angle in radians
    :param eps: precision
    :param max_iter: 500
    :return: result, iter_number
    """
    result = 0
    term = x
    i = 0

    for i in range(max_iter):
        result += term
        if (abs(term) < eps and i > 0):
             return result, i + 1

        #execute next component
        term = term * (-1) * x * x /((2 * i + 2) * (2 * i +3))
        return result, i + 1


def math_sin(x):
    #execute sin
    return math.sin(x)










