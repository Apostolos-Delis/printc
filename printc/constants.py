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
    "RED": "\033[0;31",
    "GREEN": "\033[0;31",
    "NOCOLOR": "\033[39m",
}

BLACK = colors["BLACK"]
NOCOLOR = colors["NOCOLOR"]

backgrounds = {
    "BLACK": "40;",
    "RED": "\033[0;31",
    "GREEN": "",
    "NOCOLOR": "49;",
}

NO_BACKGROUND = backgrounds["NOCOLOR"]

if __name__ == "__main__":
    pass
