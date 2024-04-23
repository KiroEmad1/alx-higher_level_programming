#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    unique_integers = set(my_list)
    return sum(unique_integers)
