#!/usr/bin/python3
"""Defines the Base class."""

class Base:
    """Represents the base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance.

        Args:
            id (int): The identifier for the instance. If None, increments __nb_objects and assigns the new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
