#!/usr/bin/env python3

__authors__ = 'Sonia Duda & Lauren Olar'
__email__ = "sonia.duda@mail.utoronto.ca & lauren.olar@mail.utoronto.ca"

__copyright__ = "2014 SD&LO"

__status__ = "Prototype"

# imports one per line

import pytest
from exercise3 import decide_rps


def test_decide_rps():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2 is True
    assert decide_rps("Scissors", "Scissors") == 0 is True
    assert decide_rps("Rock", "Scissors") == 1 is True

def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        decide_rps("papah")  # misspelled
        decide_rps("P")  # not full word
        decide_rps("player1")  # incorrect input