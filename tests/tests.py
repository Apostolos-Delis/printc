# coding: utf8

"""
Different unit tests for the printc library
"""

import pytest

from printc import printc


class TestClass:
    """
    Dummy Test Class
    """

    def __init__(self):
        self.name = "TestClass"

    def __repr__(self):
        return self.name


def print_all_colors(content):
    """
    Prints the content with every type of colored text
    """
    printc(content, color="black")
    printc(content, color="red")
    printc(content, color="green")
    printc(content, color="yellow")
    printc(content, color="blue")
    printc(content, color="purple")
    printc(content, color="cyan")
    printc(content, color="none")
    printc(content, color="light gray")
    printc(content, color="dark gray")
    printc(content, color="light red")
    printc(content, color="light green")
    printc(content, color="light blue")
    printc(content, color="light purple")
    printc(content, color="light cyan")
    printc(content, color="white")


def print_all_highlights(content):
    """
    Print the Content with every type of background color
    """
    printc(content, highlight="black")
    printc(content, highlight="red")
    printc(content, highlight="green")
    printc(content, highlight="yellow")
    printc(content, highlight="blue")
    printc(content, highlight="purple")
    printc(content, highlight="cyan")
    printc(content, highlight="none")
    printc(content, highlight="light gray")
    printc(content, highlight="dark gray")
    printc(content, highlight="light red")
    printc(content, highlight="light green")
    printc(content, highlight="light blue")
    printc(content, highlight="light purple")
    printc(content, highlight="light cyan")
    printc(content, highlight="white")


def print_all_styles(content):
    """Test all 4 different types of styles along with various combinations"""
    printc(content, bold=True)
    printc(content, blink=True)
    printc(content, underline=True)
    printc(content, fade=True)
    printc(content, bold=True, underline=True, blink=True, fade=True)


def test_ascii_str():
    """
    Tests printc with a really easy string that it
    should pass.
    If it fails this case, it will most likely fail everything
    else.
    """
    simple_string = "Hello world in Color!"
    print_all_colors(simple_string)
    print_all_highlights(simple_string)
    print_all_styles(simple_string)


def test_unicode_str():
    """
    Test with a unicode string to make sure that there is still
    color support.
    """
    unicode_string = u"'''&éאָדки((-편è__çίρετà)==)^邮政编^¨¨"
    print_all_colors(unicode_string)
    print_all_highlights(unicode_string)
    print_all_styles(unicode_string)


def print_numbers():
    """
    Test to see if printc has numeric support
    """
    print_all_colors(1234567890)
    print_all_highlights(1234567890)
    print_all_styles(1234567890)


def print_list():
    """
    Test to see if list printing is supported
    """
    test_list = ["Hello", 123, "邮政编", [1, 2, "World"]]
    print_all_colors(test_list)
    print_all_highlights(test_list)
    print_all_styles(test_list)


def test_print_tuple():
    """
    Test to see if tuple printing is supported
    """
    test_tup = ("Hello", 123, "邮政编", (1, 2, "World"))
    print_all_colors(test_tup)
    print_all_highlights(test_tup)
    print_all_styles(test_tup)


def test_print_object():
    """
    Test to see if printc works on objects
    """
    print_all_colors(TestClass())
    print_all_highlights(TestClass())
    print_all_styles(TestClass())
