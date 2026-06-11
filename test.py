import matplotlib.pyplot as plt
from simulation.grid import Grid
from simulation.station import Station
from simulation.propagation import calculate_signal
from visualization.heatmap import show_heatmap
import numpy as np
from visualization.metrics import (
    coverage_percentage,
    covered_cells,
    uncovered_cells,
    average_signal
)

# Création de la grille
grid = Grid(50, 50)

# Création d'une station LTE
station = Station(
    x=25,
    y=25,
    power=100,
    radius=15
)

# Test du calcul du signal
signal = calculate_signal(
    station_x=25,
    station_y=25,
    power=100,
    cell_x=30,
    cell_y=30
)

print("Signal :", signal)

# Calcul de la couverture
grid.compute_coverage(station)
print("Centre :", grid.get_cells()[25][25])
print("Coin :", grid.get_cells()[0][0])
print("Maximum :", grid.get_cells().max())
print("Minimum :", grid.get_cells().min())

np.set_printoptions(
    precision=1,
    suppress=True
)
# Affichage de la matrice
print(grid.get_cells()[20:31,20:31])

# Affichage de la heatmap
fig = show_heatmap(
    grid.get_cells()
)

print("Couverture :", coverage_percentage(grid.get_cells()), "%")
print("Cellules couvertes :", covered_cells(grid.get_cells()))
print("Zones blanches :", uncovered_cells(grid.get_cells()))
print("Signal moyen :", average_signal(grid.get_cells()))
fig.show()

stations = [

    Station(
        x=10,
        y=10,
        power=100
    ),

    Station(
        x=40,
        y=10,
        power=100
    ),

    Station(
        x=25,
        y=25,
        power=100
    ),

    Station(
        x=10,
        y=40,
        power=100
    ),

    Station(
        x=40,
        y=40,
        power=100
    )
]

grid.compute_multi_coverage(stations)