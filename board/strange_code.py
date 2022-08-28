
from typing import Tuple


class StrangeCode:
    """ """

    morse_code: dict = dict()

    def __init__(self) -> None:

        self.morse_code.update({
            "0": "-----", "1": "----•",
            "2": "---••", "3": "--•••",
            "4": "-••••", "5": "•••••",
            "6": "•----", "7": "••---",
            "8": "•••--", "9": "••••-",
        })

    def pass_code_maker(self, axis: int) -> str:
        """

        Parameters
        ----------
        axis: int :
            Get Axis like:
            Axis(3, 2)

        Returns
        -------
        turn Axis location to morse code
        """
        axis = str(axis)
        code_msg: str = ""
        for num in axis:
            code_msg += self.morse_code[num]
        return code_msg

    def make_code(self, value) -> Tuple[str]:
        """

        Parameters
        ----------
        value :
            Get Axis like:
            Axis(3, 2)

        Returns
        -------
        A message with a morse code
        """
        x_axis = value.X
        y_axis = value.Y
        msg = "\t\t ***"
        msg_1 = ">>>> If you understand "
        msg_2 = ">>>> the secret of the position "
        msg_3 = ">>>> Maybe you can find your destiny :) "
        msg_4 = f'>>>> {self.pass_code_maker(x_axis)} '
        msg_5 = f'>>>> {self.pass_code_maker(y_axis)} '
        return (msg, msg_1, msg_2, msg_4, msg_5, msg_3, msg)
