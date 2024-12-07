#! /usr/bin/env python3
# stdlib imports
import re

# local imports
import utils


@utils.part1
def part1(puzzle_input: str):
    # Use regular expression to parse out all the valid `mul` expressions
    instructions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", puzzle_input)

    # The sum of all products is the answer
    utils.print_answer(sum(int(x) * int(y) for x, y in instructions))


@utils.part2
def part2(puzzle_input: str, _):
    # Once again, parse the expressions using regular expression
    instructions = re.findall(
        r"mul\((\d{1,3}),(\d{1,3})\)|(do|don't)\(\)", puzzle_input)

    # Iterate through each instruction and summate the product ONLY if enabled
    enabled = True  # Start off in an enabled state
    summation = 0
    for x, y, operator in instructions:
        if operator == 'do':
            enabled = True
        if operator == 'don\'t':
            enabled = False

        if enabled and x and y:
            summation += int(x) * int(y)

    utils.print_answer(summation)


if __name__ == "__main__":
    utils.start()
