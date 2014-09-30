#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

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
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    if type(upc) is not str:
        raise TypeError("Invalid input")

    if len(upc) != 12:
        raise ValueError("Incorrect length")

    digits = list(upc)

    odd_result = (int(digits[0]) + int(digits[2]) + int(digits[4]) + int(digits[6]) + int(digits[8]) + int(digits[10]))*3
    result = odd_result + int(digits[1]) + int(digits[3]) + int(digits[5]) + int(digits[7]) + int(digits[9])
    # generate checksum using the first 11 digits provided


    if(int(result)%10 != 0):
        check_digit = 10 - int(result)%10
    else:
        check_digit = 0

    if check_digit == int(digits[11]):
        return True
    else:
        return False

print(checksum("786936224306"))
    # check against the the twelfth digit

    # return True if they are equal, False otherwise


