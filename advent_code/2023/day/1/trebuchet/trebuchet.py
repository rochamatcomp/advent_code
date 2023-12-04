"""
Advent of Code - 2023

--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected
to take a look. The Elves have even given you a map; on it, they've used
stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations,
you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on
each day in the Advent calendar; the second puzzle is unlocked when you
complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine
("not powerful enough") and where they're even sending you ("the sky")
and why your map looks mostly blank ("you sure ask a lot of questions")
and hang on did you just say the sky
("of course, where do you think snow comes from") when you realize that
the Elves are already loading you into a trebuchet
("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration
document (your puzzle input) has been amended by a very young Elf who was
apparently just excited to show off her art skills.
Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves
now need to recover. On each line, the calibration value can be found by
combining the first digit and the last digit (in that order) to form
a single two-digit number.

--- Part Two ---

It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
"""

from dataclasses import dataclass
from itertools import chain


@dataclass
class NumberPosition:
    number: str
    position: int


numbers = {
    # 3 letters
    'one': '1',
    # 3 letters
    'two': '2',
    # 5 letters
    'three': '3',
    # 4 letters
    'four': '4',
    # 4 letters
    'five': '5',
    # 3 letters
    'six': '6',
    # 5 letters
    'seven': '7',
    # 5 letters
    'eight': '8',
    # 4 letters
    'nine': '9'
}


def search_word(search, line):
    for word, digit in numbers.items():
        try:
            start = search(line, word)
        except ValueError:
            continue

        yield NumberPosition(digit, start)


def search_digit(search, line):
    for digit in numbers.values():
        try:
            start = search(line, digit)
        except ValueError:
            continue

        yield NumberPosition(digit, start)


def first(line: str) -> str:
    search = str.index
    query = chain(search_word(search, line), search_digit(search, line))
    digit = min(query, key=lambda number: number.position)

    return digit.number


def last(line: str) -> str:
    search = str.rindex
    query = chain(search_word(search, line), search_digit(search, line))
    digit = max(query, key=lambda number: number.position)

    return digit.number


def calibration(line: str) -> int:
    """
    Calibration value can be found by combining the first digit
    and the last digit (in that order) to form a single two-digit number.

    Args:
        line (str): document text line.

    Returns:
        int: Calibration value as first digit and the last digit
        (in that order) to form a single two-digit number.
    """
    first_digit = first(line)
    last_digit = last(line)

    # first digit in line as tens digit and last digit in as units digit
    value = int(f'{first_digit}{last_digit}')

    return value
