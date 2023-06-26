#!/usr/bin/python3

def safe_print_list_integers(my_list=[], y=0):
    """Print the first x elements of a list that are integers.
    Args:
        my_list (list): The list to print elements from.
        y (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(0, y):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
