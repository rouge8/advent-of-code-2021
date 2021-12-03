import operator
import typing
from collections import defaultdict

import attr
import click


@attr.frozen
class Diagnostic:
    gamma_rate: int
    epsilon_rate: int

    @property
    def power_consumption(self) -> int:
        return self.gamma_rate * self.epsilon_rate


def part1(data: typing.Iterable[str]) -> Diagnostic:
    counts = defaultdict(lambda: {0: 0, 1: 0})

    for line in data:
        for i, digit in enumerate(line):
            counts[i][int(digit)] += 1

    gamma_rate = "".join(
        str(max(count.items(), key=operator.itemgetter(1))[0])
        for count in counts.values()
    )
    epsilon_rate = "".join(
        str(min(count.items(), key=operator.itemgetter(1))[0])
        for count in counts.values()
    )

    return Diagnostic(int(gamma_rate, 2), int(epsilon_rate, 2))


@click.command(name="day03")
@click.argument("data", type=click.File("r"))
def main(data):
    data = [line.strip() for line in data]

    diagnostic = part1(data)
    print(f"part1: {diagnostic} -- {diagnostic.power_consumption}")

    life_support_diagnostic = part2(data)
    print(f"part2: {life_support_diagnostic} -- {life_support_diagnostic.rating}")


if __name__ == "__main__":
    main()
