#!/usr/bin/env python3

""" Assignment 1, Exercise 3, INF1340, Fall, 2014.

Rock, Paper, Scissors Outcomes

This module contains one function decide_rps. It can show the results of a game of
Rock, Paper, Scissors between two players. It can be passed one of three options (Rock,
Paper, or Scissors) from each player to show who will win. All other inputs will
result in an error. A returned value of 1 shows player 1 as the winner,
whereas a returned value of 2 shows that player 2 is the winner.

"""

__authors__ = 'Sonia Duda and Lauren Olar'
__email__ = "sonia.duda@mail.utoronto.ca & lauren.olar@mail.utoronto.ca"

__copyright__ = "2014 SD&LO"

__status__ = "Prototype"

# imports one per line

def decide_rps(player1, player2):
    """
    Returns value of winning player
    :param:
        string: "Rock", "Paper", "Scissors"
    :return:
        int, value of player that wins
    :raises:
        TypeError if parameter is not correct string input
    """

    rps_outcomes = {("Rock", "Rock"): 0,
                    ("Rock", "Paper"): 2,
                    ("Rock", "Scissors"): 1,
                    ("Paper", "Rock"): 1,
                    ("Paper", "Paper"): 0,
                    ("Paper", "Scissors"): 2,
                    ("Scissors", "Rock"): 2,
                    ("Scissors", "Paper"): 1,
                    ("Scissors", "Scissors"): 0}

    if player1 != "Rock" or player1 != "Paper" or player1 != "Scissors":
        raise TypeError("Invalid input")

    if player2 != "Rock" or player2 != "Paper" or player2 != "Scissors":
        raise TypeError("Invalid input")

    return rps_outcomes.get((player1, player2))