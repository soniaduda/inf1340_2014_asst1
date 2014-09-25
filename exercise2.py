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

    odd_result = (digits[0] + digits[2] + digits[4] + digits[6] + digits[8] + digits[10])*3
    result = odd_result + digits[1] + digits[3] + digits[5] + digits[7] + digits[9]
    int(result)
    # generate checksum using the first 11 digits provided
    check_digit = " "

    if(result%10 != 0):
        check_digit = 10 - result%10
    else:
        check_digit = 0

    if check_digit == digits[11]:
        return True
    else:
        return False

    # check against the the twelfth digit

    # return True if they are equal, False otherwise


