import math
from typing import Tuple


class Axis:
    """
    Displays the coordinates of a point.
    It also has capabilities such as leading a point to
    one of the cardinal directions.

    For example coordinate of point is 10, 5:
        >>> Axis(10, 5)
        Axis (10, 5)
    """

    def __init__(self, x_axis: int, y_axis: int) -> None:
        self.X = x_axis
        self.Y = y_axis

    @property
    def X(self) -> int:
        """ Get X coordinate of axis """
        return self.__X

    @X.setter
    def X(self, value: int) -> None:
        """
        Set X coordinate of Axis instance

        Parameters
        ----------
        value: int :
            value must be a positive integer number

        Returns
        -------
        None - just set x coordinate to Axis instance
        """
        if isinstance(value, int):
            self.__X = value
        else:
            raise TypeError("The value must be integer")

    @property
    def Y(self) -> int:
        """ Get Y coordinate of axis """
        return self.__Y

    @Y.setter
    def Y(self, value: int) -> None:
        """
        Set Y coordinate of axis

        Parameters
        ----------
        value: int :
            value must be a positive integer number

        Returns
        -------
        None - just set y coordinate to Axis instance
        """
        if isinstance(value, int):
            self.__Y = value
        else:
            raise TypeError("The value must be integer")

    def distance(self, axis: 'Axis') -> float:
        """
        Multidimensional Euclidean distance from the origin to a point.

        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))

        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).

        For example, the hypotenuse of a 3/4/5 right triangle is:

            >>> hypot(3.0, 4.0)
            5.0

        `Note`: The math.hypot() method returns the Euclidean norm.

        Parameters
        ----------
        axis: 'Axis' :
            Axis instance

        Returns
        -------
        `float`
        """
        dx = abs(self.X - axis.X)
        dy = abs(self.Y - axis.Y)
        return math.hypot(dx, dy)

    @classmethod
    def lead_north(cls) -> Tuple[int, int]:
        """
        Lead an origin axis to a north point of it.

        for example, north of Axis(3, 4) is:
            >>> Axis(3, 4) + Axis.lead_north()
                Axis(3, 3)
        """

        return cls(-1, 0)

    @classmethod
    def lead_south(cls) -> Tuple[int, int]:
        """
        Lead an origin axis to a south point of it.

        for example, south of Axis(3, 4) is:
            >>> Axis(3, 4) + Axis.lead_south()
                Axis(3, 5)
        """

        return cls(1, 0)

    @classmethod
    def lead_west(cls) -> Tuple[int, int]:
        """
        Lead an origin axis to a left point of it.

        for example, west of Axis(3, 4) is:
            >>> Axis(3, 4) + Axis.lead_west()
                Axis(2, 4)
        """
        return cls(0, -1)

    @classmethod
    def lead_east(cls) -> Tuple[int, int]:
        """
        Lead an origin axis to a east point of it.

        for example, east of Axis(3, 4) is:
            >>> Axis(3, 4) + Axis.lead_east()
                Axis(4, 4)
        """

        return cls(0, 1)

    def __add__(self, axis: 'Axis') -> 'Axis':
        x = self.X + axis.X
        y = self.Y + axis.Y
        return Axis(x, y)

    def __iadd__(self, axis: 'Axis') -> 'Axis':
        x = axis.X + self.X
        y = axis.Y + self.Y
        return Axis(x, y)

    def __sub__(self, axis: 'Axis') -> 'Axis':
        x = self.X - axis.X
        y = self.Y - axis.Y
        return Axis(x, y)

    def __isub__(self, axis: 'Axis') -> 'Axis':
        x = axis.X - self.X
        y = axis.Y - self.Y
        return Axis(x, y)

    def __str__(self) -> str:
        return f'Axis({self.X}, {self.Y})'

    def __repr__(self) -> str:
        return f'Axis({self.X}, {self.Y})'


class Location(Axis):
    """ """

    __DIRECTIONS = ('left', 'right', 'top', 'bottom')

    def __init__(self, x_axis, y_axis) -> None:
        super().__init__(x_axis, y_axis)
        self.current = Axis(x_axis, y_axis)

    def move(self, direction: str) -> "Location":
        """
        To move a point in one of the cardinal directions.

        For example:
            >>> loc = Location(10, 3)
            >>> loc.move('left')
            Location (9, 3)
        Parameters
        ----------
        direction: str :
            one of choices of DIRECTIONS.
            valid choices are `left`, `right`, `top`, `bottom`

        Returns
        -------
        Location instance
        """
        WEST, EAST, NORTH, SOUTH = self.__DIRECTIONS
        self.direction = direction

        if direction == EAST:
            new_loc = self.current + Axis.lead_east()
        elif direction == WEST:
            new_loc = self.current + Axis.lead_west()
        elif direction == NORTH:
            new_loc = self.current + Axis.lead_north()
        elif direction == SOUTH:
            new_loc = self.current + Axis.lead_south()
        self.current = new_loc
        return Location(self.current.X, self.current.Y)

    @property
    def direction(self) -> str:
        """Get direction """
        return self.__direction

    @direction.setter
    def direction(self, value: str) -> None:
        """

        Parameters
        ----------
        value: str :
            Get a string value

        Returns
        -------
        Set the direction
        """
        if isinstance(value, str):
            if value.isalpha():
                if value in self.__DIRECTIONS:
                    self.__direction = value.lower()
                else:
                    raise ValueError(
                        "valid choices are 'left', 'right', 'top', 'bottom'")
            else:
                raise ValueError("value must be alphabetic")
        else:
            raise TypeError("value must be string")

    @property
    def current(self) -> 'Axis':
        """Get current value """
        return self.__current

    @current.setter
    def current(self, value: 'Axis') -> None:
        """

        Parameters
        ----------
        value: 'Axis' :
            Get current value

        Returns
        -------
        Set current value
        """
        self.__current = value

    def __eq__(self, other: "Location") -> bool:
        return self.X == other.X and self.Y == other.Y

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __lt__(self, map_) -> bool:
        upper_bound = map_.dimension + 1
        return self.X < upper_bound and self.Y < upper_bound

    def __str__(self) -> str:
        return f"Location({self.X}, {self.Y})"

    def __repr__(self) -> str:
        return f"Location({self.X}, {self.Y})"
