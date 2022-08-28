from enum import Enum
import os


def clear_screen():
    return os.system('cls') if os.name == 'nt' else 'clear'


class ConstantCharacter(Enum):

    NEW_LINE = '\n'
    PLAYER = 'X'
    EMPTY_LOC = '_'
    EMPTY = ''
