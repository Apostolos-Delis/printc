import os


class FontError(Exception):
    """
    Error Raised when a font is used that is not in that standard errors
    """
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class ColorError(Exception):
    def __init__(self,):
        pass

    # TODO: NEED TO FINISH
