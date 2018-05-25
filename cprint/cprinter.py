import os
import sys
from cprint.cprint_errors import FontError
from cprint.cprint_errors import ColorError

VALID_FONTS = {"italic", "bold", "normal"}


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


    :param font: selection from {italic, bold, normal}
    """

    if font not in VALID_FONTS:
        raise FontError("""ERROR: Only available fonts:
    Normal,
    Bold,
    Italic,
    Strike-through,
    Underline, """)

    bash_print_script = "scripts/print_functions.sdh"

    print_command = bash_print_script + " "\
        + color.upper().replace(' ', '') \
        + " " + output_string

    try:
        if os.path.isfile(bash_print_script):
            os.system(print_command)
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("""It appears that the bash script: {0} was
not found, make sure to have installed cprint 
properly with all its files and to not have 
modified the scripts in a way that would corrupt the library.
""".format(bash_print_script))
        sys.exit(-1)


if __name__ == "__main__":
    cprint("Hello World", color="Blue")
    cprint("Hello World", color="cyan")
