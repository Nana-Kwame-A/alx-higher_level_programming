#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    nums = 0

    for i in uniq_list:
        nums += i

    return (nums)
