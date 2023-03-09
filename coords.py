class Coord2d:
    """A single 2D Coordinate"""

    def __init__(self, x, y):
        if not isinstance(x, (int, float)):
            raise TypeError("x only accepts an int or a float")
        self._x = x
        if not isinstance(y, (int, float)):
            raise TypeError("y only accepts an int or a float")
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"

    def __eq__(self, other):
        if isinstance(other, Coord2d):
            return self._x == other.get_x() and self._y == other.get_y()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, new_x):
        if not isinstance(new_x, (int, float)):
            raise TypeError("x only accepts an int or a float")
        self._x = new_x

    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, (int, float)):
            raise TypeError("y only accepts an int or a float")
        self._y = new_y


class Coord3d:
    """A single 3D Coordinate"""

    def __init__(self, x, y, z):
        if not isinstance(x, (int, float)):
            raise TypeError("x only accepts an int or a float")
        self._x = x
        if not isinstance(y, (int, float)):
            raise TypeError("y only accepts an int or a float")
        self._y = y
        if not isinstance(z, (int, float)):
            raise TypeError("z only accepts an int or a float")
        self._z = z

    def __str__(self):
        return f"({self._x}, {self._y}, {self._z})"

    def __eq__(self, other):
        if isinstance(other, Coord3d):
            return self._x == other.get_x() and self._y == other.get_y() and self._z == other.get_z()

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
    def x(self, new_x):
        if not isinstance(new_x, (int, float)):
            raise TypeError("x only accepts an int or a float")
        self._x = new_x

    @y.setter
    def y(self, new_y):
        if not isinstance(new_y, (int, float)):
            raise TypeError("y only accepts an int or a float")
        self._y = new_y

    @z.setter
    def sz(self, new_z):
        if not isinstance(new_z, (int, float)):
            raise TypeError("z only accepts an int or a float")
        self._z = new_z
