import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

    for obstacle in grid_obj.obstacles:

        rectangle = patches.Rectangle(
            (obstacle.x, obstacle.y),
            obstacle.width,
            obstacle.height,
            fill=False
        )

        ax.add_patch(rectangle)
        # ax.scatter(
        #     obstacle.x,
        #     obstacle.y,
        #     marker="s",
        #     s=150
        # )

    ax.set_title(
        "Couverture LTE/5G"
    )

    return fig
# import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt

# def show_heatmap(grid):

#     fig, ax = plt.subplots(figsize=(8, 8))

#     image = ax.imshow(
#         grid,
#         cmap="turbo"
#     )

#     plt.colorbar(
#         image,
#         label="Puissance du signal"
#     )

#     ax.set_title(
#         "Couverture LTE/5G"
#     )

#     return fig
