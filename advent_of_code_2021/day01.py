import click


def part1(depths: list[int]) -> int:
    count = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            count += 1

    return count


def part2(depths: list[int]) -> int:
    sliding_windows = [
        depths[i - 2] + depths[i - 1] + depths[i] for i in range(2, len(depths))
    ]
    return part1(sliding_windows)


@click.command(name="day01")
@click.argument("depths", type=click.File("r"))
def main(depths):
    depths = [int(line) for line in depths]

    print(f"part1: {part1(depths)}")
    print(f"part2: {part2(depths)}")


if __name__ == "__main__":
    main()
