import unittest

from mp3 import create_parser


class Mp3TestCase(unittest.TestCase):
    """Tests for `mp3.py`."""

    def test_parser(self):
        """Is generated parser correctly"""
        parser = create_parser(['/localsytem/'])
        self.assertFalse(parser.overwrite_title)

    def test_parser_overwrite(self):
        """Is generated pasrer correctly"""
        parser = create_parser(['/localsytem/', '--overwrite_title'])
        self.assertTrue(parser.overwrite_title)


if __name__ == '__main__':
    unittest.main()
