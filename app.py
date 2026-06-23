import streamlit as st
from simulation.mobility import move_users
from simulation.grid import Grid
import matplotlib.pyplot as plt
from simulation.station import Station
from simulation.obstacle import Obstacle
from visualization.heatmap import show_heatmap
from visualization.metrics import (
    coverage_percentage,
    covered_cells,
    uncovered_cells,
    average_signal,
    users_coverage_stats
)
# from visualization.metrics import (
#     covered_users,
#     uncovered_users
# )
from visualization.metrics import (
    user_coverage_percentage
)
from statistics.network import (
    station_loads,
    station_status
)
from statistics.network import station_loads
from simulation.optimizer import generate_stations
from simulation.optimizer import generate_users

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
    value=75
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
    1
)

nombre_utilisateurs = st.sidebar.slider(
    "Nombre d'utilisateurs",
    1,
    100,
    5
)

#Ajouter un obstacle
obstacle_x = st.sidebar.slider(
    "Position obstacle X",
    0,
    taille - 1,
    21
    # taille // 2
)

obstacle_y = st.sidebar.slider(
    "Position obstacle Y",
    0,
    taille - 1,
    25
    # taille // 2
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
    stations = generate_stations(
        taille,
        nombre_stations,
        puissance,
        technology
    )

    grid.set_stations(stations)

    ##creation de l'utilisateur 
    users = generate_users(
        taille,
        nombre_utilisateurs
    )

    grid.set_users(users)

    # st.write("Utilisateurs :", len(grid.users))

    for user in grid.users[:1]:
    #     st.write(user.x, user.y)
        st.write("Nombre d'utilisateurs générés :",len(users))

    # Calcul de couverture
    grid.compute_multi_coverage(
        stations
    )

    #calcul de statistique des utilisateurs
    covered_users, uncovered_users = (
        users_coverage_stats(
            users,
            grid
        )
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

    st.write(
        f"Utilisateurs couverts : {covered_users}"
    )

    st.write(
        f"Utilisateurs non couverts : {uncovered_users}"
    )


    fig_users, ax = plt.subplots()

    ax.pie(
        [covered_users, uncovered_users],
        labels=[
            "Couverts",
            "Non couverts"
        ],
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Répartition des utilisateurs"
    )

    st.pyplot(fig_users)

    st.metric(
    "Taux de couverture utilisateur (%)",
        user_coverage_percentage(
            grid.get_cells(),
            users
        )
    )
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

    loads = station_loads(
    users,
    stations
    )

    station_names = []
    station_values = []

    for station_id, load in loads.items():

        station_names.append(
            f"Station {station_id}"
        )

        station_values.append(load)

    for station_id, load in loads.items():

        status = station_status(load)

        if status == "Normal":

            st.success(
                f"Station {station_id} : {load} utilisateurs"
            )

        elif status == "Chargee":

            st.warning(
                f"Station {station_id} : {load} utilisateurs"
            )

        else:

            st.error(
                f"Station {station_id} : {load} utilisateurs"
            )
    fig_load, ax = plt.subplots()

    ax.bar(
        station_names,
        station_values
    )

    ax.set_title(
        "Charge des stations"
    )

    ax.set_ylabel(
        "Nombre d'utilisateurs"
    )

    st.pyplot(fig_load)