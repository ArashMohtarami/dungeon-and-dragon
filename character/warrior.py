from character.base import ICharacter


class BarbarianWarrior(ICharacter):
    """ BarbarianWarrior a kind of Character in the game """

    def __init__(
        self,
        name: str,
        experience: int = 0,
        *args,
        **kwargs
    ) -> None:
        super().__init__(name, experience, *args, **kwargs)
        self.actions.update({
            "pd": "power damage"
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

    def power_damage(self, VALUE: int) -> int:
        """

        Parameters
        ----------
        VALUE: int :
            `value` must be a positive integer number

        Returns
        -------
        improve the power of damage
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
        return F'{self.name} Warrior'

    def __repr__(self) -> str:
        return F'{self.name} Warrior'


class FighterWarrior(ICharacter):
    """ FighterWarrior a kind of Character in the game """

    def __init__(
        self,
        name: str,
        experience: int = 0,
        *args,
        **kwargs
    ) -> None:
        super().__init__(name, experience, *args, **kwargs)
        self.actions.update({
            "sd": "speed damage",
            "e": "endurance"
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

    def speed_damage(self, VALUE: int) -> int:
        """

        Parameters
        ----------
        VALUE: int :
            `value` must be a positive integer number

        Returns
        -------
        improve the rate of damage
        """
        self.VALUE = VALUE
        return VALUE

    def endurance_health(self, VALUE: int) -> int:
        """

        Parameters
        ----------
        VALUE: int :
            `value` must be a positive integer number

        Returns
        -------
        improve of health
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
        return F'{self.name} Warrior'

    def __repr__(self) -> str:
        return F'{self.name} Warrior'
