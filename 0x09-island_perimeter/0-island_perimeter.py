#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Returns the perimeter of the island
    described in the grid"""

    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4
                if row and grid[row - 1][col] == 1:
                    perimeter -= 2
                if row and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
