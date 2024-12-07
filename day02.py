#! /usr/bin/env python3
# stdlib imports
import math

# vendor imports
import more_itertools

# local imports
import utils


def sign(n: int):
    return -1 if n < 0 else 1


def is_report_safe(report: tuple[int, ...]) -> bool:
    # Over the length of the report, we track the polarity, how many times
    # the polarity has changed, and both the smallest and largest changes in value
    polarity = 0
    polarity_flips = -1  # We expect there to be one at the beginning, so we offset
    smallest_delta = math.inf
    largest_delta = 0
    for x, y in more_itertools.sliding_window(report, 2):
        delta = y - x
        delta_polarity = sign(delta)
        if delta_polarity != polarity:
            polarity_flips += 1
            polarity = delta_polarity
        largest_delta = max(largest_delta, abs(delta))
        smallest_delta = min(smallest_delta, abs(delta))

    # If there has been no additional polarity flips, and both the smallest
    # and largest delta bound are satisfied, then this report is safe
    if polarity_flips == 0 and smallest_delta >= 1 and largest_delta <= 3:
        return True

    return False


@utils.part1
def part1(puzzle_input: str):
    # Split the input into lines
    lines = puzzle_input.strip().splitlines()

    # Start by parsing each line into a tuple of numbers (a report)
    report_list = [tuple(int(n) for n in line.split(' ')) for line in lines]

    # Count up the number safe reports
    safe_reports = sum(is_report_safe(r) for r in report_list)

    utils.print_answer(safe_reports)

    return report_list


@utils.part2
def part2(_, report_list: list[tuple[int, ...]]):
    # We're doing the same basic thing as in part 1 except we're allowed
    # to exclude one number from each report, so we've got to test each permutation
    safe_reports = 0
    for report in report_list:
        for i in range(len(report)):
            sub_report = report[:i] + report[i + 1:]
            if is_report_safe(sub_report):
                safe_reports += 1
                break

    utils.print_answer(safe_reports)


if __name__ == "__main__":
    utils.start()
