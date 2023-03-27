"""A module with 2d and 3d coordinate classes."""

from dataclasses import dataclass


@dataclass(eq=True)
class Coord2d:
    """A single 2D Coordinate"""

    x: int | float
    y: int | float


@dataclass(eq=True)
class Coord3d:
    """A single 3D Coordinate"""

    x: int | float
    y: int | float
    z: int | float


def main():
    point = Coord2d(5, 2.0)
    print(point)


if __name__ == "__main__":
    main()
