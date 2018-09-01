#!/usr/bin/env python
from constants import *
from printc_errors import ColorError, StyleError
import sys
import re


class ColorString(object):

    _valid_colors = {
        BLACK.__str__(): BLACK,
        RED.__str__(): RED,
        GREEN.__str__(): GREEN,
        YELLOW.__str__(): YELLOW,
        BLUE.__str__(): BLUE,
        PURPLE.__str__(): PURPLE,
        CYAN.__str__(): CYAN,
        LIGHT_GRAY.__str__(): LIGHT_GRAY,
        DARK_GRAY.__str__(): DARK_GRAY,
        LIGHT_RED.__str__(): LIGHT_RED,
        LIGHT_GREEN.__str__(): LIGHT_GREEN,
        LIGHT_YELLOW.__str__(): LIGHT_YELLOW,
        LIGHT_BLUE.__str__(): LIGHT_BLUE,
        LIGHT_MAGENTA.__str__(): LIGHT_MAGENTA,
        LIGHT_CYAN.__str__(): LIGHT_CYAN,
        WHITE.__str__(): WHITE,
        NOCOLOR.__str__(): NOCOLOR
    }

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
    NOCOLOR  (Default) |    NOCOLOR""".format(color.__repr__(), highlight.__repr__()))
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

        self._color = color
        self._highlight = highlight
        self._bold = bold
        self._faded = faded
        self._underline = underline
        self._blink = blink

        regex_pattern = re.compile("{{.+?}}")
        string = re.sub(regex_pattern, self._format_string, string)

        self._formatted_str = "\033["
        if not bold and not faded and not blink and not underline:
            self._formatted_str += styles["NO STYLE"]
        if bold:
            self._formatted_str += styles["BOLD"]
        if faded:
            self._formatted_str += styles["FADED"]
        if blink:
            self._formatted_str += styles["BLINKING"]
        if underline:
            self._formatted_str += styles["UNDERLINED"]

        self._formatted_str += highlight.highlight()
        self._formatted_str += color.color()
        self._formatted_str += string
        self._formatted_str += END

    def __str__(self)->str:
        return self._formatted_str

    def __repr__(self)->str:
        return self.__str__()

    def __add__(self, other):
        """
        :param other: must be either of type ColorString ot str
        :return: a str with all the formats of a ColorString (if Any)

        So if the ColorString was defined to be red, then for example:
        >> print(Colorstring("Hello", color=RED) + " World!")
        Hello World!

        Will print 'Hello' in Red and World! normally
        """
        if isinstance(other, str):
            return self._formatted_str + other
        elif isinstance(other, ColorString):
            return self._formatted_str + other._formatted_str
        else:
            try:

                raise TypeError(ColorString("TypeError: cannot add type: {0} to Colorstring"
                                            .format(type(other)), color=RED))
            except TypeError as error:
                print(error, file=sys.stderr)

    def _format_string(self, match_obj):
        """
        formats a string using the double bracket notation.
        For Example:

            >> "{{RED}}Hello {{BOLD, UNDERLINED}}World!"
            will make the 'Hello ' red and 'World!' will still be red
            since that wasn't changed, but it will also be bold and underlined

            If the user wants to define the highlight and the text both, or just wants
            a more robust format:

            >> "{{RED:C, BLUE:H}}Hello"
            will make the RED the text color and Blue will be the highlight color

            if you want to remove a style like bold, use the following syntax:

            >> "{{RED, UNDERLINED, BOLD}}Hello {{BOLD:F,BLUE}}World!"
            this will make 'Hello', Bold, underlined, and red, while 'World!'
            will now be Blue and underlined, but not bold

        :param match_obj: a re.matchobj type from the regular expressions library
        :return: the formatting necessary for colors/styles as a string that will be inserted
        back into the initial string that was called with re.sub()
        """
        formating = "\033["
        nochange = True
        object_match = match_obj.group(0).replace("{{", '')
        object_match = object_match.replace("}}", '')
        tokens = object_match.replace(' ', '').split(',')

        for token in tokens:
            token = token.upper()
            if ':' in token:
                token = token.split(':')

                if token[0] in ColorString._valid_colors.keys():
                    if token[1].upper() == 'C':
                        nochange = False
                        self._color = ColorString._valid_colors[token[0]]
                    elif token[1].upper() == 'H':
                        nochange = False
                        self._highlight = ColorString._valid_colors[token[0]]

                elif token[0] == "BOLD" and token[1] == 'F':
                    nochange = False
                    self._bold = False

                elif token[0] == "FADED" and token[1] == 'F':
                    nochange = False
                    self._faded = False

                elif token[0] == "UNDERLINED" and token[1] == 'F':
                    nochange = False
                    self._underline = False

                elif token[0] == "BLINKING" and token[1] == 'F':
                    nochange = False
                    self._blink = False

            elif token in ColorString._valid_colors.keys():
                nochange = False
                self._color = ColorString._valid_colors[token]

            elif token == "BOLD":
                nochange = False
                self._bold = True

            elif token == "FADED":
                nochange = False
                self._faded = True

            elif token == "UNDERLINED":
                nochange = False
                self._underline = True

            elif token == "BLINKING":
                nochange = False
                self._blink = True

        if not self._bold and not self._faded and not self._blink and not self._underline:
            formating += styles["NO STYLE"]
        if self._bold:
            formating += styles["BOLD"]
        if self._faded:
            formating += styles["FADED"]
        if self._blink:
            formating += styles["BLINKING"]
        if self._underline:
            formating += styles["UNDERLINED"]

        formating += self._highlight.highlight()
        formating += self._color.color()

        if nochange:
            return match_obj.group()
        else:
            return formating


if __name__ == "__main__":

    test = ColorString("ColorString Test", color=GREEN, underline=True,
                       bold=True, faded=False,
                       blink=False, highlight=BLACK)
    # print(test)
    import re

    # print(test)
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
    # print(re.sub("{{.+?}}", dashrepl, cstring))

