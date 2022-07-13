class Hearth:
    def __init__(self, position : tuple, age : int, charcoal : bool):
        self.age = age
        self.charcoal = charcoal
        self.position = position
        self.hidden = False

class Human:
    def __init__(self):
        self.position = tuple
    
    def set_position(self, x : int, y : int):
        self.position = (x, y)
    
    def build_hearth(self, years_bp : int):
        if years_bp < 200:
            return Hearth(self.position, age=0, charcoal=True)