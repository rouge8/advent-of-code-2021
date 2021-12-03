from advent_of_code_2021.day01 import part1


def test_part1():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    assert part1(depths) == 7
