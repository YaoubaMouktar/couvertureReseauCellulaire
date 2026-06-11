from simulation.station import Station

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