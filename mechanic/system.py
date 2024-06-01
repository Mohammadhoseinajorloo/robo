import enum

class Quantity(enum.Enum):
    SCALER = 0
    VECTOR = 1

class Body:
    def __init__(self, position:tuple=(0,0)):
        '''A system is formed from the juxtaposition of several Body in the mechanics
        ===
        input:
        1. position -> tuple (defult=(0,0))
            An object is expressed by choosing a coordinate system (which can be 2D or 3D).
            - 2D (x, y)
            - 3D (x, y, z)
        '''
        self._position = position

class System:
    def __init__(self, bodys:list):
        self._bodys = bodys
