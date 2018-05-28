#!/usr/bin/env python
import sys
from printc_errors import *
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

        formatting = ColorString(self._get_repr(output), color=color, underline=underline,
                                 bold=bold, faded=faded,
                                 blink=blink, background=background)
        print(formatting, file=sys.stdout)
        del self

    @classmethod
    def _get_repr(cls, arg):
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

# def cprint(output_string: str, color=Colors.NC, font="normal")->None:
#     """
#     :param output_string: the string that will be printed
#     :param color: what color to print the string in
#
#     Available colors and their bash values:
#     Black        0;30     Dark Gray     1;30
#     Red          0;31     Light Red     1;31
#     Green        0;32     Light Green   1;32
#     Brown/Orange 0;33     Yellow        1;33
#     Blue         0;34     Light Blue    1;34
#     Purple       0;35     Light Purple  1;35
#     Cyan         0;36     Light Cyan    1;36
#     Light Gray   0;37     White         1;37
#     NC           0;37 <- (NC for No Color)
#
#     :param font: selection from {italic, bold, normal}
#
#     """
#     try:
#         if font.lower()not in VALID_FONTS:
#             raise FontError("""\nERROR: '{}' not a valid font
# Only available fonts:
#     Normal,
#     Bold,
#     Italic,
#     Strike-through,
#     Underline, """)
#
#     except FontError as errno:
#         print(errno, file=sys.stderr)
#         sys.exit(-1)
#
#     try:
#         if color not in VALID_COLORS or not isinstance(color, Colors):
#             raise ColorError("""\nColorError: '{}' not a valid color
# Only available colors:
#     Black            Dark Gray
#     Red              Light Red
#     Green            Light Green
#     Brown/Orange     Yellow
#     Blue             Light Blue
#     Purple           Light Purple
#     Cyan             Light Cyan
#     Light Gray       White
#     None)
# """.format(color))
#
#     except ColorError as errno:
#         print(errno, file=sys.stderr)
#         sys.exit(-1)
#
#     bash_print_script = "scripts/print_functions.sh"
#
#     print_command = bash_print_script + " \'"\
#         + color.__str__() \
#         + "\' " + output_string
#
#     try:
#         if os.path.isfile(bash_print_script):
#             os.system(print_command)
#         else:
#             raise FileNotFoundError("""\nFileNotFoundError: {0} was
# not found, make sure to have installed printc
# properly with all its files and to not have
# modified the scripts in a way that would corrupt the library.
# """.format(bash_print_script))
#
#     except FileNotFoundError as errno:
#         print(errno, file=sys.stderr)
#         sys.exit(-1)


if __name__ == "__main__":
    printc(123, color=RED)
