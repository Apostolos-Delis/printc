#!/usr/bin/env python
from constants import *
from printc_errors import ColorError, StyleError
import sys


class ColorString(object):

    def __init__(self, string: str,
                 color=NOCOLOR,
                 highlight=NOCOLOR,
                 bold=False,
                 faded=False,
                 blink=False,
                 underline=False):
        """
        Creates a string that will be printed with
        the following parameters:

        :param string: what the actual text of the string will be
        :param color: color of the string
        :param highlight: highlight color of the string

        Viable Colors:         | Viable Highlight Colors:
        ==================================================
            BLACK              |    BLACK
            RED                |    RED
            GREEN              |    GREEN
            YELLOW             |    YELLOW
            BLUE               |    BLUE
            PURPLE             |    PURPLE
            CYAN               |    CYAN
            LIGHT_GRAY         |    LIGHT
            DARK_GRAY          |    DARK
            LIGHT_RED          |    LIGHT_RED
            LIGHT_GREEN        |    LIGHT_GREEN
            LIGHT_YELLOW       |    LIGHT_YELLOW
            LIGHT_BLUE         |    LIGHT_BLUE
            LIGHT_MAGENTA      |    LIGHT_MAGENTA
            LIGHT_CYAN         |    LIGHT_CYAN
            NOCOLOR  (Default) |    NOCOLOR

        :param bold: boolean to make text bold or not
        :param faded: boolean to make text faded or not
        :param blink: boolean to make text blink or not
        :param underline: boolean to make text underlined or not
        """
        try:
            if not isinstance(color, Color):
                raise ColorError("""The color: {0} and/or the highlight: {1} that you have
selected is not a valid color.

Viable Colors:         | Viable Highlight Colors:
==================================================
    BLACK              |    BLACK
    RED                |    RED
    GREEN              |    GREEN
    YELLOW             |    YELLOW
    BLUE               |    BLUE
    PURPLE             |    PURPLE
    CYAN               |    CYAN
    LIGHT_GRAY         |    LIGHT
    DARK_GRAY          |    DARK
    LIGHT_RED          |    LIGHT_RED
    LIGHT_GREEN        |    LIGHT_GREEN
    LIGHT_YELLOW       |    LIGHT_YELLOW
    LIGHT_BLUE         |    LIGHT_BLUE
    LIGHT_MAGENTA      |    LIGHT_MAGENTA
    LIGHT_CYAN         |    LIGHT_CYAN
    NOCOLOR  (Default) |    NOCOLOR""".format(color.__str__(), highlight.__str__()))
        except ColorError as error:
            print(error, file=sys.stderr)
            sys.exit(-1)

        try:
            if not isinstance(bold, bool):
                raise StyleError("the parameter 'bold' must be of type 'bool'")
            if not isinstance(faded, bool):
                raise StyleError("the parameter 'faded' must be of type 'bool'")
            if not isinstance(blink, bool):
                raise StyleError("the parameter 'blink' must be of type 'bool'")
            if not isinstance(underline, bool):
                raise StyleError("the parameter 'underline' must be of type 'bool'")
        except StyleError as error:
            print(error, file=sys.stderr)
            sys.exit(-1)

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

        self.formatted_str += highlight.highlight()
        self.formatted_str += color.color()
        self.formatted_str += string
        self.formatted_str += END

    def __str__(self)->str:
        return self.formatted_str

    def __repr__(self)->str:
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, str):
            return self.formatted_str + other
        elif isinstance(other, ColorString):
            return self.formatted_str + other.formatted_str
        else:
            try:

                raise TypeError(ColorString("TypeError: cannot add type: {0} to Colorstring"
                                            .format(type(other)), color=RED))
            except TypeError as error:
                print(error, file=sys.stderr)


if __name__ == "__main__":

    test = ColorString("ColorString Test", color=GREEN, underline=True,
                       bold=True, faded=False,
                       blink=False, highlight=BLACK)
    print(test)
    # import re
    #
    # cstring = "{{RED}}HELLO WORLD! {{BLUE}}I REALLY LIKE {{BOLD,}}THIS"
    # prog = re.compile("{{.+?}}")
    # m = re.findall(prog, cstring)
    # print(m)
    # n = re.search('.+' + m[1], cstring)
    #
    # temp = re.sub("{{RED}}", "\033[0;31m", cstring)
    # temp = re.sub("{{BLUE}}", "\033[0;34m", temp)
    # temp = re.sub("{{BOLD}}", "\033[1;34m", temp)
    # temp += END
    # print(temp)

