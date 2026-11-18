import unittest

from hash_identifier.patterns import is_hexadecimal


class TestHexadecimal(unittest.TestCase):

    def test_valid_hexadecimal(self):
        self.assertTrue(is_hexadecimal("5f4dcc3b5aa765d61d8327deb882cf99"))

    def test_uppercase_hexadecimal(self):
        self.assertTrue(is_hexadecimal("ABCDEF123456"))

    def test_invalid_characters(self):
        self.assertFalse(is_hexadecimal("hello123"))

    def test_invalid_hexadecimal_character(self):
        self.assertFalse(is_hexadecimal("12345g"))

    def test_empty_string(self):
        self.assertFalse(is_hexadecimal(""))

    def test_special_characters(self):
        self.assertFalse(is_hexadecimal("1234@abc"))


if __name__ == "__main__":
    unittest.main()
