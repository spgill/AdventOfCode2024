#! /usr/bin/env python3
# stdlib imports
import collections

# local imports
import utils


@utils.part1
def part1(puzzle_input: str):
    # Split the input into lines
    lines = puzzle_input.strip().splitlines()

    # Iterate through each line and parse out the left and right hand numbers
    left_list: list[int] = []
    right_list: list[int] = []
    for line in lines:
        left, right = line.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))

    # Clone the lists for later use
    left_list_clone = left_list.copy()
    right_list_clone = right_list.copy()

    # Iterate through each smallest L-R pair and summate their difference
    diff_sum = 0
    while len(left_list) > 0:
        left = min(left_list)
        right = min(right_list)

        left_list.remove(left)
        right_list.remove(right)

        diff_sum += abs(left - right)

    # The answer for part 1 is this sum
    utils.print_answer(diff_sum)

    # Pass the left and right lists onto part 2
    return (left_list_clone, right_list_clone)


@utils.part2
def part2(_, part_1_ret: tuple[list[int], list[int]]):
    # Destructure the data from part 1
    left_list, right_list = part_1_ret

    # First we'll use a counter to count the number of appearances of each
    # unique number in the right list
    right_counter = collections.Counter(right_list)

    # Finally we'll iterate through each left hand number and multiply it by the number
    # of times it occurs in the right list
    similarity_score = 0
    for n in left_list:
        similarity_score += n * right_counter[n]

    # This total similarity score is the answer
    utils.print_answer(similarity_score)


if __name__ == "__main__":
    utils.start()
