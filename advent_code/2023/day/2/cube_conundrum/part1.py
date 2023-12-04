"""
Advent of Code - 2023

--- Day 2: Cube Conundrum ---

Determine which games would have been possible if the bag had been loaded with
only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the
IDs of those games?
"""

from cube_conundrum import check


def possible_games():
    with open('input') as file_input:
        for line in file_input:
            yield check(line)

total = sum(possible_games())
print(total)
