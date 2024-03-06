import unittest
from cscd_437_regex_methods import CSCD437RegExMethods

class CSCD437RegExTesting(unittest.TestCase):
    
    def test_ipv6_pattern_valid_format(self):
        self.assertTrue(CSCD437RegExMethods.ipv6_pattern("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))

    def test_ipv6_pattern_invalid_format(self):
        self.assertFalse(CSCD437RegExMethods.ipv6_pattern("20g1:0db8:85a3:00h0:0000:8a2e:03p0:7334"))

    def test_password_pattern_valid_format(self):
        self.assertTrue(CSCD437RegExMethods.password_pattern("A7xB?9jI4@8jK"))

    def test_password_pattern_invalid_format(self):
        self.assertFalse(CSCD437RegExMethods.password_pattern("A7xB?9JI4@8JK"))

    def test_money_pattern_valid_format(self):
        self.assertTrue(CSCD437RegExMethods.money_pattern("$123,123,123.23"))

    def test_money_pattern_invalid_format(self):
        self.assertFalse(CSCD437RegExMethods.money_pattern("123,123,123.123"))

    def test_email_pattern_valid_format(self):
        self.assertTrue(CSCD437RegExMethods.email_pattern("stu.stiner@ewu.edu"))

    def test_email_pattern_invalid_format(self):
        self.assertFalse(CSCD437RegExMethods.email_pattern("stu.stiner.@ewu.edu"))



if __name__ == '__main__':
    unittest.main()