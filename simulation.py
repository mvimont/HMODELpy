from setting import Grid

class Simulation:
    """General simulation object"""
    def __init__(self, x_axis_len : int, y_axis_len : int, years_bp : int):
        self.x_axis_len = x_axis_len
        self.y_axis_len = y_axis_len
        self.patches = dict()
        self.grid = Grid(self.x_axis_len, self.y_axis_len)