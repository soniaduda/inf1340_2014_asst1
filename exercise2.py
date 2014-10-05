#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014.

Grade to gpa conversion

This module contains one function checksum. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

"""

__authors__ = 'Sonia Duda and Lauren Olar'
__email__ = "sonia.duda@mail.utoronto.ca & lauren.olar@mail.utoronto.ca"

__copyright__ = "2014 SD&LO"

__status__ = "Prototype"

# imports one per line

def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under)
    """

    if type(upc) is not str:  # check type of input
        raise TypeError("Invalid input")  # raise TypeError if not string

    if len(upc) != 12:  # check length of string
        raise ValueError("Incorrect length")  # raise ValueError if not 12

    digits = list(upc)  # convert string to array

    odd_result = (int(digits[0]) + int(digits[2]) + int(digits[4]) + int(digits[6]) + int(digits[8]) + int(digits[10]))*3
    result = odd_result + int(digits[1]) + int(digits[3]) + int(digits[5]) + int(digits[7]) + int(digits[9])

    # generate checksum using the first 11 digits provided
    if int(result) % 10 != 0:
        check_digit = 10 - int(result) % 10
    else:
        check_digit = 0

    # check against the the twelfth digit
    # return True if they are equal, False otherwise
    if check_digit == int(digits[11]):
        return True
    else:
        return False


