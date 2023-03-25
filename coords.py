"""A module with 2d and 3d coordinate classes."""

from pyutil.decorators import expects


class Coord2d:
    """A single 2D Coordinate"""

    @expects(int | float, int | float, method=True)
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __repr__(self):
        return f"Coord2d(x={self._x}, y={self._y})"

    def __eq__(self, other):
        if isinstance(other, Coord2d):
            return self._x == other.x and self._y == other.y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    @expects(int | float, method=True)
    def x(self, new_x):
        self._x = new_x

    @y.setter
    @expects(int | float, method=True)
    def y(self, new_y):
        self._y = new_y


class Coord3d:
    """A single 3D Coordinate"""

    @expects(int | float, int | float, int | float, method=True)
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return f"({self._x}, {self._y}, {self._z})"

    def __repr__(self):
        return f"Coord3d(x={self._x}, y={self._y}, z={self._z})"

    def __eq__(self, other):
        if isinstance(other, Coord3d):
            return self._x == other.x and self._y == other.y and self._z == other.z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    @expects(int | float, method=True)
    def x(self, new_x):
        self._x = new_x

    @y.setter
    @expects(int | float, method=True)
    def y(self, new_y):
        self._y = new_y

    @z.setter
    @expects(int | float, method=True)
    def z(self, new_z):
        self._z = new_z


def main():
    point = Coord2d(5, 2.0)
    point.y = .2
    point.x = b"hello!"


if __name__ == "__main__":
    main()
