from enum import Enum
"""
    Black        0;30     Dark Gray     1;30
    Red          0;31     Light Red     1;31
    Green        0;32     Light Green   1;32
    Brown/Orange 0;33     Yellow        1;33
    Blue         0;34     Light Blue    1;34
    Purple       0;35     Light Purple  1;35
    Cyan         0;36     Light Cyan    1;36
    Light Gray   0;37     White         1;37
    NC           0;37 <- (NC for No Color)
"""

colors = {
    "BLACK": "\033[0;30",
    "RED": "\033[0;31",
    "GREEN": "\033[0;31",
    "NC": "\033[39m"
}


class Colors(Enum):
    """
    Colors enum type
    """
    BLACK = "BLACK"
    RED = "RED"
    GREEN = "GREEN"
    BROWN = "BROWN"
    ORANGE = "ORANGE"
    BLUE = "BLUE"
    PURPLE = "PURPLE"
    CYAN = "CYAN"
    LIGHT_GRAY = "LIGHT GRAY"
    YELLOW = "YELLOW"
    WHITE = "WHITE"
    NC = "NC"
    DARK_GRAY = "DARK GRAY"
    LIGHT_RED = "LIGHT RED"
    LIGHT_GREEN = "LIGHT GREEN"
    LIGHT_BLUE = "LIGHT BLUE"
    LIGHT_PURPLE = "LIGHT PURPLE"
    LIGHT_CYAN = "LIGHT_CYAN"

    def __str__(self):
        """
        When printing:

        >> print(Color.RED),

        It will print: 'RED' instead of <Color.RED: 'RED'>
        If that output is desired, run the following:

        >> print(Color.RED.__repr())
        >> <Color.RED: 'RED'>

        """
        return str(str(self.__repr__()).split('\'')[1])


class Fonts(Enum):
    ITALIC = "ITALIC"
    BOLD = "BOLD"
    NORMAL = "NORMAL"


VALID_FONTS = {"italic", "bold", "normal"}
VALID_COLORS = {Colors.BLACK, Colors.RED, Colors.GREEN,
                Colors.BROWN, Colors.ORANGE, Colors.BLUE,
                Colors.PURPLE, Colors.CYAN, Colors.YELLOW,
                Colors.WHITE, Colors.LIGHT_GRAY,
                Colors.DARK_GRAY, Colors.LIGHT_GREEN,
                Colors.LIGHT_CYAN, Colors.LIGHT_BLUE,
                Colors.LIGHT_PURPLE, Colors.NC,
                Colors.LIGHT_RED}


if __name__ == "__main__":
    temp = Colors.BLUE.__repr__()
    print(Colors.BLUE.__repr__())
