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
    assert checksum("717951000841") is False
    assert checksum("746936224300") is True
    # other tests


def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
        checksum(786936224306)
        checksum("abcdefghiklm")

    with pytest.raises(ValueError):
        checksum("1")
        checksum("1234567890")

    # other tests

# add functions for any other tests
