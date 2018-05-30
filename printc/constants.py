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

END = '\033[0m'


class Color:
    def __init__(self, name: str, color_id: str, highlight_id: str):
        self._name = name
        self._color = color_id
        self._highlight = highlight_id

    def __str__(self)->str:
        return self._name

    def __repr__(self)->str:
        return self.__str__()

    def color(self)->str:
        return self._color

    def highlight(self)->str:
        return self._highlight


BLACK = Color("BLACK", "30m", "40;")
RED = Color("RED", "31m", "41;")
GREEN = Color("GREEN", "32m", "42;")
YELLOW = Color("YELLOW", "33m", "43;")
BLUE = Color("BLUE", "34m", "44;")
PURPLE = Color("PURPLE", "35m", "45;")
CYAN = Color("CYAN", "36m", "46;")
LIGHT_GRAY = Color("LIGHT GRAY", "37m", "47;")
DARK_GRAY = Color("DARK GRAY", "90m", "100;")
LIGHT_RED = Color("LIGHT RED", "91m", "101;")
LIGHT_GREEN = Color("LIGHT GREEN", "92m", "102;")
LIGHT_YELLOW = Color("LIGHT YELLOW", "93m", "103;")
LIGHT_BLUE = Color("LIGHT BLUE", "94m", "104;")
LIGHT_MAGENTA = Color("LIGHT MAGENTA", "95m", "105;")
LIGHT_CYAN = Color("LIGHT CYAN", "96m", "106;")
WHITE = Color("WHITE", "97m", "107;")
NOCOLOR = Color("NOCOLOR", "39m", "49;")

styles = {
    "NO STYLE": "0;",
    "BOLD": "1;",
    "FADED": "2;",
    "UNDERLINED": "4;",
    "BLINKING": "5;",
}

if __name__ == "__main__":
    pass
