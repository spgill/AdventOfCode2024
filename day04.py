#! /usr/bin/env python3
# stdlib imports

# local imports
import utils


class Grid:
    def __init__(self, puzzle_input: str) -> None:
        self._cells: list[str] = puzzle_input.strip().splitlines()

    @property
    def width(self) -> int:
        return len(self._cells[0])

    @property
    def height(self) -> int:
        return len(self._cells)

    def get(self, x: int, y: int) -> str:
        if x >= self.width or x < 0:
            return ''
        if y >= self.height or y < 0:
            return ''

        return self._cells[y][x]


direction_normals: list[tuple[int, int]] = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]

target_word = 'XMAS'


@utils.part1
def part1(puzzle_input: str):
    # Contruct a grid using the puzzle input
    grid = Grid(puzzle_input)

    # Iterate through each position on the grid and perform a search in every
    # cardinal direction
    targets_found: set[tuple[tuple[int, int], tuple[int, int],
                             tuple[int, int], tuple[int, int]]] = set()
    for y in range(grid.height):
        for x in range(grid.width):
            # Iterate through each search direction
            for normal_x, normal_y in direction_normals:
                capture = ''
                capture_coords: list[tuple[int, int]] = []
                for i in range(4):
                    coord = (x + normal_x * i, y + normal_y * i)
                    cell = grid.get(*coord)
                    if not cell:
                        break
                    capture += cell
                    capture_coords.append(coord)

                # If the captured string matches the target words (or its reverse),
                # then save it to the set
                if capture == target_word:
                    targets_found.add(
                        (capture_coords[0], capture_coords[1], capture_coords[2], capture_coords[3]))
                elif capture == target_word[::-1]:
                    targets_found.add(
                        (capture_coords[3], capture_coords[2], capture_coords[1], capture_coords[0]))

    # The answer is the number of unique targets found
    utils.print_answer(len(targets_found))

    # Pass the grid on to part 2
    return grid


center_char = 'A'
cross_chars = 'MS'
valid_legs = [cross_chars, cross_chars[::-1]]


@utils.part2
def part2(_, grid: Grid):
    # We take the grid created in part 1 and iterate over each place in the grid.
    # Because we're looking for a large shapes, we can skip first and last rows
    # and columns.
    valid_center_coords: set[tuple[int, int]] = set()
    for y in range(1, grid.height - 1):
        for x in range(1, grid.width - 1):
            # When we identify the middle of a cross, we need to investigate each leg
            if grid.get(x, y) == center_char:
                leg0 = grid.get(x - 1, y - 1) + grid.get(x + 1, y + 1)
                leg1 = grid.get(x - 1, y + 1) + grid.get(x + 1, y - 1)
                if leg0 in valid_legs and leg1 in valid_legs:
                    valid_center_coords.add((x, y))

    # The answer is the number of valid x-mas crosses found
    utils.print_answer(len(valid_center_coords))


if __name__ == "__main__":
    utils.start()
