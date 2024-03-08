#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """
    Returns a list of lists of numbers representing Pascal's triangle.

    Arguments:
    n -- The number of rows of Pascal's triangle to generate.

    Returns:
    A list of lists of integers representing Pascal's triangle.
    """
    # Returns and empty list of n is 0 or less.
    if n <= 0:
        return []

    triangle = [[1]]

    for row_index in range(1, n):
        # Start and end each row with 1.
        new_row = [1]

        # Calculate the middle values based on the previous row.
        for col_index in range(1, row_index):
            new_row.append(
                triangle[row_index - 1][col_index - 1] +
                triangle[row_index - 1][col_index])

        # End the row with 1.
        new_row.append(1)

        triangle.append(new_row)

    return triangle
