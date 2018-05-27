import printc
import pytest


def test_color_printing():
    printc("BLACK", color=Colors.BLACK)
    printc("RED", color=Colors.RED)
    printc("GREEN", color=Colors.GREEN)
    printc("ORANGE", color=Colors.ORANGE)
    printc("BLUE", color=Colors.BLUE)
    printc("PURPLE", color=Colors.PURPLE)
    printc("CYAN", color=Colors.CYAN)
    printc("NC", color=Colors.NC)
    printc("LIGHT GRAY", Colors.LIGHT_GRAY)
    printc("DARK GRAY", color=Colors.DARK_GRAY)
    printc("LIGHT RED", color=Colors.LIGHT_RED)
    printc("LIGHT GREEN", color=Colors.LIGHT_GREEN)
    printc("LIGHT BLUE", color=Colors.LIGHT_BLUE)
    printc("LIGHT PURPLE", color=Colors.LIGHT_PURPLE)
    printc("LIGHT CYAN", color=Colors.LIGHT_CYAN)
    printc("WHITE", color=Colors.WHITE)
    return


if __name__ == "__main__":
    test_color_printing()
