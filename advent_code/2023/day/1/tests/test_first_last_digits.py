"""
Advent of Code - 2023

--- Day 1: Trebuchet?! ---

On each line, the calibration value can be found by combining the first digit
and the last digit (in that order) to form a single two-digit number.

For example:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are
12, 38, 15, and 77. Adding these together produces 142.

--- Part Two ---

It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also
count as valid "digits".

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are
29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""

from trebuchet.trebuchet import calibration


def test_calibration_value_for_1abc2_must_be_12():
    value = '1abc2'

    calibrated = calibration(value)

    assert calibrated == 12


def test_calibration_value_for_pqr3stu8vwx_must_be_38():
    value = 'pqr3stu8vwx'

    calibrated = calibration(value)

    assert calibrated == 38


def test_calibration_value_for_a1b2c3d4e5f_must_be_15():
    value = 'a1b2c3d4e5f'

    calibrated = calibration(value)

    assert calibrated == 15


def test_calibration_value_for_treb7uchet_must_be_77():
    value = 'treb7uchet'

    calibrated = calibration(value)

    assert calibrated == 77


def test_calibration_value_for_two1nine_must_be_29():
    value = 'two1nine'

    calibrated = calibration(value)

    assert calibrated == 29


def test_calibration_value_for_eightwothree_must_be_83():
    value = 'eightwothree'

    calibrated = calibration(value)

    assert calibrated == 83


def test_calibration_value_for_abcone2threexyz_must_be_13():
    value = 'abcone2threexyz'

    calibrated = calibration(value)

    assert calibrated == 13


def test_calibration_value_for_xtwone3four_must_be_24():
    value = 'xtwone3four'

    calibrated = calibration(value)

    assert calibrated == 24


def test_calibration_value_for_4nineeightseven2_must_be_42():
    value = '4nineeightseven2'

    calibrated = calibration(value)

    assert calibrated == 42


def test_calibration_value_for_zoneight234_must_be_14():
    value = 'zoneight234'

    calibrated = calibration(value)

    assert calibrated == 14


def test_calibration_value_for_7pqrstsixteen_must_be_76():
    value = '7pqrstsixteen'

    calibrated = calibration(value)

    assert calibrated == 76
