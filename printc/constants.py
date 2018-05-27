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

END = '\033[0m'

colors = {
    "BLACK": "30m",
    "RED": "31m",
    "GREEN": "32m",
    "YELLOW": "33m",
    "BLUE": "34m",
    "PURPLE": "35m",
    "CYAN": "36m",
    "LIGHT GRAY": "37m",
    "DARK GRAY": "90m",
    "LIGHT RED": "91m",
    "LIGHT GREEN": "92m",
    "LIGHT YELLOW": "93m",
    "LIGHT BLUE": "94m",
    "LIGHT MAGENTA": "95m",
    "LIGHT CYAN": "96m",
    "WHITE": "97m",
    "NOCOLOR": "39m",
}

BLACK = colors["BLACK"]
RED = colors["RED"]
GREEN = colors["GREEN"]
YELLOW = colors["YELLOW"]
BLUE = colors["BLUE"]
PURPLE = colors["PURPLE"]
CYAN = colors["CYAN"]
LIGHT_GRAY = colors["LIGHT GRAY"]
DARK_GRAY = colors["DARK GRAY"]
LIGHT_RED = colors["LIGHT RED"]
LIGHT_GREEN = colors["LIGHT GREEN"]
LIGHT_YELLOW = colors["LIGHT YELLOW"]
LIGHT_BLUE = colors["LIGHT BLUE"]
LIGHT_MAGENTA = colors["LIGHT MAGENTA"]
LIGHT_CYAN = colors["LIGHT CYAN"]
NOCOLOR = colors["NOCOLOR"]

backgrounds = {
    "BLACK": "40;",
    "RED": "41;",
    "GREEN": "42;",
    "YELLOW": "43;",
    "BLUE": "44;",
    "PURPLE": "45;",
    "CYAN": "46;",
    "LIGHT GRAY": "47;",
    "DARK GRAY": "100;",
    "LIGHT RED": "101;",
    "LIGHT GREEN": "102;",
    "LIGHT YELLOW": "103;",
    "LIGHT BLUE": "104;",
    "LIGHT MAGENTA": "105;",
    "LIGHT CYAN": "106;",
    "WHITE": "107;",
    "NOCOLOR": "49;",
}

BLACK_BG = backgrounds["BLACK"]
RED_BG = backgrounds["RED"]
GREEN_BG = backgrounds["GREEN"]
YELLOW_BG = backgrounds["YELLOW"]
BLUE_BG = backgrounds["BLUE"]
PURPLE_BG = backgrounds["PURPLE"]
CYAN_BG = backgrounds["CYAN"]
LIGHT_GRAY_BG = backgrounds["LIGHT GRAY"]
DARK_GRAY_BG = backgrounds["DARK GRAY"]
LIGHT_RED_BG = backgrounds["LIGHT RED"]
LIGHT_GREEN_BG = backgrounds["LIGHT GREEN"]
LIGHT_YELLOW_BG = backgrounds["LIGHT YELLOW"]
LIGHT_BLUE_BG = backgrounds["LIGHT BLUE"]
LIGHT_MAGENTA_BG = backgrounds["LIGHT MAGENTA"]
LIGHT_CYAN_BG = backgrounds["LIGHT CYAN"]
NOCOLOR_BG = backgrounds["NOCOLOR"]

NO_BACKGROUND = backgrounds["NOCOLOR"]

if __name__ == "__main__":
    pass
