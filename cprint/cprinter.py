import os
import sys
from cprint_errors import FontError, ColorError

VALID_FONTS = {"italic", "bold", "normal"}
VALID_COLORS = {"black", "red", "green", "brown", "orange",
                "blue", "purple", "cyan", "light gray",
                "dark gray", "light, red", "light green",
                "yellow", "light blue", "light purple",
                "light cyan", "white", "nc"}


def cprint(output_string: str, color="NC", font="normal")->None:
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
        if color.lower() not in VALID_COLORS:
            raise ColorError("""\nERROR: '{}' not a valid color
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

    print_command = bash_print_script + " "\
        + color.upper().replace(' ', '') \
        + " " + output_string

    try:
        if os.path.isfile(bash_print_script):
            os.system(print_command)
        else:
            raise FileNotFoundError("""\nERROR: {0} was
not found, make sure to have installed cprint 
properly with all its files and to not have 
modified the scripts in a way that would corrupt the library.
""".format(bash_print_script))

    except FileNotFoundError as errno:
        print(errno, file=sys.stderr)
        sys.exit(-1)


if __name__ == "__main__":
    cprint("Hello World", color="Blue")
    cprint("Hello World", color="cyan")
    cprint("Hello World", color="purple")
    cprint("Hello World", color="green")
    cprint("Hello World", color="yellow")
    cprint("Hello World", color="orange")
    cprint("Hello World", color="red")
    cprint("Hello World", color="light gray")
    # cprint("Hello World", color="light dick")
    cprint("Hello World")
