from simulation.station import Station
from simulation.user import User
import random

def generate_stations(
    grid_size,
    number_stations,
    power,
    technology
):

    stations = []

    spacing = grid_size // (number_stations + 1)

    for i in range(number_stations):

        x = spacing * (i + 1)

        y = grid_size // 2

        stations.append(
            Station(
                x=x,
                y=y,
                power=power,
                technology=technology
            )
        )
    return stations

def generate_users(
    grid_size,
    number_users
    ):

    users = []

    for _ in range(number_users):

        users.append(
            User(
                random.randint(0, grid_size - 1),
                random.randint(0, grid_size - 1)
            )
        )

    return users

    