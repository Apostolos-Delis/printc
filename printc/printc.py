#!/usr/bin/env python
import sys
from constants import *
from colorstring import ColorString
"""
    Usage:
        >>> from printc import *
        >>> printc.warning(str)
        >>> ...
"""


class printc(object):

    def __init__(self, output,
                 color=NOCOLOR,
                 highlight=NOCOLOR,
                 bold=False,
                 faded=False,
                 blink=False,
                 underline=False, end='\n'):
        """
        print to stdout in color and/or other styles

        :param output: what the actual text will be
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
        :param end: just like the end parameter in print(), what
        string will be printed at the very end of the function call.
        Default is '\n'
        Example:
        >> printc("Hello World!", end="THE END")
        ...
        Hello World!THE END
        """

        formatting = ColorString(
            self._get_repr(output),
            color=color,
            underline=underline,
            bold=bold,
            faded=faded,
            blink=blink,
            highlight=highlight)

        print(formatting, file=sys.stdout, end=end)
        del self

    @staticmethod
    def _get_repr(arg)->str:
        """
        :param arg: anything that will be printed with printc
        :return: the arguement's computer representation as a string
        """
        if isinstance(arg, str):
            return arg
        return repr(arg)

    @classmethod
    def warning(cls, output, end='\n'):
        """
            Prints in yellow to stderr
            :param output: warning message
            :param end: what will be the termination byte of the print
            statement, default is '\n'
        """
        formatting = "\033[0;38;33m" + cls._get_repr(output) + END
        print(formatting, file=sys.stderr, end=end)

    @classmethod
    def fatal_msg(cls, output, interrupt=False):
        """
            Prints in red to stderr
            :param output: error message
            :param interrupt: stops the program if True

        """

        error_format = "\033[91m"
        print(error_format + cls._get_repr(output) + END,
              file=sys.stderr)
        if interrupt:
            print(error_format + "Fatal Error: Program stopped." +
                  END, file=sys.stderr)
            sys.exit(-1)


if __name__ == "__main__":

    # hello = {BLUE: {RED: GREEN}, BLACK: {RED: GREEN, BLACK: BLUE, BLUE: [1, 2, 3, 4]}}
    # printc({BLUE: {RED: GREEN}, BLACK: {RED: GREEN, BLACK: BLUE}, LIGHT_MAGENTA: [1, 2, 3, 4]},
    #        color=LIGHT_MAGENTA, highlight=CYAN, bold=True,
    #        underline=True, faded=False, blink=True)
    # printc.warning("THIS IS A WARNING:")
    # printc.fatal_msg("THIS IS FATAL", interrupt=True)
    # printc("Hello World!", color=LIGHT_MAGENTA, bold=True, underline=True, blink=False, faded=False)
    # printc("Hello World!", color=BLUE, bold=True, underline=True, blink=False, faded=False)
    # printc("sdfsdafasd", highlight=YELLOW)
    # idk = printc.warning("YOU SHOULDNT DO THIS BUT YOU CAN")
    # printc.fatal_msg("ERROR", interrupt=True)
    printc("HELLO", color=LIGHT_MAGENTA, highlight=BLUE)

