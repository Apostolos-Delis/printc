#!/usr/bin/env python
from constants import *
import printc


class ColorString(object):

    def __init__(self, string: str,
                 color=NOCOLOR,
                 background=NO_BACKGROUND,
                 bold=False,
                 faded=False,
                 blink=False,
                 underline=False):
        """
        Creates a string that will be printed with
        the following parameters:

        :param string: what the actual text of the string will be
        :param color: color of the string
        :param background: background color of the string

        Viable Colors:         | Viable Background Colors:
        ==================================================
            BLACK              |    BLACK_BG
            RED                |    RED_BG
            GREEN              |    GREEN_BG
            YELLOW             |    YELLOW_BG
            BLUE               |    BLUE_BG
            PURPLE             |    PURPLE_BG
            CYAN               |    CYAN_BG
            LIGHT_GRAY         |    LIGHT_GRAY_BG
            DARK_GRAY          |    DARK_GRAY_BG
            LIGHT_RED          |    LIGHT_RED_BG
            LIGHT_GREEN        |    LIGHT_GREEN_BG
            LIGHT_YELLOW       |    LIGHT_YELLOW_BG
            LIGHT_BLUE         |    LIGHT_BLUE_BG
            LIGHT_MAGENTA      |    LIGHT_MAGENTA_BG
            LIGHT_CYAN         |    LIGHT_CYAN_BG
            NOCOLOR  (Default) |    NO_BACKGROUND

        :param bold: boolean to make text bold or not
        :param faded: boolean to make text faded or not
        :param blink: boolean to make text blink or not
        :param underline: boolean to make text underlined or not
        """

        self.formatted_str = "\033["
        if not bold and not faded and not blink and not underline:
            self.formatted_str += styles["NO STYLE"]
        if bold:
            self.formatted_str += styles["BOLD"]
        if faded:
            self.formatted_str += styles["FADED"]
        if blink:
            self.formatted_str += styles["BLINKING"]
        if underline:
            self.formatted_str += styles["UNDERLINED"]

        self.formatted_str += background
        self.formatted_str += color
        self.formatted_str += string
        self.formatted_str += END

    def __str__(self):
        return self.formatted_str

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    test = ColorString("ColorString Test", color=BLUE, underline=True,
                       bold=True, faded=False,
                       blink=True, background=RED_BG)
    print(test)
