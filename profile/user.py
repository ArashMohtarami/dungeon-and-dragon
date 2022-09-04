
import re
import pathlib

from typing import (
    Tuple,
    List
)

from board.location import Location


class Profile:

    _OBJECTS_NAME: Tuple[str] = (
        "player_loc",
        "dragon_loc",
        "dungeon_loc",
        "map_helper_loc"
    )

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def write_in_file(
        self,
        object_loc: Tuple["Location"],
        level: int,
        type_char: str
    ) -> None:
        """
        write some locations in a file

        Parameters
        ----------
        object_loc : Tuple[Location]
        level : int :
        get the level of the player
        type_char : str :
        get a name of an instance class
        """
        file_address = "./data/" + self.username + ".txt"
        with open(file_address, "w") as save_file:
            for i in range(len(object_loc)):
                string = f"{self._OBJECTS_NAME[i]}: {object_loc[i]}\n"
                save_file.write(string)
            save_file.write(f"({level}, {type_char})")

    def read_from_file(self) -> List['Location']:
        """
        open a file and get some locations
        """
        file_address = "./data/" + self.username + ".txt"
        with open(file_address, "r") as f:
            pattern = r'(\w+), (\w+)'
            objects_loc = [
                re.findall(pattern, loc,)[0]
                for loc in f.readlines()
            ]
            last_one = objects_loc[-1]
            print(type(last_one))
            objects_loc = [
                Location(int(loc[0]), int(loc[1]))
                for loc in objects_loc[:-1]
            ]
            return objects_loc, last_one

    def is_save_file_exist(self) -> bool:
        """check is a special file exist. """
        file_address = "./data/" + self.username + ".txt"
        return True if pathlib.Path(file_address).is_file() else False  # noqa

    def write_userpass(self) -> None:
        """ write username and password in dir : ./data/data.txt"""
        string = f"({self.username},{self.password})\n"
        with open("./data/data.txt", "a") as file:
            file.write(string)

    @classmethod
    def read_userpass(self):
        """ read username and password from dir : ./data/data.txt"""
        pattern = r"\(([\w\W]+),([\w\W]+)\)"
        with open("./data/data.txt", "r") as file:
            rows = file.readlines()
            users_list = [
                re.findall(pattern, row)
                for row in rows
            ]
        users_list = [
            user[0]
            for user in users_list
        ]
        return users_list

    def is_userpass_valid(self) -> bool:
        """ check username and password are true or not"""
        return True if (self.username, self.password) \
            in self.read_userpass() else False

    def is_username_exist(self) -> bool:
        """check username exist or not"""
        exist = False
        for userpass in self.read_userpass():
            if self.username == userpass[0]:
                exist = True
                break
        return exist

    def safe_password(self) -> bool:
        """check password is safe or not"""
        is_valid = False
        pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$'
        if re.match(pattern, self.password):
            is_valid = True
        return is_valid
