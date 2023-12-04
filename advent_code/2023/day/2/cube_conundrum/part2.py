"""
Advent of Code - 2023

--- Day 2: Cube Conundrum ---

--- Part Two ---

For each game, find the minimum set of cubes that must have been present.
What is the sum of the power of these sets?
"""

from cube_conundrum import total_power_sets


with open('input') as file_input:
    total = total_power_sets(games=file_input)
    print(total)
