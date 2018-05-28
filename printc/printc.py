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

        print(formatting, file=sys.stdout)
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

    # @classmethod
    # def ok(cls, arg):
    #     """
    #         Prints in blue to stdout
    #     """
    #     print(cprint.colors['OK'] + cls._get_repr(arg) + cprint.colors['ENDC'],
    #           file=sys.stdout)
    #
    # @classmethod
    # def info(cls, arg):
    #     """
    #         Prints in green to stdout
    #     """
    #     print(cprint.colors['INFO'] + cls._get_repr(arg) + cprint.colors['ENDC'],
    #           file=sys.stdout)

    @classmethod
    def warn(cls, arg):
        """
            Prints in yellow to strerr
        """
        print(printc.colors['WARNING'] + cls._get_repr(arg) + printc.colors['ENDC'],
              file=sys.stderr)
    #
    # @classmethod
    # def err(cls, arg, interrupt=False):
    #     """
    #         Prints in brown to stderr
    #         interrupt=True: stops the program
    #     """
    #     print(cprint.colors['ERR'] + cls._get_repr(arg) + cprint.colors['ENDC'],
    #           file=sys.stderr)
    #     if interrupt:
    #         print(cprint.colors['ERR'] + "Error: Program stopped." +
    #               cprint.colors['ENDC'],
    #               file=sys.stderr)
    #         exit(1)
    #
    # @classmethod
    # def fatal(cls, arg, interrupt=False):
    #     """
    #         Prints in red to stderr
    #         interrupt=True: stops the program
    #     """
    #     print(cprint.colors['FATAL'] + cls._get_repr(arg) + cprint.colors['ENDC'],
    #           file=sys.stderr)
    #     if interrupt:
    #         print(cprint.colors['FATAL'] + "Fatal error: Program stopped." +
    #               cprint.colors['ENDC'],
    #               file=sys.stderr)
    #         exit(1)


if __name__ == "__main__":
    printc(123, color=RED, background=BLUE_BG, bold=True,
           underline=True, faded=True, blink=True)
