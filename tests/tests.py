# coding: utf8

"""
Different unit tests for the printc library
"""
from printc import *
import pytest

class TestClass(object):
    
    def __init__(self):
        self.name = "TestClass"

    def __repr__():
        return self.name 

def test_all_colors(content):
    printc(content, color=BLACK)
    printc(content, color=RED)
    printc(content, color=GREEN)
    printc(content, color=ORANGE)
    printc(content, color=BLUE)
    printc(content, color=PURPLE)
    printc(content, color=CYAN)
    printc(content, color=NC)
    printc(content, color=LIGHT_GRAY)
    printc(content, color=DARK_GRAY)
    printc(content, color=LIGHT_RED)
    printc(content, color=LIGHT_GREEN)
    printc(content, color=LIGHT_BLUE)
    printc(content, color=LIGHT_PURPLE)
    printc(content, color=LIGHT_CYAN)
    printc(content, color=WHITE)
    return

def test_all_highlights(content):
    printc(content, highlight=BLACK)
    printc(content, highlight=RED)
    printc(content, highlight=GREEN)
    printc(content, highlight=ORANGE)
    printc(content, highlight=BLUE)
    printc(content, highlight=PURPLE)
    printc(content, highlight=CYAN)
    printc(content, highlight=NC)
    printc(content, highlight=LIGHT_GRAY)
    printc(content, highlight=DARK_GRAY)
    printc(content, highlight=LIGHT_RED)
    printc(content, highlight=LIGHT_GREEN)
    printc(content, highlight=LIGHT_BLUE)
    printc(content, highlight=LIGHT_PURPLE)
    printc(content, highlight=LIGHT_CYAN)
    printc(content, highlight=WHITE)
    return

def test_ascii_str():
    """
    Tests printc with a really easy string that it 
    should pass. 
    If it fails this case, it will most likely fail everything
    else.
    """
    simple_string = "Hello world in Color!"
    test_all_colors(simple_string)
    test_all_highlights(simple_string)
    return

def test_unicode_str():
    """
    Test with a unicode string to make sure that there is still 
    color support. 
    """
    unicode_string = u"'''&éאָדки((-편è__çίρετà)==)^邮政编^¨¨"
    test_all_colors(simple_string)
    test_all_highlights(simple_string)
    return

def print_numbers():
    """
    Test to see if printc has numeric support
    """
    test_all_colors(1234567890)
    test_all_highlights(1234567890)
    return 

def print_list():
    """
    Test to see if list printing is supported
    """
    l = ["Hello", 123, "邮政编", [1, 2, "World"]]
    test_all_colors(l)
    test_all_highlights(l)

def print_tuple():
    """
    Test to see if tuple printing is supported
    """
    t = ("Hello", 123, "邮政编", (1, 2, "World"))
    test_all_colors(t)
    test_all_highlights(t)

def print_object():
    """
    Test to see if printc works on objects
    """
    test_all_colors(TestClass())
    test_all_highlights(TestClass())

if __name__ == "__main__":
    taa = 
    test_ascii_str()
