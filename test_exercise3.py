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
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1


def test_input():
    """
    Inputs that are the incorrect format and length
    """

    with pytest.raises(TypeError):
        decide_rps(1, 2)  # integer
        decide_rps(1, "Rock") # player1 integer
        decide_rps("Rock", 1) # player2 integer

        decide_rps(1.2, 2.3)  # float
        decide_rps(1.2, "Paper") # player1 float
        decide_rps("Paper", 2.3) # player2 float

    with pytest.raises(ValueError):
        decide_rps("papah", "Rock")  # misspelled player1
        decide_rps("Rock", "papah")  # misspelled player2

        decide_rps("P", "R")  # not full word
        decide_rps("player1", "player2")  # incorrect input