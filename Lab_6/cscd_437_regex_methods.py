import re

class CSCD437RegExMethods:
    """
    A class containing skeleton methods for students to implement validation of IPv6 addresses,
    passwords, money (in US and Euro formats), and email addresses using regular expressions.
    """

    @staticmethod
    def ipv6_pattern(ipv6_string):
        """
        Validate if the input string is a valid IPv6 address.
        """
        if not ipv6_string:
            raise ValueError("Bad ipv6_string Parameter to the method")

        regex = r"(?:[0-9a-fA-f]{1,4}::?){1,7}[0-9a-fA-f]{1,4}"
        return re.fullmatch(regex, ipv6_string) is not None

    @staticmethod
    def password_pattern(password_string):
        """
        Validate if the input string is a valid password.
        Criteria for a valid password defined in Lab PDF
        """
        if not password_string:
            raise ValueError("Bad password_string Parameter to the method")

        regex = r"^(?=.*?[A-Z])(?=.*?[a-z].*?[a-z])(?=.*?[0-9].*?[0-9])(?=.*?[#?!@$ %^&*-,.()_=+])(?!.*?[a-z]{3,})(?!.*?[0-9]{3,}).{12,}"
        return re.fullmatch(regex, password_string) is not None

    @staticmethod
    def money_pattern(money_string):
        """
        Validate if the input string is in a valid money format, either US or Euro.
        """
        if not money_string:
            raise ValueError("Bad money_string Parameter to the method")

        regex = r"(\$[0-9]{1,3}(?:\,[0-9]{3})*\.[0-9]{1,2})|([0-9]{1,3}(?:\.?[0-9]{1,3})*\,[0-9]{1,2})"
        return re.fullmatch(regex, money_string) is not None

    @staticmethod
    def email_pattern(email_string):
        """
        Validate if the input string is a valid email address.
        """
        if not email_string:
            raise ValueError("Bad email_string Parameter to the method")

        regex = r"^(?:(?!.*[eE][aA][sS][tT][eE][rR][nN])(?!.*[eE][aA][gG][lL][eE][sS]))(.{2,}(?<!\.))@(.{2,})\.(.{2,})"
        return re.fullmatch(regex, email_string) is not None
