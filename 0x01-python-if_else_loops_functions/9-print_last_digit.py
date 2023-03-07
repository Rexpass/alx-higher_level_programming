#!/usr/bin/python3
def print_last_digit(number):
    non_negative = number
    if non_negative < 0:
        non_negative = -non_negative
        last_digit = non_negative % 10
        last_digit = -last_digit
    else:
        last_digit = non_negative % 10
    print("{}".format(last_digit), end='')
    return last_digit
