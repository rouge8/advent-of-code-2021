import typing

import click


def part1(data: typing.Iterable[str]) -> None:
    pass


@click.command(name="day00")
@click.argument("data", type=click.File("r"))
def main(data):
    data = [line.strip() for line in data]

    print(f"part1: {part1(data)}")


if __name__ == "__main__":
    main()
