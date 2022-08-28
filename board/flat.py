from random import sample
from typing import (
    Tuple,
    List
)

from board.location import Location


class Map:
    """ Dungeon & Dragon game map """

    __DIRECTIONS: Tuple = ('left', 'right', 'top', 'bottom')
    WEST, EAST, NORTH, SOUTH = __DIRECTIONS

    def __init__(self, dimension, *args, **kwargs) -> None:
        self.dimension = dimension
        self.__CELLS = [
            Location(col, row)
            for col in range(1, 1 + self.dimension)
            for row in range(1, 1 + self.dimension)
        ]

    @property
    def dimension(self) -> int:
        """ Get dimensions of the map """
        return self.__dimension

    @dimension.setter
    def dimension(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            Get value of dimensions

        Returns
        -------
        Set dimensions of the map.
        """

        if isinstance(value, int):
            if value >= 5:
                self.__dimension = value
            else:
                raise ValueError("Minimum value of dimension is 5.")
        else:
            raise TypeError("Value must be an integer")

    def show_board(self, *args) -> None:
        """

        Parameters
        ----------
        *args :
            show `args` argument on the map with a
            `P`-> Player , `D`-> Dragon mark.

        Returns
        -------
        print the game map in the terminal.
        """
        print(' _'*self.dimension)
        __counter = 0
        for loc in self.__CELLS:
            __counter += 1
            if loc == args[0]:
                print("|P|" if loc.Y == 1 else "P|", end="")
            elif loc not in args:
                print("|_|" if loc.Y == 1 else "_|", end="")
            elif len(args) == 2:
                if loc == args[1]:
                    print("|D|" if loc.Y == 1 else "D|", end="")
            if __counter % self.dimension == 0:
                print()

    def get_locations(self, sample_num: int = 1) -> List:
        """

        Parameters
        ----------
        sample_num: int :
            (Default value = 1)

            Chooses `sample_num` unique random
            elements from a CELL population sequence.

        Returns
        -------
        Get one or more Axis instances
        """
        self.sample_num = sample_num
        return sample(self.__CELLS, sample_num)

    @property
    def sample_num(self) -> int:
        """Get the  sample_num"""
        return self.__sample_num

    @sample_num.setter
    def sample_num(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            Get the  value of sample_num

        Returns
        -------
        Set the  sample_num
        """

        if isinstance(value, int):
            if value >= 1:
                self.__sample_num = value
            else:
                raise ValueError("Minimum value of dimension is 1.")
        else:
            raise TypeError("Value must be an integer")

    def get_limitation(self, player: "Location") -> Tuple[str]:
        """

        Parameters
        ----------
        player: "Location" :
            Get location of player

        Returns
        -------
        Limitation of player moving
        """
        moves = list(self.__DIRECTIONS)
        MAX = self.dimension
        if player.X == 1:
            moves.remove("top")
        if player.Y == 1:
            moves.remove("left")
        if player.X == MAX:
            moves.remove("bottom")
        if player.Y == MAX:
            moves.remove("right")
        return tuple(moves)

    def distance_player_dragon(
        self, player_loc: 'Location',
        dragon_loc: 'Location'
    ) -> float:
        """

        Parameters
        ----------
        player_loc: 'Location' :
            Get location of player
        dragon_loc: 'Location' :
            Get location of dragon

        Returns
        -------
        distance between dragon and player
        """

        distance = Location.distance(player_loc, dragon_loc)
        return distance

    def dragon_option_move(
        self,
        player_loc: "Location",
        dragon_loc: "Location"
    ) -> str:
        """

        Parameters
        ----------
        player_loc: "Location" :
            Get location of player
        dragon_loc: "Location" :
            Get location of dragon

        Returns
        -------
        Limitation of dragon moving
        """
        delta_x = player_loc.X - dragon_loc.X
        delta_y = player_loc.Y - dragon_loc.Y
        is_player_x_farther = player_loc.X > dragon_loc.X
        is_player_y_farther = player_loc.Y > dragon_loc.Y
        direction: str
        if delta_x == 0:
            if is_player_y_farther:
                direction = ["right"]
            else:
                direction = ["left"]
        elif delta_y == 0:
            if is_player_x_farther:
                direction = ["bottom"]
            else:
                direction = ["top"]
        elif is_player_x_farther:

            if is_player_y_farther:
                direction = sample(("right", "bottom"), 1)
            else:
                direction = sample(("left", "bottom"), 1)

        elif is_player_y_farther:

            if is_player_x_farther:
                direction = sample(("right", "top"), 1)
            else:
                direction = sample(("right", "bottom"), 1)

        elif not is_player_x_farther:

            if is_player_y_farther:
                direction = sample(("right", "top"), 1)
            else:
                direction = sample(("left", "top"), 1)

        elif not is_player_y_farther:

            if is_player_x_farther:
                direction = sample(("left", "bottom"), 1)
            else:
                direction = sample(("left", "top"), 1)
        return direction[0]

    def move(self, direction: str, player_loc: "Location"):
        """

        Parameters
        ----------
        direction: str :
            Get direction for movement
        player_loc: "Location" :
            Get location of player

        Returns
        -------
        move the player
        """
        return player_loc.move(direction)

    def __str__(self) -> str:
        return f'Map <{self.dimension}x{self.dimension}>'

    def __repr__(self) -> str:
        return f'Map <{self.dimension}x{self.dimension}>'
