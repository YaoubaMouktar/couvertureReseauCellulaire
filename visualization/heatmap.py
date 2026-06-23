import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D

def show_heatmap(grid_obj):

    fig, ax = plt.subplots(figsize=(8, 8))

    image = ax.imshow(
        grid_obj.get_cells(),
        cmap="turbo"
    )

    plt.colorbar(
        image,
        label="Puissance du signal"
    )

    # Affichage des obstacles
    for obstacle in grid_obj.obstacles:

        rectangle = patches.Rectangle(
            (obstacle.x, obstacle.y),
            obstacle.width,
            obstacle.height,
            fill=False
        )

        ax.add_patch(rectangle)

    # Affichage des stations
    for station in grid_obj.stations:

        if station.technology == "LTE":
            color = "blue"
        else:
            color = "purple"

        ax.scatter(
            station.x,
            station.y,
            marker="^",
            s=250,
            color=color
        )

        ax.text(
            station.x,
            station.y - 2,
            station.technology,
            fontsize=8,
            ha="center"
        )

    # Affichage des utilisateurs
    for user in grid_obj.users:

        signal = grid_obj.get_cells()[
            user.y
        ][
            user.x
        ]

        if signal >= 20:

            color = "green"

        else:

            color = "red"

        ax.scatter(
            user.x,
            user.y,
            marker="o",
            s=50,
            color=color
        )

    legend_elements = [

        Line2D(
            [0],
            [0],
            marker='^',
            color='w',
            label='Station',
            markerfacecolor='blue',
            markersize=10
        ),

        Line2D(
            [0],
            [0],
            marker='o',
            color='w',
            label='Utilisateur couvert',
            markerfacecolor='green',
            markersize=8
        ),

        Line2D(
            [0],
            [0],
            marker='o',
            color='w',
            label='Utilisateur non couvert',
            markerfacecolor='red',
            markersize=8
        )

    ]

    ax.legend(
        # handles=legend_elements,
        # bbox_to_anchor=(1.25, 1),
        # loc="upper left"
        handles=legend_elements,
        loc="lower left",
        bbox_to_anchor=(0.5, 1.02),
        #ncol=3
    )

    return fig