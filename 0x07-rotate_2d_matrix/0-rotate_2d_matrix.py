#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an n by n 2D matrix in place.
    """
    if not isinstance(matrix, list):
        return
    if len(matrix) <= 0:
        return
    if not all(isinstance(row, list) for row in matrix):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(len(row) == cols for row in matrix):
        return

    n = len(matrix)

    # Perform the rotation in place
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
