#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    new_list = [x if x != search else replace for x in my_list]
    return new_list
