from itertools import product

class Grid:
    def __init__(self, x_axis_len : int, y_axis_len : int):
        self.x_axis_len = x_axis_len
        self.y_axis_len = y_axis_len
        self.patches = self._set_patches()

    def _set_patches(self):
        x_list = list(range(0, self.x_axis_len))
        y_list = list(range(0, self.y_axis_len))
        for coordinate in product(x_list + y_list):
            self.patches[coordinate] = Patch(coordinate)

class Patch:
    def __init__(self, position : tuple):
        self.position = position
        self.sediment_age = 0
    
    def increment_sediment_age(self, years : int):
        self.sediment_age += 1