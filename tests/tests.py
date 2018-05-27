import src
import pytest


def test_color_printing():
    src("BLACK", color=Colors.BLACK)
    src("RED", color=Colors.RED)
    src("GREEN", color=Colors.GREEN)
    src("ORANGE", color=Colors.ORANGE)
    src("BLUE", color=Colors.BLUE)
    src("PURPLE", color=Colors.PURPLE)
    src("CYAN", color=Colors.CYAN)
    src("NC", color=Colors.NC)
    src("LIGHT GRAY", Colors.LIGHT_GRAY)
    src("DARK GRAY", color=Colors.DARK_GRAY)
    src("LIGHT RED", color=Colors.LIGHT_RED)
    src("LIGHT GREEN", color=Colors.LIGHT_GREEN)
    src("LIGHT BLUE", color=Colors.LIGHT_BLUE)
    src("LIGHT PURPLE", color=Colors.LIGHT_PURPLE)
    src("LIGHT CYAN", color=Colors.LIGHT_CYAN)
    src("WHITE", color=Colors.WHITE)
    return


if __name__ == "__main__":
    test_color_printing()
