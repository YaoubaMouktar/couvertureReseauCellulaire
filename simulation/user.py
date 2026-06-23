class User:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def move(
        self,
        max_x,
        max_y
    ):

        import random

        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        self.x = max(
            0,
            min(self.x, max_x - 1)
        )

        self.y = max(
            0,
            min(self.y, max_y - 1)
        )