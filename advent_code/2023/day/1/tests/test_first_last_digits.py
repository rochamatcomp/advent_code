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
"""

from trebuchet.trebuchet import calibration


def test_calibration_value_for_1abc2_must_be_12():
    value = '1abc2'

    calibrated = calibration(value)

    assert calibrated == 12


def test_calibration_value_for_pqr3stu8vwx_must_be_12():
    value = 'pqr3stu8vwx'

    calibrated = calibration(value)

    assert calibrated == 38


def test_calibration_value_for_a1b2c3d4e5f_must_be_12():
    value = 'a1b2c3d4e5f'

    calibrated = calibration(value)

    assert calibrated == 15


def test_calibration_value_for_treb7uchet_must_be_12():
    value = 'treb7uchet'

    calibrated = calibration(value)

    assert calibrated == 77
