#!/usr/bin/env python3
import unittest
from isitahaiku import isHaiku

class TestTheThing(unittest.TestCase):

    def test_negative(self):
        self.assertFalse(isHaiku("foo bar baz"))

    def test_positive(self):
        haiku = """I Windowed my skype
        Then closed my browser window
        Death only answer"""
        self.assertTrue(isHaiku(haiku))

if __name__ == '__main__':
    unittest.main()
