# Part 6.2 (Road)

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def total_mass(self, square_mass, thickness):
        print(self._length * self._width * square_mass * thickness)


road = Road(2000, 8)
road.total_mass(5, 10)

