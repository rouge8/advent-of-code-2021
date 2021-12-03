from advent_of_code_2021.day02 import Direction, Position, part1, part2

DATA = [
    (Direction.FORWARD, 5),
    (Direction.DOWN, 5),
    (Direction.FORWARD, 8),
    (Direction.UP, 3),
    (Direction.DOWN, 8),
    (Direction.FORWARD, 2),
]


def test_part1():
    assert part1(DATA) == Position(15, 10)


def test_part2():
    assert part2(DATA) == Position(15, 60)
