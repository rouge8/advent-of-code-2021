import pytest

from advent_of_code_2021.day01 import part1, part2


@pytest.fixture
def depths():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part1(depths):
    assert part1(depths) == 7


def test_part2(depths):
    assert part2(depths) == 5
