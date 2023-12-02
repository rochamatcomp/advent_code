"""
Advent of Code - 2023

--- Day 1: Trebuchet?! ---

Consider your entire calibration document.
What is the sum of all of the calibration values?
"""


from trebuchet import calibration

def calibration_value():
    with open('input') as file_input:
        for line in file_input:
            yield calibration(line)

total = sum(calibration_value())
print(total)
