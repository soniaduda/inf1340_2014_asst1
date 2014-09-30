#!/usr/bin/env python3


def decide_rps(player1, player2):
    rps_outcomes = {("Rock","Rock"): 0,
                    ("Rock", "Paper"): 2,
                    ("Rock", "Scissors"): 1,
                    ("Paper", "Rock"): 1,
                    ("Paper", "Paper"): 0,
                    ("Paper", "Scissors"): 2,
                    ("Scissors", "Rock"): 2,
                    ("Scissors", "Paper"): 1,
                    ("Scissors", "Scissors"): 0}

    if player1 != "Rock" or player1!= "Paper" or player1 != "Scissors":
        raise TypeError("Not a valid input")

    if player2 != "Rock" or player1!= "Paper" or player1 != "Scissors":
        raise TypeError("Not a valid input")

    return rps_outcomes.get((player1, player2))



