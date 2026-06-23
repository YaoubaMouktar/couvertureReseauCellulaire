import numpy as np
from simulation.propagation import calculate_signal

class Grid:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = np.zeros((height, width))

        self.obstacles = []

        self.stations = []

        self.users = []

    def get_cells(self):
        return self.cells

    def set_stations(self, stations):

        self.stations = stations

    def set_users(self, users):

        self.users = users
        
    def add_obstacle(self, obstacle):

        self.obstacles.append(obstacle)

    def compute_coverage(self, station):

        for y in range(self.height):
            for x in range(self.width):

                signal = calculate_signal(
                    station.x,
                    station.y,
                    station.power,
                    x,
                    y
                )

                self.cells[y][x] = signal
    def compute_multi_coverage(self, stations):

        for y in range(self.height):
            for x in range(self.width):

                best_signal = 0

                for station in stations:

                    signal = calculate_signal(
                        station.x,
                        station.y,
                        station.power,
                        x,
                        y,
                        station.technology
                    )
                    for obstacle in self.obstacles:

                        if (
                            obstacle.x <= x < obstacle.x + obstacle.width
                             and
                            obstacle.y <= y < obstacle.y + obstacle.height
                            ):

                            signal = max(
                                signal - obstacle.attenuation,
                                0
                            )

                    best_signal = max(
                        best_signal,
                        signal
                    )

                self.cells[y][x] = best_signal
