#!/usr/bin/env python3
# coding: utf8

# pylint: disable: too-many-instance-attributes
# pylint: disable: too-many-arguments

"""
code_gen.py
Date: 08-21-2019

Description: Implementation of CodeGen class that generates ANSI codes
"""

from .constants import COLORS

START = "\033["
END = "\033[0m"


class CodeGen:
    """
    Description: generates an ansi code based on its member variables
    """

    def __init__(self, color="none", highlight="none", bold=False, 
                 underline=False, fade=False, blink=False):
        color = color.lower()
        highlight = highlight.lower()

        if color not in COLORS.keys():
            raise ValueError(f"'{color}', is not a valid color")
        if highlight not in COLORS.keys():
            raise ValueError(f"'{highlight}', is not a valid highlight")

        self._color = color
        self._highlight = highlight

        self._bold = bold
        self._underline = underline
        self._fade = fade
        self._blink = blink

        # Initialize the Ansi Code
        self._update = True
        self._code = self.code()

    def code(self) -> str:
        """
        Returns the Ansi Code generated from the member variables, if
        self._update is true, the ansi code gets reevaluated
        """
        if self._update:
            color = COLORS[self._color][0]
            highlight = COLORS[self._highlight][1]
            style = f"{self._bold}{self._blink}{self._underline}{self._fade}"
            self._code = f"{START}{style}{highlight}{color}{END}"
            self._update = False
        return self._code

    @property
    def color(self) -> str:
        """Returns the color (as a name not a code)"""
        return self._color

    @color.setter
    def color(self, new_color: str):
        if new_color not in COLORS.keys():
            raise ValueError(f"'{new_color}', is not a valid color")
        self._color = new_color
        self._update = True

    @property
    def highlight(self) -> str:
        """Returns the highlight (as a name not a code)"""
        return self._highlight

    @highlight.setter
    def highlight(self, new_highlight):
        if new_highlight not in COLORS.keys():
            raise ValueError(f"'{new_highlight}', is not a valid highlight")
        self._highlight = new_highlight
        self._update = True

    @property
    def fade(self) -> bool:
        """
        fade is a style that fades out text in terminal, it is not currently
        supported by all terminals however, so its usage should not be
        depended upon too heavily
        """
        return self._blink

    @fade.setter
    def fade(self, new_fade):
        self._fade = new_fade
        self._update = True

    @property
    def blink(self) -> bool:
        """
        blink is a style that causes text to flash on and off in terminal
        this is not supproted by all terminals or there is usually an
        option to disable this ANSI style
        """
        return self._blink

    @blink.setter
    def blink(self, new_blink):
        self._blink = new_blink
        self._update = True

    @property
    def underline(self) -> bool:
        """
        If True, underlines text
        """
        return self._underline

    @underline.setter
    def underline(self, new_underline):
        self._underline = new_underline
        self._update = True

    @property
    def bold(self) -> bool:
        """If true, bolds text"""
        return self._bold

    @bold.setter
    def bold(self, new_bold):
        self._bold = new_bold
        self._update = True


if __name__ == "__main__":
    pass
