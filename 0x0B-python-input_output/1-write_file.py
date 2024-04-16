#!/usr/bin/python
"""    function that writes a string to a text file"""

def write_file(filename="", text=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
