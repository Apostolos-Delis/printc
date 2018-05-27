import cprint
import pytest


def test_color_printing():
    cprint("BLACK", color=Colors.BLACK)
    cprint("RED", color=Colors.RED)
    cprint("GREEN", color=Colors.GREEN)
    cprint("ORANGE", color=Colors.ORANGE)
    cprint("BLUE", color=Colors.BLUE)
    cprint("PURPLE", color=Colors.PURPLE)
    cprint("CYAN", color=Colors.CYAN)
    cprint("NC", color=Colors.NC)
    cprint("LIGHT GRAY", Colors.LIGHT_GRAY)
    cprint("DARK GRAY", color=Colors.DARK_GRAY)
    cprint("LIGHT RED", color=Colors.LIGHT_RED)
    cprint("LIGHT GREEN", color=Colors.LIGHT_GREEN)
    cprint("LIGHT BLUE", color=Colors.LIGHT_BLUE)
    cprint("LIGHT PURPLE", color=Colors.LIGHT_PURPLE)
    cprint("LIGHT CYAN", color=Colors.LIGHT_CYAN)
    cprint("WHITE", color=Colors.WHITE)
    return


if __name__ == "__main__":
    test_color_printing()
