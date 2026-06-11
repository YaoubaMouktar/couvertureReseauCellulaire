import math

def calculate_signal(
    station_x,
    station_y,
    power,
    cell_x,
    cell_y,
    technology="LTE"
):

    distance = math.sqrt(
        (station_x - cell_x)**2 +
        (station_y - cell_y)**2
    )

    if technology == "LTE":
        attenuation_factor = 3

    else:
        attenuation_factor = 6

    signal = max(
        power - distance * attenuation_factor,
        0
    )

    return round(signal, 1)

# import math

# def calculate_signal(
#     station_x,
#     station_y,
#     power,
#     cell_x,
#     cell_y
# ):
#     distance = math.sqrt(
#         (station_x - cell_x)**2 +
#         (station_y - cell_y)**2
#     )

#     signal = max(
#         power - distance * 5,
#         0
#     )

#     return round(signal, 1)