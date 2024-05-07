#!/usr/bin/env python3
"""
This module conatins function that returns the
perimeter of the island described in grid
"""


def island_perimeter(grid):
    """ Function that returns the perimeter of the island described in grid"""
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check up
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # Check down
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # Check right
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter
