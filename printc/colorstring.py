#!/usr/bin/env python3
# coding: utf8

"""
colorstring.py
Date: 08-21-2019

Description: ColorString objects are used to parse strings and insert ANSI
escape codes in correct locations
"""

import re

if __name__ == "__main__":
    from code_gen import CodeGen
    from constants import END, COLORS
else:
    from .code_gen import CodeGen
    from .constants import END, COLORS


class ColorString:
    """
    Description: Used to parse strings and insert ANSI
    escape codes in correct locations
    """

    def __init__(self, string: str, color="none", highlight="none",
                 bold=False, fade=False, blink=False, underline=False):
        """
        Creates a string that will be printed with
        the following parameters:

        :param string: what the actual text of the string will be
        :param color: color of the string
        :param highlight: highlight color of the string

        Viable Colors:         | Viable Highlight Colors:
        ==================================================
            'black'            |    'black'
            'red'              |    'red'
            'green'            |    'green'
            'yellow'           |    'yellow'
            'blue'             |    'blue'
            'purple'           |    'purple'
            'cyan'             |    'cyan'
            'light gray'       |    'light'
            'dark gray'        |    'dark'
            'light red'        |    'light red'
            'light green'      |    'light green'
            'light yellow'     |    'light yellow'
            'light blue'       |    'light blue'
            'light magenta'    |    'light magenta'
            'light cyan'       |    'light cyan'
            'none   (default)  |    'none'

        :param bold: boolean to make text bold or not
        :param faded: boolean to make text faded or not
        :param blink: boolean to make text blink or not
        :param underline: boolean to make text underlined or not
        """
        assert isinstance(color, str), "color must be of type str"
        assert isinstance(highlight, str), "highlight must be of type str"
        assert isinstance(bold, bool), "bold must be of type bool"
        assert isinstance(fade, bool), "fade must be of type bool"
        assert isinstance(underline, bool), "underline must be of type bool"
        assert isinstance(blink, bool), "blink must be of type bool"

        self._code = CodeGen(color=color.lower(),
                             highlight=highlight.lower(),
                             bold=bold, underline=underline,
                             fade=fade, blink=blink)
        code = self._code.code()

        regex_pattern = re.compile("{{(.+?)}}")
        string = re.sub(regex_pattern, self._format_string, string)
        self._formatted_str = f"{code}{string}{END}"

    def __str__(self) -> str:
        return self._formatted_str

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, other):
        """
        :param other: must be either of type ColorString ot str
        :return: a str with all the formats of a ColorString (if Any)

        So if the ColorString was defined to be red, then for example:
        >> print(Colorstring("Hello", color='red') + " World!")
        Hello World!

        Will print 'Hello' in Red and World! normally
        """
        if isinstance(other, str):
            return ColorString(self._formatted_str + other)
        if isinstance(other, ColorString):
            return ColorString(self._formatted_str + other.__str__())
        raise TypeError(
            ColorString("Cannot add type: {type(other)} to Colorstring",
                        color='red', bold=True))

    def _format_string(self, match_obj):
        """
        formats a string using the double bracket notation.
        For Example:

            >> "{{RED}}Hello {{BOLD, UNDERLINE}}World!"
            will make the 'Hello ' red and 'World!' will still be red
            since that wasn't changed, but it will also be bold and underlined

            If the user wants to define the highlight and the text both, or
            just wants a more robust format:

            >> "{{RED:C, BLUE:H}}Hello"
            Hello will print with red text and a blue background

            if you want to remove a style like bold, use the following syntax:

            >> "{{RED, UNDERLINE, BOLD}}Hello {{BOLD:F,BLUE}}World!"
            this will make 'Hello', Bold, underlined, and red, while 'World!'
            will now be Blue and underlined, but not bold

        :param match_obj: a re.matchobj type from the regular expressions
                          library
        :return: the formatting necessary for colors/styles as a string that
                 will be inserted back into the initial string that was called
                 with re.sub()
        """
        tokens = match_obj.group(1).lower().replace(' ', '').split(',')

        styles = {"bold", "fade", "blink", "highlight"}

        for token in tokens:
            if ":" in token:
                token = token.split(":")

                if token[0] in COLORS.keys():
                    if token[1] == "c":
                        self._code.color = token[0]
                    elif token[1] == "h":
                        self._code.highlight = token[0]

                if token[0] in styles and token[1] == 'f':
                    setattr(self._code, token[0], False)

            elif token in COLORS.keys():
                self._code.color = token.lower()
            elif token in styles:
                setattr(self._code, token, True)

        if self._code.update:
            return self._code.code()
        return match_obj.group()


if __name__ == "__main__":
    pass
