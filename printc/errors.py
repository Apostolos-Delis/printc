#!/usr/bin/env python3
# coding: utf8

from .colorstring import ColorString


class ExceptionC(Exception):
    """
    Inherit from this exception so that color will be
    red for more vivid error messages

    Example:

    class NewException(ExceptionC):
        pass

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
        output = f"{self.__class__.__name__}: {error}"
        message = ColorString(output, color="red", bold=True)
        super().__init__(message)


class PrintcFatalException(ExceptionC):
    """
    Error raised when printc.fatal() is called with interrupt=True
    """
    pass  # pylint: disable=unnecessary-pass


if __name__ == "__main__":
    pass
