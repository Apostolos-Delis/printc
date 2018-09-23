#!/usr/bin/env python3
# coding: utf8


class ExceptionC(Exception):
    """
    Inherit from this exception so that color will be
    red for more vivid error messages

    Example:

    class NewException(ExceptionC):
        def __init__(self, errno):
            super().__init__(errno)

    so now when you raise a NewException:

    Usage:
    >> try:
    >>     raise NewException(message)
    >> except NewException as e:
    >>     print(e)

    will output:
    >> NewException: message
    in red
    """
    def __init__(self, error):
        formating = "\033[31m"
        message = formating +\
            self.__class__.__name__ + ": " + error + END
        super().__init__(message)


class StyleError(ExceptionC):
    """
    Error Raised when a Style is used that is not in that standard fonts
    Only Styles allowed are:
    NO STYLE
    BOLD
    FADED
    UNDERLINED
    BLINKING
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
    try:
        raise ColorError("there was an error with color!")

    except ColorError as errno:
        print(errno)
        try:
            raise StyleError("Wrong Style!")
        except StyleError as errno:
            print(errno)
