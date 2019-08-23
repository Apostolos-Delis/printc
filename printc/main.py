#!/usr/bin/env python3
# coding: utf8

"""
main.py
Date: 08-22-2019

Description: defines the printc class

Usage:
    >>> from printc import printc
    >>> printc.warning(str)
    >>> ...
"""

import sys

from .colorstring import ColorString
from .constants import COLOR_CODES, END
from .errors import PrintcFatalException


class printc:  # pylint: disable=invalid-name
    """
    the printc object defines the main printc method in its constructor, as
    well as supporting all the differnet
    """

    def __init__(self, output, *args, color="none", highlight="none",
                 bold=False, fade=False, blink=False, underline=False,
                 **kwargs):
        """
        print to stdout in color and/or other styles

        :param output: what the actual text will be
        :param color: color of the string
        :param highlight: highlight color of the string
        :param bold: boolean to make text bold or not
        :param fade: boolean to make text faded or not
        :param blink: boolean to make text blink or not
        :param underline: boolean to make text underlined or not

        Note: args and kwargs is for other
        """
        if color in COLOR_CODES.keys():
            color = COLOR_CODES[color]
        if highlight in COLOR_CODES.keys():
            highlight = COLOR_CODES[highlight]

        formatting = ColorString(
            self._get_repr(output),
            color=color,
            underline=underline,
            bold=bold,
            fade=fade,
            blink=blink,
            highlight=highlight,
        )
        print(formatting, *args, **kwargs)
        del self

    @staticmethod
    def _get_repr(arg) -> str:
        """
        :param arg: anything that will be printed with printc
        :return: the arguement's computer representation as a string
        """
        if isinstance(arg, str):
            return arg
        return repr(arg)

    @classmethod
    def warning(cls, output, *args, **kwargs):
        """
        Prints in yellow to stderr
        :param output: warning message
        :param end: what will be the termination byte of the print
                    statement, default is '\n'
        """
        orange = "\033[38;5;208m"
        formatting = f"{orange}{cls._get_repr(output)}{END}"
        cls(formatting, file=sys.stderr, *args, **kwargs)

    @classmethod
    def fatal(cls, output, interrupt=False):
        """
        Prints in red to stderr
        :param output: error message
        :param interrupt: stops the program if True
        """
        cls(cls._get_repr(output), color='red', bold=True, file=sys.stderr)
        if interrupt:
            raise PrintcFatalException("Program Terminated")


if __name__ == "__main__":
    pass
