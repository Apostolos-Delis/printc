import os
import string
from cprint.cprint_errors import FontError
from cprint.cprint_errors import ColorError

VALID_FONTS = {"italic", "bold", "normal"}


def cprint(output_string: str, color="NC", font="normal")->None:
    """
    :param output_string: the string that will be printed
    :param color: what color to print the string in
    :param font: selection from {italic, bold, normal}
    :return:
    """

    if font not in VALID_FONTS:
        raise FontError("""ERROR: Only available fonts:
    Normal,
    Bold,
    Italic,
    Strike-through,
    Underline, """)

    print_command = "scripts/temp.sh " + color.upper().replace(' ', '') + " " + output_string
    os.system(print_command)


if __name__ == "__main__":
    cprint("Hello World", color="Blue")
