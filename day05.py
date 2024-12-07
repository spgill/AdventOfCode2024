#! /usr/bin/env python3
# stdlib imports
import math
import re

# local imports
import utils


@utils.part1
def part1(puzzle_input: str):
    # Begin by parsing the puzzle input into a mapping of page rules and a list
    # of page updates
    upper_section, lower_section = puzzle_input.strip().split('\n\n')

    page_rules: dict[int, set[int]] = {}
    for line in upper_section.splitlines():
        left, right = [int(s) for s in line.split('|')]
        if left not in page_rules:
            page_rules[left] = set()
        page_rules[left].add(right)

    page_updates: list[list[int]] = [[int(n) for n in line.split(',')]
                                     for line in lower_section.splitlines()]

    # We iterate through each page update, and check the constraints on every
    # number therein. Valid updates will have their middle number added to
    # a running sum. We will also maintain a list of all the invalid updates
    # to pass on to part 2
    middle_sum = 0
    invalid_updates: list[list[int]] = []
    for update in page_updates:
        invalid = False
        for i in range(len(update)):
            character = update[i]
            predecessors = set(update[:i])
            if character in page_rules:
                if page_rules[character].intersection(predecessors):
                    invalid = True

        middle_idx = math.floor(len(update) / 2)
        if invalid:
            invalid_updates.append(update)
        else:
            middle_sum += update[middle_idx]

    # The sum of middle numbers is the answer
    utils.print_answer(middle_sum)

    # Return the page rules and updates for part 2
    return (page_rules, invalid_updates)


@utils.part2
def part2(_, part1_ret: tuple[dict[int, set[int]], list[list[int]]]):
    # Unpack the values from part 1
    (page_rules, invalid_updates) = part1_ret

    # Simliar to part 1, we're going to iterate through each page update (only
    # the ones that were previously flagged as invalid), and use the
    # page rules to reorder the updates to become valid.
    middle_sum = 0
    for update in invalid_updates:
        i = 0
        while i < len(update):
            # print(new_update)
            predecessors = update[:i]
            character = update[i]
            successors = update[i + 1:]

            if character in page_rules:
                for constraint in page_rules[character]:
                    if constraint in predecessors:
                        predecessors.remove(constraint)
                        successors.insert(0, constraint)
                        i -= 1  # Move the index back to account for the drift

            # Store the rearranged list and increment the index
            update = [*predecessors, character, *successors]
            i += 1

        # Now that the update has been rearranged, add up the middle number
        middle_idx = math.floor(len(update) / 2)
        middle_sum += update[middle_idx]

    # This sum is the answer to part 2
    utils.print_answer(middle_sum)


if __name__ == "__main__":
    utils.start()
