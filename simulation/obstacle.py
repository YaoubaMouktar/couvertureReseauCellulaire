class Obstacle:

    def __init__(
        self,
        x,
        y,
        width=5,
        height=5,
        attenuation=30
    ):

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.attenuation = attenuation
# class Obstacle:

#     def __init__(self, x, y, attenuation=30):

#         self.x = x
#         self.y = y
#         self.attenuation = attenuation