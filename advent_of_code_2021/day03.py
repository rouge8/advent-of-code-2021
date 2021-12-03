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


@attr.frozen
class LifeSupportDiagnostic:
    oxygen_generator_rating: int
    co2_scrubber_rating: int

    @property
    def rating(self) -> int:
        return self.oxygen_generator_rating * self.co2_scrubber_rating


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


def digit_counts(data: typing.Iterable[str]) -> dict[int, int]:
    counts = {0: 0, 1: 0}

    for digit in data:
        counts[int(digit)] += 1
    return counts


def part2(data: typing.Iterable[str]) -> LifeSupportDiagnostic:
    oxygen_generator_data = list(data)
    co2_scrubber_data = list(oxygen_generator_data)

    oxygen_generator_rating = ""
    co2_scrubber_rating = ""

    for i in range(len(oxygen_generator_data[0])):
        oxygen_generator_data = [
            line
            for line in oxygen_generator_data
            if line.startswith(oxygen_generator_rating)
        ]

        if len(oxygen_generator_data) == 1:
            oxygen_generator_rating = oxygen_generator_data[0]
            break

        oxygen_digit_counts = digit_counts((line[i] for line in oxygen_generator_data))

        if oxygen_digit_counts[1] >= oxygen_digit_counts[0]:
            oxygen_generator_rating += "1"
        else:
            oxygen_generator_rating += "0"

    for i in range(len(co2_scrubber_data[0])):
        co2_scrubber_data = [
            line for line in co2_scrubber_data if line.startswith(co2_scrubber_rating)
        ]

        if len(co2_scrubber_data) == 1:
            co2_scrubber_rating = co2_scrubber_data[0]
            break

        co2_digit_counts = digit_counts((line[i] for line in co2_scrubber_data))

        if co2_digit_counts[0] <= co2_digit_counts[1]:
            co2_scrubber_rating += "0"
        else:
            co2_scrubber_rating += "1"

    return LifeSupportDiagnostic(
        int(oxygen_generator_rating, 2), int(co2_scrubber_rating, 2)
    )


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
