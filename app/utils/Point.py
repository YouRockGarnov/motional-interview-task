

class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __sub__(self, other):
        return Point(self._x - other.x, self._y - other.y)

    def __abs__(self):
        return abs(self._x) + abs(self._y)

    def __eq__(self, other):
        return self._x == other.x and self._y == other.y