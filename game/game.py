import re
import pathlib
import logging

from time import sleep
from random import randint
from typing import (
    List,
    Tuple
)

import pyfiglet

from board.flat import Map
from board.location import Location
from helper.utils import clear_screen
from board.strange_code import StrangeCode

from character.archer import (
    RangerArcher as RA,
    SniperArcher as SA
)
from character.warrior import (
    BarbarianWarrior as BW,
    FighterWarrior as FW
)
from character.wizard import (
    LightWizard as LW,
    DarkWizard as DW
)


class Game:
    """ Play the game """
    _SAVED = False
    _PLAYING = True

    __EXIT_COMMANDS: List[str] = [
        'QUIT',
        'EXIT',
        'END',
        'Q'
    ]

    AVAILABLE_CHARACTERS: Tuple[str] = (
        'sniperarcher',
        'rangerarcher',
        'lightwizard',
        'darkwizard',
        'fighterwarrior',
        'barbarianwarrior')

    _PLAYER_NOTICE: Tuple[str] = (
        "\t   ** Be Careful **",
        "\t ** Dragon is near you ** ",
    )

    _OBJECTS_NAME: Tuple[str] = (
        "player_loc",
        "dragon_loc",
        "dungeon_loc",
        "map_helper_loc"
    )

    _ENDING_MSG: str = "Have good time ..."
    _SAVE_MSG: str = "> Do you want to save your game? [yes/no]"
    _WINNER_MSG: str = "** You Scaped! Congratulation general. **"
    _PLAY_AGAIN_MSG: str = "Do you want to play again ? [yes/no] : "
    _HIT_WALL_MSG: str = "** Walls are hard! Don't run into them! **"
    _LOSER_MSG: str = "** OH NO! The dragon got you! Better luck next time! **"
    _DEBUG_MSG: str = "Do you want to play the game or test it ? [play/test] : " # noqa
    _PLAY_SAVED_GAME_MSG: str = '> Do you want to play of your save game? [yes/no] ' # noqa
    _DISTANCE_3_BLOCK: float = 4.26
    _DISTANCE_2_BLOCK: float = 2.82
    _DISTANCE_1_BLOCK: float = 1.41

    def intro(self) -> str:
        """ Game introduction """
        clear_screen()
        banner = pyfiglet.figlet_format("SAGE Team Game Studio")
        print(banner)
        sleep(3)
        print("Welcome to our Dungeon & Dragon Game.")
        sleep(1)
        dimension = input("What dimension is good for you? ")
        logging.info("the dimension was inserted.")
        print(f"Your Map will be {dimension} x {dimension}.")
        sleep(1)
        print("Thank you.")
        return dimension

    def character_intro(self) -> str:
        """ Characters introduction """
        clear_screen()
        print("What characters : {")
        self.show_messages(self.AVAILABLE_CHARACTERS)
        print(" } is good for you? ", end="")
        self.character = input().lower()
        logging.info("the character was inserted.")
        return self.character

    @property
    def character(self) -> str:
        """ Get character """
        return self.__character

    @character.setter
    def character(self, value: str) -> None:
        """

        Parameters
        ----------
        value: str :
            `value` must be string

        Returns
        -------
        Set character
        """

        while value.lower() not in self.AVAILABLE_CHARACTERS:
            clear_screen()
            print(f"> your value must be in {self.AVAILABLE_CHARACTERS}")
            value = input("> ")
        self.__character = value

    def create_character(self, character: str):
        """ assignment of character type"""
        if character == "sniperarcher":
            character_kind = SA
        elif character == "rangerarcher":
            character_kind = RA
        elif character == "lightwizard":
            character_kind = LW
        elif character == "darkwizard":
            character_kind = DW
        elif character == "barbarianwarrior":
            character_kind = BW
        elif character == "fighterwarrior":
            character_kind = FW
        else:
            print("Oops, something happened wrong.")
        return character_kind

    def is_debug_mode(self, _command: str) -> bool:
        """

        Parameters
        ----------
        _command: str :
            must chose (play or test)

        Returns
        -------
        Debug mode is on or off
        """
        return True if _command == "play" else False

    @property
    def _command(self) -> str:
        """Get _command """
        return self.__command

    @_command.setter
    def _command(self, value: str) -> None:
        """

        Parameters
        ----------
        value: str :
            `value` must be string

        Returns
        -------
        Set command
        """
        _correct_command = [
            "test",
            "debug",
            "d",
            "play",
            "p",
            "t",
            "yes",
            "yeah",
            "y",
            "no",
            "n"
        ]
        while value.lower() not in _correct_command:
            clear_screen()
            print("> your value must be in ")
            print(_correct_command)
            print(f"> but you enter <{value}>")
            value = input("> ")
        self.__command = value.lower()

    def get_help_play(
        self,
        player_loc: 'Location',
        player_valid_move: Tuple[str]
    ) -> Tuple[str]:
        """

        Parameters
        ----------
        player_loc: 'Location' :
            Get location of player
        player_valid_move: Tuple[str] :
            A tuple of workable moves

        Returns
        -------
        Some notices that player can see like : currently player location, ...
        """
        sentence_1 = f"-> You're currently in {player_loc}"
        sentence_2 = f"-> You can move {player_valid_move}"
        sentence_3 = f"-> Enter {self.__EXIT_COMMANDS} to quit."
        sentences = (sentence_1, sentence_2, sentence_3)
        return sentences

    def get_help_test(
        self,
        player_valid_move: Tuple[str],
        *args
    ) -> Tuple[str]:
        """

        Parameters
        ----------
        player_valid_move: Tuple[str] :
            A tuple of workable moves
        *args :
            A list of item locations

        Returns
        -------
        Some notices that tester can see and debug like:
        currently dragon location, ...
        """
        sentence_1 = f"-> You're currently in {args[0]}"
        sentence_2 = f"-> Dragon in {args[1]}"
        sentence_3 = f"-> Door in {args[2]}"
        sentence_4 = f"-> Map_Guide in {args[3]}"
        sentence_5 = f"-> You can move {player_valid_move}"
        sentence_6 = f"-> Enter {self.__EXIT_COMMANDS} to quit."
        sentences = (
            sentence_1, sentence_2,
            sentence_3, sentence_4,
            sentence_5, sentence_6
        )
        return sentences

    def show_messages(self, sentences: Tuple[str]) -> None:
        """

        Parameters
        ----------
        sentences: Tuple[str] :
            A tuple of messages

        Returns
        -------
        Iterate and show the messages
        """
        for sentence in sentences:
            print(sentence)

    def is_player_winner(
        self,
        player_loc: 'Location',
        dungeon_loc: 'Location'
    ) -> bool:
        """

        Parameters
        ----------
        player_loc: 'Location' :
            Get location of player
        dungeon_loc: 'Location' :
            Get location of dragon

        Returns
        -------
        Is player win the game? ...
        """
        return True if player_loc == dungeon_loc else False

    def is_player_loser(
        self,
        player_loc: 'Location',
        dragon_loc: 'Location'
    ) -> bool:
        """

        Parameters
        ----------
        player_loc: 'Location' :
            Get location of player
        dragon_loc: 'Location' :
            Get location of dragon

        Returns
        -------
        Is player lose the game? ...
        """
        return True if player_loc == dragon_loc else False

    def percent_calculating(self, percent: int) -> bool:
        """

        Parameters
        ----------
        percent: int :
            must be an integer number between [1, 10]

        Returns
        -------
        percent count for possibility
        """
        return True if randint(1, 10) <= percent else False

    def make_choice(self, distance: float) -> bool:
        """

        Parameters
        ----------
        distance: float :
            distance between dragon and player

        Returns
        -------
        is feeling of dragon on/off ? ...
        """
        is_feeling_on = False
        if distance <= self._DISTANCE_1_BLOCK:
            is_feeling_on = self.percent_calculating(9)  # 90%
        elif distance <= self._DISTANCE_3_BLOCK:
            is_feeling_on = self.percent_calculating(3)  # 30%
        return is_feeling_on

    def dragon_move(
        self,
        object_tools: Tuple["Location", "Location"]
    ) -> 'Location':
        """

        Parameters
        ----------
        object_tools: Tuple :
            A tuple of items

        Returns
        -------
        move dragon in game
        """
        player_loc, dragon_loc, dragon_valid_moves, flat = object_tools
        direction = flat.dragon_option_move(player_loc, dragon_loc)

        if direction in dragon_valid_moves:
            dragon_loc = dragon_loc.move(direction)
        if self.is_player_loser(player_loc, dragon_loc):
            print(self._LOSER_MSG)
            self._PLAYING = False
            self._command = input(self._PLAY_AGAIN_MSG).lower()
            self.play_again(self._command)
            print(self._ENDING_MSG)

        return dragon_loc

    def block_distance(self, distance: float, block: float) -> bool:
        """

        Parameters
        ----------
        distance: float :
            distance between items in game
        block: float :
            distance between block in game

        Returns
        -------
        `bool`
        """
        return True if distance <= block else False

    def show_warning_dragon_place(
        self,
        flat: "Map",
        objects_loc: Tuple,
        _distance: float
    ) -> None:
        """

        Parameters
        ----------
        flat: Map :
            an instance of class
        objects_loc: Tuple :
            location of player and dragon
        _distance: float :
            distance between block in game

        Returns
        -------
        Just show some messages
        """
        player_loc, dragon_loc = objects_loc[0:2]
        if self.block_distance(_distance, self._DISTANCE_1_BLOCK):
            self.show_messages(self._PLAYER_NOTICE)
            flat.show_board(player_loc, dragon_loc)
        elif self.block_distance(_distance, self._DISTANCE_2_BLOCK):
            self.show_messages(self._PLAYER_NOTICE)
            flat.show_board(player_loc)
        else:
            flat.show_board(player_loc)

    def is_map_helper_show(
        self,
        player_loc: "Location",
        map_helper_loc: "Location"
    ) -> bool:
        """

        Parameters
        ----------
        player_loc: "Location" :
            location of player
        map_helper_loc: "Location" :
            location of map_helper

        Returns
        -------
        deiced to show map_helper or not
        """
        return True if player_loc == map_helper_loc else False

    def show_map_helper(self, dungeon_loc: "Location") -> None:
        """
        Parameters
        ----------
        dungeon_loc : Location :
            location of door

        Returns
        -------
        show some helping massages
        """
        help_notice = StrangeCode()
        print()
        self.show_messages(
            help_notice.make_code(dungeon_loc)
        )
        logging.info("the map help code was made.")
        print()

    def is_save_on(self, command: str) -> bool:
        """
        related to game saving

        Parameters
        ----------
        command : str :
            included yes/no
        """
        return True if command == "yes" else False

    def write_locations(self, object_loc: Tuple["Location"]) -> None:
        """
        write some locations in a file

        Parameters
        ----------
        object_loc : Tuple[Location]
        """
        with open("tools_location.txt", "w") as save_file:
            for i in range(len(object_loc)):
                string = f"{self._OBJECTS_NAME[i]}: {object_loc[i]}\n"
                save_file.write(string)

    def is_save_file_exist(self) -> bool:
        """check is a special file exist. """
        return True if pathlib.Path("./tools_location.txt").is_file() else False # noqa

    def insert_saved_location(self) -> List['Location']:
        """
        open a file and get some locations
        """
        with open("./tools_location.txt", "r") as f:
            pattern = r'(\d), (\d)'
            objects_loc = [
                re.findall(pattern, loc,)[0]
                for loc in f
                ]
            objects_loc = [
                Location(int(loc[0]), int(loc[1]))
                for loc in objects_loc
                ]
            return objects_loc

    def start(self) -> None:
        """ start game ... """

        dimension = self.intro()
        character_type = self.character_intro()
        character = self.create_character(character_type)
        arash = character("Arash", 6) # noqa
        flat = Map(int(dimension))
        logging.info("the board was created.")
        if self.is_save_file_exist():
            self._command = input(self._PLAY_SAVED_GAME_MSG)
            if self._command == "yes":
                locs = self.insert_saved_location()
            else:
                locs = flat.get_locations(4)
        else:
            locs = flat.get_locations(4)
        player_loc, dragon_loc, dungeon_loc, map_helper_loc = locs
        logging.info("location of objects were inserted.")

        clear_screen()
        self._command = input(self._DEBUG_MSG).lower()
        self._PLAYING = True

        while self._PLAYING:
            clear_screen()

            player_valid_moves = flat.get_limitation(player_loc)
            dragon_valid_moves = flat.get_limitation(dragon_loc)
            _distance = flat.distance_player_dragon(player_loc, dragon_loc)
            objects_loc = (
                player_loc,
                dragon_loc,
                dungeon_loc,
                map_helper_loc
            )

            self.show_warning_dragon_place(flat, objects_loc, _distance)

            if self.is_map_helper_show(player_loc, map_helper_loc):
                self.show_map_helper(dungeon_loc)

            if self.is_debug_mode(self._command):
                self.show_messages(
                    self.get_help_play(
                        player_loc,
                        player_valid_moves
                    )
                )
            else:
                self.show_messages(self.get_help_test(
                    player_valid_moves,
                    player_loc,
                    dragon_loc,
                    dungeon_loc,
                    map_helper_loc
                )
                )

            command = input('> ').lower()

            if command.upper() in self.__EXIT_COMMANDS:
                print(self._SAVE_MSG)
                self._command = input('> ').lower()
                if self.is_save_on(self._command):
                    self.write_locations(objects_loc)
                print(self._ENDING_MSG)
                logging.info("player exited the game.")
                break
            elif command in player_valid_moves:
                player_loc = player_loc.move(command)
                logging.info(f"player moves to {command}")
                if self.is_player_loser(player_loc, dragon_loc):
                    print(self._LOSER_MSG)
                    logging.info("player lost.")
                    self._PLAYING = False
                    self._command = input(self._PLAY_AGAIN_MSG).lower()
                    self.play_again(self._command)
                    print(self._ENDING_MSG)
                    continue
                elif self.is_player_winner(player_loc, dungeon_loc):
                    print(self._WINNER_MSG)
                    logging.info("player won.")
                    self._PLAYING = False
                    self._command = input(self._PLAY_AGAIN_MSG).lower()
                    self.play_again(self._command)
                    print(self._ENDING_MSG)
                    continue
            else:
                print(self._HIT_WALL_MSG)
                print(
                    f' ** You enter <{command}>,you can chose {player_valid_moves} ** \n')  # noqa
                input('To continue please press enter..')
                clear_screen()
                continue
            object_tools = (
                player_loc,
                dragon_loc,
                dragon_valid_moves,
                flat
            )
            if self.make_choice(_distance):
                dragon_loc = self.dragon_move(object_tools)

    def play_again(self, _command: str) -> None:
        """

        Parameters
        ----------
        _command: str :
            must chose (yes or no)

        Returns
        -------
        If enter yes The game will be started again
        """
        if _command == "yes":
            logging.info("the game started again.")
            self.start()
