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

def covered_users(grid, users, threshold=20):

    count = 0

    for user in users:

        signal = grid[user.y][user.x]

        if signal >= threshold:

            count += 1

    return count

def uncovered_users(grid, users, threshold=20):

    return len(users) - covered_users(
        grid,
        users,
        threshold
    )

def user_coverage_percentage(
    grid,
    users,
    threshold=20
    ):

    total = len(users)

    if total == 0:
        return 0

    covered = covered_users(
        grid,
        users,
        threshold
    )

    return round(
        (covered / total) * 100,
        1
    )

def users_coverage_stats(users, grid):

    covered = 0
    uncovered = 0

    for user in users:

        signal = grid.get_cells()[
            user.y,
            user.x
        ]

        if signal >= 20:
            covered += 1
        else:
            uncovered += 1

    return covered, uncovered