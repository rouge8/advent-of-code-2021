from advent_of_code_2021.day03 import Diagnostic, part1
DATA = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_part1():
    assert part1(DATA) == Diagnostic(22, 9)
