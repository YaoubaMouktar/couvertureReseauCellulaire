import streamlit as st

from simulation.grid import Grid
from simulation.station import Station
from simulation.obstacle import Obstacle
from visualization.heatmap import show_heatmap
from visualization.metrics import (
    coverage_percentage,
    covered_cells,
    uncovered_cells,
    average_signal
)
from simulation.optimizer import generate_stations

# Titre
st.title("Simulation de couverture LTE/5G")

st.write(
    "Simulation de la propagation du signal LTE/5G "
    "à l'aide d'une grille d'automates cellulaires."
)

# Paramètres dans la barre latérale
st.sidebar.header("Paramètres")

taille = st.sidebar.slider(
    "Taille de la grille",
    min_value=20,
    max_value=100,
    value=50
)

puissance = st.sidebar.slider(
    "Puissance de la station",
    min_value=50,
    max_value=200,
    value=100
)

nombre_stations = st.sidebar.slider(
    "Nombre de stations",
    1,
    5,
    3
)

#Ajouter un obstacle
obstacle_x = st.sidebar.slider(
    "Position obstacle X",
    0,
    taille - 1,
    taille // 2
)

obstacle_y = st.sidebar.slider(
    "Position obstacle Y",
    0,
    taille - 1,
    taille // 2
)

obstacle_width = st.sidebar.slider(
    "Largeur bâtiment",
    1,
    20,
    5
)

obstacle_height = st.sidebar.slider(
    "Hauteur bâtiment",
    1,
    20,
    5
)

technology = st.sidebar.selectbox(
    "Technologie",
    ["LTE", "5G"]
)

# Bouton de simulation
if st.button("Lancer la simulation"):

    # Création de la grille
    grid = Grid(taille, taille)

    grid.add_obstacle(
    Obstacle(
            obstacle_x,
            obstacle_y,
            obstacle_width,
            obstacle_height,
            attenuation=50
        )
    )

    # Création de la station
    stations = []

    positions = [
        (10,10),
        (40,10),
        (25,25),
        (10,40),
        (40,40)
    ]

    for i in range(nombre_stations):

        x, y = positions[i]

        stations.append(
            Station(
                x=x,
                y=y,
                power=puissance,
                technology=technology
            )
        )

    # Calcul de couverture
    grid.compute_multi_coverage(
        stations
    )

    # Affichage de la carte
    fig = show_heatmap(
        grid
    )
    # fig = show_heatmap(
    #     grid.get_cells()
    # )

    st.pyplot(fig)
    st.subheader("Statistiques")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            "Couverture (%)",
            coverage_percentage(
            grid.get_cells()
            )
        )

        st.metric(
            "Cellules couvertes",
            covered_cells(
            grid.get_cells()
            )
        )

    with col2:
        st.metric(
            "Zones blanches",
            uncovered_cells(
            grid.get_cells()
            )
        )

        st.metric(
            "Signal moyen",
            average_signal(
            grid.get_cells()
            )
        )


    # Quelques informations
    st.success("Simulation terminée.")

    st.write(
        f"Puissance maximale : {grid.get_cells().max():.1f}"
    )

    st.write(
        f"Puissance minimale : {grid.get_cells().min():.1f}"
    )