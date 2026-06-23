import math

def nearest_station(
    user,
    stations
):

    best_station = None

    best_distance = float("inf")

    for station in stations:

        distance = math.sqrt(
            (user.x - station.x)**2 +
            (user.y - station.y)**2
        )

        if distance < best_distance:

            best_distance = distance
            best_station = station

    return best_station

def station_loads(
    users,
    stations
):

    loads = {}

    for i in range(len(stations)):

        loads[i + 1] = 0

    for user in users:

        station = nearest_station(
            user,
            stations
        )

        index = stations.index(
            station
        )

        loads[index + 1] += 1

    return loads

def station_status(load):

    if load <= 15:
        return "Normal"

    elif load <= 25:
        return "Chargee"

    else:
        return "Saturee"