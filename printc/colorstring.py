from constants import *
import printc


class ColorString(object):

    def __init__(self, color=NOCOLOR,
                 background=NO_BACKGROUND,
                 italic=False,
                 bold=False,
                 faded=False,
                 blink=False,
                 underline=False):

        formated_str = "\033["
        formated_str += background


if __name__ == "__main__":
    print(printc.__version__)
    ColorString({"color": colors["RED"]})
