def move_users(
    users,
    grid_size
):

    for user in users:

        user.move(
            grid_size,
            grid_size
        )