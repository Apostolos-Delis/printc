

END = '\033[0m'


class Color:
    """
    color class used for
    """
    def __init__(self, name: str, color_id: str, highlight_id: str):
        self._name = name
        self._color = color_id
        self._highlight = highlight_id

    def __str__(self)->str:
        return self._name

    def __repr__(self)->str:
        return "Color Object: <" + self._name + ">"

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
LIGHT_GRAY = Color("LIGHT_GRAY", "37m", "47;")
DARK_GRAY = Color("DARK_GRAY", "90m", "100;")
LIGHT_RED = Color("LIGHT_RED", "91m", "101;")
LIGHT_GREEN = Color("LIGHT_GREEN", "92m", "102;")
LIGHT_YELLOW = Color("LIGHT_YELLOW", "93m", "103;")
LIGHT_BLUE = Color("LIGHT_BLUE", "94m", "104;")
LIGHT_MAGENTA = Color("LIGHT_MAGENTA", "95m", "105;")
LIGHT_CYAN = Color("LIGHT_CYAN", "96m", "106;")
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
