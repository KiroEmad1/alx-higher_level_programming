#!/usr/bin/python3
"""Defines the Rectangle class, a subclass of Base."""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        self.validate_non_negative_int('width', value)
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        self.validate_non_negative_int('height', value)
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle's position."""
        self.validate_non_negative_int('x', value)
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle's position."""
        self.validate_non_negative_int('y', value)
        self.__y = value

    def validate_non_negative_int(self, attribute, value):
        """Validates that a value is a non-negative integer.

        Args:
            attribute (str): The name of the attribute being validated.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Displays the rectangle."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return f"[Rectangle] "

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle.

        Args:
            *args: Non-keyworded arguments (optional).
            **Keyworded arguments representing attributes .

        Note:
            If *args exists and is not empty, **kwargs will be skipped.
            Each key in **kwargs represents an attribute of the rectangle.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle."""
        return{'n': self.id, 'w': self.width, 'h': self.height, 'x': self.x, 'y': self.y}


if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)
    print(r1)
    print(r1.area())
    r1.display()
