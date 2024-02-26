import unittest
from CSCD437RegExMethods import CSCD437RegExMethods

class CSCD437RegExTesting(unittest.TestCase):
    
    def test_ssn_pattern_valid_format(self):
        self.assertTrue(CSCD437RegExMethods.ssn_pattern("123-45-6789"))

    def test_ssn_pattern_invalid_format(self):
        self.assertFalse(CSCD437RegExMethods.ssn_pattern("123-45-678a"))

    def test_name_pattern_valid_format(self):
        self.assertTrue(CSCD437RegExMethods.name_pattern("Doe, John"))

    def test_name_pattern_invalid_format(self):
        self.assertFalse(CSCD437RegExMethods.name_pattern("Doe, John1"))

    def test_phone_pattern_valid_format(self):
        self.assertTrue(CSCD437RegExMethods.phone_pattern("+1 (123) 456-7890"))

    def test_phone_pattern_invalid_format(self):
        self.assertFalse(CSCD437RegExMethods.phone_pattern("+1 (123) 456-789"))

    def test_date_pattern_valid_format(self):
        self.assertTrue(CSCD437RegExMethods.date_pattern("12-31-2020"))

    def test_date_pattern_invalid_format(self):
        self.assertFalse(CSCD437RegExMethods.date_pattern("12-31-20"))
        
    def test_ipv4_pattern_valid_format(self):
        self.assertTrue(CSCD437RegExMethods.ipv4_pattern("192.168.1.1"))

    def test_ipv4_pattern_invalid_format(self):
        self.assertFalse(CSCD437RegExMethods.ipv4_pattern("192.168.1.256"))


if __name__ == '__main__':
    unittest.main()