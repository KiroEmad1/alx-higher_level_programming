#!/usr/bin/python3
"""Defines the Square class, a subclass of Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a special case of a Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The identifier for the square. .
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Updates the attributes of the square.

        Args:
            *args: Non-keyworded arguments (optional).
            **kwargs: keyword for attributes and their values.

        Note:
            If *args exists and is not empty, **kwargs will be skipped.
            Each key in **kwargs represents an attribute of the square.
        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}


if __name__ == "__main__":
    s1 = Square(5)
    print(s1)
    print(s1.area())
