#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

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

def mark_to_letter(mark):
    """
    Convert numeric grade to a letter grade.
    :param mark: (integer): Numeric grade to be converted
    :return: str: The equivalent letter grade
    """

    letter = ""
    if mark >=90 and mark <=100:
        letter = "A+"
    elif mark >=85 and mark <=89:
        letter = "A"
    elif mark >=80 and mark <=84:
        letter = "A-"
    elif mark >=77 and mark <=79:
        letter = "B+"
    elif mark >=73 and mark <=76:
        letter = "B"
    elif mark >=70 and mark <=72:
        letter = "B-"
    else:
        letter = "FZ"

    return letter


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

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        if grade == "A+" or grade == "A" or grade == "A-" or grade == "B+" or grade == "B" or grade == "B-" or grade == "FZ":
            letter_grade = grade
        else:
            raise ValueError("Invalid input")
    elif type(grade) is int:
        # check that grade is in the accepted range
        if grade >= 0 or grade<= 100:
            letter_grade = mark_to_letter(grade)
        else:
            raise ValueError("Invalid input")
        # convert the numeric grade to a letter grade

    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    if letter_grade == "A+" or letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade =="B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    elif letter_grade == "FZ":
        gpa = 0.9

    return gpa

