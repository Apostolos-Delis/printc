#!/usr/bin/env python3
# coding: utf8

"""
constants.py
Date: 08-21-2019

Description: Defines the codes required for ansi code generation
"""


START = "\033["
END = "\033[0m"

COLOR_CODES = {
    "k": "black",
    "b": "blue",
    "r": "red",
    "g": "green",
    "p": "purple",
    "y": "yellow",
    "c": "cyan",
    "w": "white",
    "lg": "light green",
    "dg": "dark gray",
    "lr": "light red",
    "ly": "light yellow",
    "lb": "light blue",
    "lm": "light magenta",
    "lc": "light cyan",
    "n": "none",
    "db": "dodger blue"
}

COLORS = {
    "black": ("30m", "40;"),
    "red": ("31m", "41;"),
    "green": ("32m", "42;"),
    "yellow": ("33m", "43;"),
    "blue": ("34m", "44;"),
    "purple": ("35m", "45;"),
    "cyan": ("36m", "46;"),
    "light gray": ("37m", "47;"),
    "dark gray": ("90m", "100;"),
    "light red": ("91m", "101;"),
    "light green": ("92m", "102;"),
    "light yellow": ("93m", "103;"),
    "light blue": ("94m", "104;"),
    "light purple": ("95m", "105;"),
    "light cyan": ("96m", "106;"),
    "white": ("97m", "107;"),
    "none": ("39m", "49;"),
    "dodger blue": ("38;5;33m", "48;5;33m")
}

STYLES = {
    "NONE": "0;",
    "BOLD": "1;",
    "FADE": "2;",
    "UNDERLINE": "4;",
    "BLINK": "5;",
}


if __name__ == "__main__":
    pass
