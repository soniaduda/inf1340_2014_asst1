#!/usr/bin/env python3

""" Module to test exercise2.py """

__authors__ = 'Sonia Duda & Lauren Olar'
__email__ = "sonia.duda@mail.utoronto.ca & lauren.olar@mail.utoronto.ca"

__copyright__ = "2014 SD&LO"

__status__ = "Prototype"

# imports one per line

import pytest
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("012222335895") is False  # same numbers, different order
    assert checksum("717951000841") is False
    assert checksum("746936224300") is True  # 0 check digit


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)  # test to see if accepts float types
        checksum(786936224306)  # test to see if accepts int types
        checksum("abcdefghiklm")  # test to see if accepts letters
        checksum("738462184721")  # test to see if accepts mix of letters and numbers
        checksum("7a7951000841")  # test to see if accepts letter (a) in place of number (1)

    with pytest.raises(ValueError):
        checksum("1")  # correct format, too few digits
        checksum("1234567890")  # correct format, too few digits
        checksum("12345678901011")  # correct format, too many digits