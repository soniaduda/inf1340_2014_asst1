#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014.

Grade to GPA Conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__authors__ = 'Sonia Duda and Lauren Olar'
__email__ = "sonia.duda@mail.utoronto.ca & lauren.olar@mail.utoronto.ca"

__copyright__ = "2014 SD&LO"

__status__ = "Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.
    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ
    :return:
        float: The equivalent GPA
            Value is 0.0-4.0
    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    gpa = 0.0

    if type(grade) is str:
        if grade == "A+" or grade == "A" or grade == "A-" or grade == "B+" or grade == "B" or grade == "B-" or grade == "FZ":
            letter_grade = grade  # assign grade to letter_grade
        else:
            raise ValueError("Invalid input")
    elif type(grade) is int:
        if grade >= 0 and grade <= 100:  # check that grade is in the accepted range
            # assigns the number grade to the corresponding letter grade
            if grade >= 90:
                letter_grade = "A+"
            elif grade >= 85:
                letter_grade = "A"
            elif grade >= 80:
                letter_grade = "A-"
            elif grade >= 77:
                letter_grade = "B+"
            elif grade >= 73:
                letter_grade = "B"
            elif grade >= 70:
                letter_grade = "B-"
            else:
                letter_grade = "FZ"
        else:
            raise ValueError("Invalid input")
    else:
        raise TypeError("Invalid type passed as parameter")  # raise a TypeError exception

    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    if letter_grade == "A+" or letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    elif letter_grade == "FZ":
        gpa = 0.0

    return gpa