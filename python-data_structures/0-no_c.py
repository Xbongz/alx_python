#!/usr/bin/python3
def no_c(my_string):
    My_list = ""
    for char in my_string:
        if char != "C" and char != "c":
            My_list += char
            return My_list

