import os
from cprint.cprint_errors import FontError
from cprint.cprint_errors import ColorError


def cprint(input: str, color: str, font="normal")->None:
    """
    :param input: the string that will be printed
    :param color: what color to print the string in
    :param font: selection from {
    :return:
    """

    raise FontError("""ERROR: Only available fonts:
    Normal,
    Bold,
    Italic,
    Strike-through,
    Underline,
    """)