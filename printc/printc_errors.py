#!/usr/bin/env python
import printc
from constants import *


class ExceptionC(Exception):
    """
    Inherit from this exception so that color will be
    red for more vivid error messages

    Example:

    class NewException(ExceptionC):
        def __init__(self, errno):
            super().__init__(errno)

    so now when you raise a NewException:

    >> try:
    >>     raise NewException(message)
    >> except NewException as e:
    >>     ...

    will output:
    >> NewException: message
    in red
    """
    def __init__(self, error):
        formating = "\033[1;49;31m"
        message = formating +\
            self.__class__.__name__ + ": " + error + END
        print(message)
        super().__init__(message)


class FontError(ExceptionC):
    """
    Error Raised when a font is used that is not in that standard fonts
    """
    def __init__(self, message):
        super().__init__(message)


class ColorError(ExceptionC):
    """
    Error Raised when a color is used that is not in that standard colors
    """
    def __init__(self, message):
        super().__init__(message)


if __name__ == "__main__":
    # print("\033[0;41;4;2;30m hello world")
    try:
        raise ColorError("there was an error with color!")

    except ColorError as errno:
        # print("ERROR: {}".format(errno))
        print("wut")
