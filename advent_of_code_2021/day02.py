import typing
from enum import Enum

import attr
import click


class Direction(str, Enum):
    FORWARD = "forward"
    DOWN = "down"
    UP = "up"

    @classmethod
    def from_str(cls, s: str):
        match s:
            case "forward":
                return cls.FORWARD
            case "down":
                return cls.DOWN
            case "up":
                return cls.UP
            case _:
                raise NotImplementedError


@attr.define
class Position:
    horizontal: int
    depth: int

    @property
    def product(self):
        return self.horizontal * self.depth


def part1(data: typing.Iterable[typing.Tuple[Direction, int]]) -> Position:
    position = Position(0, 0)

    for line in data:
        match line[0]:
            case Direction.FORWARD:
                position.horizontal += line[1]
            case Direction.DOWN:
                position.depth += line[1]
            case Direction.UP:
                position.depth -= line[1]

    return position


@click.command(name="day02")
@click.argument("data", type=click.File("r"))
def main(data):
    data = (line.split(" ", 1) for line in data)
    data = (
        (Direction.from_str(line[0]), int(line[1]))
        for line in data
    )

    position = part1(data)
    print(f"part1: {position} -- {position.product}")


if __name__ == "__main__":
    main()
