
class FontError(Exception):
    """
    Error Raised when a font is used that is not in that standard fonts
    """
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class ColorError(Exception):
    """
    Error Raised when a color is used that is not in that standard colors
    """
    def __init__(self, message):

        super().__init__(message)

