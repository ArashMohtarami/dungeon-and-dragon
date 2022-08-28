from typing import (
    Tuple,
    Dict
)

from character.base import ICharacter


class SniperArcher(ICharacter):
    """ SniperArcher a kind of Character in the game """

    actions: Dict[str, str]

    def __init__(self, name: str, experience: int = 0, *args, **kwargs):
        super().__init__(name, experience, *args, **kwargs)
        self.actions.update({
            "lr": "long range"
        })

    @property
    def attack_damage(self) -> int:
        """ Get value of attack_damage"""
        return self.__attack_damage

    @attack_damage.setter
    def attack_damage(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            `value` must be a positive integer number

        Returns
        -------
        Set value of attack_damage
        """
        if isinstance(value, int):
            if value >= 0:
                self.__attack_damage = value
            else:
                raise ValueError("value must be positive")
        else:
            raise TypeError("value must be an integer")

    @property
    def health(self) -> int:
        """ Get value of health"""
        return self.__health

    @health.setter
    def health(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            `value` must be a positive integer number

        Returns
        -------
        Set value of health
        """
        if isinstance(value, int):
            if value >= 0:
                self.__health = value
            else:
                raise ValueError("value must be positive")
        else:
            raise TypeError("value must be an integer")

    def fire_distance(self, VALUE: int) -> int:
        """

        Parameters
        ----------
        VALUE: int :
            `value` must be a positive integer number

        Returns
        -------
        Range of fire
        """
        self.VALUE = VALUE
        return VALUE

    def fire_speed(self, VALUE: int) -> int:
        """

        Parameters
        ----------
        VALUE: int :
            `value` must be a positive integer number

        Returns
        -------
        Speed of fire
        """
        self.VALUE = VALUE
        return VALUE

    @property
    def VALUE(self) -> int:
        """ Get the VALUE"""
        return self.__VALUE

    @VALUE.setter
    def VALUE(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            `value` must be a positive integer number

        Returns
        -------
        Set the VALUE
        """
        if isinstance(value, int):
            self.__VALUE = value
        else:
            raise TypeError("value must be an integer")

    def __str__(self) -> str:
        return F'{self.name} Archer'

    def __repr__(self) -> str:
        return F'{self.name} Archer'


class RangerArcher(ICharacter):
    """ RangerArcher a kind of Character in the game """

    def __init__(self, name: str, experience: int = 0, *args, **kwargs):
        super().__init__(name, experience, *args, **kwargs)
        self.actions.update({
            "h": "hidden itself",
            "k": "knowledge"
        })

    @property
    def attack_damage(self) -> int:
        """ Get value of attack_damage"""
        return self.__attack_damage

    @attack_damage.setter
    def attack_damage(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            `value` must be a positive integer number

        Returns
        -------
        Set value of attack_damage
        """
        if isinstance(value, int):
            if value >= 0:
                self.__attack_damage = value
            else:
                raise ValueError("value must be positive")
        else:
            raise TypeError("value must be an integer")

    @property
    def health(self) -> int:
        """ Get value of health"""
        return self.__health

    @health.setter
    def health(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            `value` must be a positive integer number

        Returns
        -------
        Set value of health
        """
        if isinstance(value, int):
            if value >= 0:
                self.__health = value
            else:
                raise ValueError("value must be positive")
        else:
            raise TypeError("value must be an integer")

    def hidden_time(self, VALUE: int) -> int:
        """

        Parameters
        ----------
        VALUE: int :
            `value` must be a positive integer number

        Returns
        -------
        The amount of time to hide
        """
        self.VALUE = VALUE
        return VALUE

    @property
    def VALUE(self) -> int:
        """ Get the VALUE"""
        return self.__VALUE

    @VALUE.setter
    def VALUE(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            `value` must be a positive integer number

        Returns
        -------
        Set the VALUE
        """
        if isinstance(value, int):
            self.__VALUE = value
        else:
            raise TypeError("value must be an integer")

    def teleport_magic(self, loc: Tuple) -> Tuple[int]:
        """

        Parameters
        ----------
        loc: Tuple :
            `loc` must be a positive tuple(integer) number

        Returns
        -------
        teleport the player
        """
        self.loc = loc
        return loc

    @property
    def loc(self) -> Tuple[int]:
        """ Get the loc"""
        return self.__loc

    @loc.setter
    def loc(self, value: Tuple[int]) -> None:
        """

        Parameters
        ----------
        value: Tuple[int] :
            `loc` must be a positive tuple(integer) number

        Returns
        -------
        Set the VALUE
        """
        if isinstance(value, Tuple):
            self.__loc = value
        else:
            raise TypeError("value must be a Tuple")

    def __str__(self) -> str:
        return F'{self.name} Archer'

    def __repr__(self) -> str:
        return F'{self.name} Archer'
