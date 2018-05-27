import os
import sys
# from cprint_errors import *
from cprint_errors import FontError, ColorError
from constants import VALID_COLORS, VALID_FONTS, Colors


def cprint(output_string: str, color=Colors.NC, font="normal")->None:
    """
    :param output_string: the string that will be printed
    :param color: what color to print the string in

    Available colors and their bash values:
    Black        0;30     Dark Gray     1;30
    Red          0;31     Light Red     1;31
    Green        0;32     Light Green   1;32
    Brown/Orange 0;33     Yellow        1;33
    Blue         0;34     Light Blue    1;34
    Purple       0;35     Light Purple  1;35
    Cyan         0;36     Light Cyan    1;36
    Light Gray   0;37     White         1;37
    NC           0;37 <- (NC for No Color)

    :param font: selection from {italic, bold, normal}

    """
    try:
        if font.lower()not in VALID_FONTS:
            raise FontError("""\nERROR: '{}' not a valid font
Only available fonts:
    Normal,
    Bold,
    Italic,
    Strike-through,
    Underline, """)

    except FontError as errno:
        print(errno, file=sys.stderr)
        sys.exit(-1)

    try:
        if color not in VALID_COLORS or not isinstance(color, Colors):
            raise ColorError("""\nColorError: '{}' not a valid color
Only available colors:
    Black            Dark Gray     
    Red              Light Red     
    Green            Light Green   
    Brown/Orange     Yellow        
    Blue             Light Blue    
    Purple           Light Purple  
    Cyan             Light Cyan    
    Light Gray       White   
    NC (no color)
""".format(color))

    except ColorError as errno:
        print(errno, file=sys.stderr)
        sys.exit(-1)

    bash_print_script = "scripts/print_functions.sh"

    print_command = bash_print_script + " \'"\
        + color.__str__() \
        + "\' " + output_string

    try:
        if os.path.isfile(bash_print_script):
            os.system(print_command)
        else:
            raise FileNotFoundError("""\nFileNotFoundError: {0} was
not found, make sure to have installed cprint 
properly with all its files and to not have 
modified the scripts in a way that would corrupt the library.
""".format(bash_print_script))

    except FileNotFoundError as errno:
        print(errno, file=sys.stderr)
        sys.exit(-1)


if __name__ == "__main__":

    cprint("BLACK", color=Colors.BLACK)
    cprint("RED", color=Colors.RED)
    cprint("GREEN", color=Colors.GREEN)
    cprint("ORANGE", color=Colors.ORANGE)
    cprint("BLUE", color=Colors.BLUE)
    cprint("PURPLE", color=Colors.PURPLE)
    cprint("CYAN", color=Colors.CYAN)
    cprint("NC", color=Colors.NC)
    cprint("LIGHT GRAY", Colors.LIGHT_GRAY)
    cprint("DARK GRAY", color=Colors.DARK_GRAY)
    cprint("LIGHT RED", color=Colors.LIGHT_RED)
    cprint("LIGHT GREEN", color=Colors.LIGHT_GREEN)
    cprint("LIGHT BLUE", color=Colors.LIGHT_BLUE)
    cprint("LIGHT PURPLE", color=Colors.LIGHT_PURPLE)
    cprint("LIGHT CYAN", color=Colors.LIGHT_CYAN)
    cprint("WHITE", color=Colors.WHITE)
