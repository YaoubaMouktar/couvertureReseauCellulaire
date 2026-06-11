class Station:

    def __init__(
        self,
        x,
        y,
        power,
        technology="LTE",
        radius=15
    ):

        self.x = x
        self.y = y
        self.power = power
        self.radius = radius
        self.technology = technology