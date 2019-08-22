#!/usr/bin/env python3
# coding: utf8

"""
constants.py
Date: 08-21-2019

Description: Defines the codes required for ansi code generation
"""


COLOR_CODES = {
    "b": "blue",
    "r": "red",
    "g": "green",
    "p": "purple",
    "y": "yellow",
    "c": "cyan",
    "w": "white",
    "lg": "light_green",
    "dg": "dark_gray",
    "lr": "light_red",
    "ly": "light_yellow",
    "lb": "light_blue",
    "lm": "light_magenta",
    "lc": "light_cyan",
    "n": "none",
    "db": "dodger_blue"
}

COLORS = {
    "black": ("30m", "40;"),
    "red": ("31m", "41;"),
    "green": ("32m", "42;"),
    "yellow": ("33m", "43;"),
    "blue": ("34m", "44;"),
    "purple": ("35m", "45;"),
    "cyan": ("36m", "46;"),
    "light_gray": ("37m", "47;"),
    "dark_gray": ("90m", "100;"),
    "light_red": ("91m", "101;"),
    "light_green": ("92m", "102;"),
    "light_yellow": ("93m", "103;"),
    "light_blue": ("94m", "104;"),
    "light_magenta": ("95m", "105;"),
    "light_cyan": ("96m", "106;"),
    "white": ("97m", "107;"),
    "none": ("39m", "49;"),
    "dodger_blue": ("38;5;33m", "48;5;33m")

}


if __name__: "__main__":
    pass
