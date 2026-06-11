import numpy as np

def coverage_percentage(grid, threshold=30):
    total_cells = grid.size

    covered_cells = np.sum(grid >= threshold)

    percentage = (covered_cells / total_cells) * 100

    return round(percentage, 2)


def covered_cells(grid, threshold=30):
    return np.sum(grid >= threshold)


def uncovered_cells(grid, threshold=30):
    return np.sum(grid < threshold)


def average_signal(grid):
    return round(np.mean(grid), 2)