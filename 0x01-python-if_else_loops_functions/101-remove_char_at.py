#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(str, a):
    """Create a copy of the string without the character at position a."""
    if a < 0:
        return (str)
    return (str[:a] + str[a+1:])
