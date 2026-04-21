"""
Module for Task 4.
Implements a geometric modeling system using abstract base classes.
Features the InscribedSquare class, which calculates area and uses
Matplotlib for visual rendering of shapes with custom labeling.
"""

from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class GeometricFigure(ABC):
    """
    Abstract base class representing a geometric figure
    Requires child classes to implement area calculation and drawing methods
    """

    @abstractmethod
    def get_area(self):
        """
        Calculates and returns the area of the geometric figure
        """
        pass

    @abstractmethod
    def draw(self, label):
        """
        Draws the geometric figure on the screen
        """
        pass

class ShapeColor:
    """
    Class representing the color of a figure
    """

    def __init__(self, color):
        """
        Initializes the ShapeColor
        :param color
        """
        self._color = color

    @property
    def color(self):
        """
        Getter for the color property
        :return: Color string
        """
        return self._color


class InscribedSquare(GeometricFigure):
    """
    Class representing a square inscribed in a circle
    """

    figure_name = "Square inscribed in a circle"

    def __init__(self, r, color):
        """
        Initializes the inscribed square
        :param r: Radius
        :param color: Color of the square.\
        """
        self._color = ShapeColor(color)
        self._radius = r

    def get_area(self):
        """
        Calculates the area of the inscribed square
        :return: Area of the square
        """
        return 2 * self._radius * self._radius

    def __str__(self):
        """
        Returns a formatted string representation of the object
        :return: Formatted string with radius, color, and area
        """
        return "Inscribed Square (Radius: {}, Color: {}, Area: {})".format(
            self._radius,
            self._color.color,
            self.get_area()
        )

    @classmethod
    def get_name(cls):
        """
        Class method to get the name of the geometric figure
        :return: Name of the figure
        """
        return cls.figure_name

    def draw(self, label):
        """
        Draws
        :param label: Text label to display in the center of the figure
        """
        print(f"\n[Drawing figure: {self.get_name()}...]")
        fig, ax = plt.subplots(figsize=(6, 6))

        circle = plt.Circle((0, 0), self._radius, fill=False, edgecolor='black', linewidth=2)
        ax.add_patch(circle)

        side = self._radius * math.sqrt(2)
        bottom_left_x = -side / 2
        bottom_left_y = -side / 2

        square = patches.Rectangle((bottom_left_x, bottom_left_y), side, side,
                                   fill=True, color=self._color.color, alpha=0.5)
        ax.add_patch(square)

        plt.text(0, 0, label, fontsize=14, ha='center', va='center', color='black', weight='bold')

        ax.set_xlim(-self._radius - 1, self._radius + 1)
        ax.set_ylim(-self._radius - 1, self._radius + 1)
        ax.set_aspect('equal')
        plt.title(self.get_name())
        plt.grid(True, linestyle=':', alpha=0.6)

        filename = "task4_figure.png"
        plt.savefig(filename)
        print(f"Figure successfully saved to '{filename}'")
        plt.show()