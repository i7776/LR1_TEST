"""
Module for Task 1.
Implements the RationalFraction class to handle mathematical fractions,
demonstrating serialization to CSV and Pickle formats.
"""

from .models import JsonSerializeMixit
class RationalFraction(JsonSerializeMixit):
    """
    Class representing a rational fraction
    """

    def __init__(self, numerator, denominator) :
        """
        Initialization fraction
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero!")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        """
        Get numerator
        """
        return self.__numerator

    @property
    def denominator(self):
        """
        Get denominator
        """
        return self.__denominator

    def __eq__(self, other):
        """
        Check if two fractions are equal
        """
        if not isinstance(other, RationalFraction):
            return False

        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        """
        Check if self < other
        """
        return  self.numerator * other.denominator < self.denominator * other.numerator

    def __str__(self):
        """
        Return string representation like a/b
        """
        return f"{self.numerator}/{self.denominator}"




