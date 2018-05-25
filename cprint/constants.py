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


class Colors(Enum):
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


VALID_FONTS = {"italic", "bold", "normal"}
VALID_COLORS = {"black", "red", "green", "brown", "orange",
                "blue", "purple", "cyan", "light gray",
                "dark gray", "light red", "light green",
                "yellow", "light blue", "light purple",
                "light cyan", "white", "nc"}

