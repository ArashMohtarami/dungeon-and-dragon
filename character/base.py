from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Dict,
)


class ICharacter(ABC):
    """Base of Character """

    actions: Dict = dict()

    def __init__(self, name: str, experience: int = 0, *args, **kwargs):
        self.name = name
        self.experience = experience
        self.actions.update({
            'a': 'attack',
            'f': 'flee'
        })

    @property
    @abstractmethod
    def attack_damage(self) -> None:
        raise NotImplementedError("Subclasses should implement this!")

    @attack_damage.setter
    @abstractmethod
    def attack_damage(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            `value` must be a positive integer

        Returns
        -------
        Set the value of attack_damage
        """
        raise NotImplementedError("Subclasses should implement this!")

    @property
    @abstractmethod
    def health(self) -> None:
        raise NotImplementedError("Subclasses should implement this!")

    @health.setter
    @abstractmethod
    def health(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            `value` must be a positive integer

        Returns
        -------
        Set the value of health
        """
        raise NotImplementedError("Subclasses should implement this!")

    @property
    def name(self) -> str:
        """ Get name"""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """

        Parameters
        ----------
        value: str :
            `value` must be a string

        Returns
        -------
        Set name
        """
        if isinstance(value, str):
            if value.isalpha():
                self.__name = value
            else:
                raise ValueError("`name` just accept alphabetic values.")
        else:
            raise TypeError(
                f'Your name data type is {type(value)} but `name` supports string!' # noqa
            )

    @property
    def experience(self) -> int:
        """ Get the value of experience"""
        return self.__experience

    @experience.setter
    def experience(self, value: int) -> None:
        """

        Parameters
        ----------
        value: int :
            `value` must be a positive integer number

        Returns
        -------
        Set the value of experience
        """
        if isinstance(value, int):
            if value >= 0:
                self.__experience = value
            else:
                raise ValueError("`experience` just accept positive integers!")
        else:
            raise TypeError(
                f'`experience` data type is {type(value)} but `experience` supports integer!' # noqa
            )

    def __str__(self) -> str:
        return F"<class Character({self.name})>"

    def __repr__(self) -> str:
        return F"<class Character({self.name})>"
