#!/usr/bin/env python
import sys
from constants import *
from colorstring import ColorString
"""
    Usage:
        >>> from printc import *
        >>> printc.info(str)
        >>> ...
"""


class printc(object):

    def __init__(self, output,
                 color=NOCOLOR,
                 background=NO_BACKGROUND,
                 bold=False,
                 faded=False,
                 blink=False,
                 underline=False, end='\n'):
        """
        print to stdout in color and/or other styles

        :param output: what the actual text will be
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
            background=background)

        import pprint
        # pprint.pprint(formatting)
        print(formatting, file=sys.stdout, end=end)
        del self

    @classmethod
    def _get_repr(cls, arg)->str:
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
        formatting = "\033[0;38;32m" + cls._get_repr(output) + END
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

# TODO Change Background to hightlight


if __name__ == "__main__":

    # hello = {BLUE: {RED: GREEN}, BLACK: {RED: GREEN, BLACK: BLUE_BG}, BLUE_BG: [1, 2, 3, 4]}
    # printc(hello, color=RED, background=BLUE_BG, bold=True)
    # printc({BLUE: {RED: GREEN}, BLACK: {RED: GREEN, BLACK: BLUE_BG}, BLUE_BG: [1, 2, 3, 4]},
    #        color=RED, background=LIGHT_RED_BG, bold=True,
    #        underline=True, faded=True, blink=True)
    printc.warning("THIS IS A WARNING:")
    printc.fatal_msg("THIS IS FATAL", interrupt=True)
