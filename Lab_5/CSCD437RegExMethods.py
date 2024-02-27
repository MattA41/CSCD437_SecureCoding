import re


def date_pattern_helper(date_string):
    if date_string[3] == '/' or date_string[2] == '/':
        string_split = date_string.split('/')
    else:
        string_split = date_string.split('-')
    if string_split[0] == "2" or string_split[0] == "02" and string_split[3].parseInt() % 400 == 0:
        regex = r'(?:0?[1-9]|1[0-2])([-\/])(?:0?[1-9]|1[0-9]|2[0-9])\1[0-9]{4}'
    if string_split[0] == "2" or string_split[0] == "02" and string_split[3].parseInt() % 400 != 0:
        regex = r'(?:0?[1-9]|1[0-2])([-\/])(?:0?[1-9]|1[0-9]|2[0-8])\1[0-9]{4}'
    else:
        regex = r"(?:0?[1-9]|1[0-2])(-|\/)(?:0?[1-9]|1[0-9]|2[0-9]|3[0-1])\1[0-9]{4}"
    return regex


class CSCD437RegExMethods:
    
    @staticmethod
    def ssn_pattern(ssn_string : str) -> bool:
        if not isinstance(ssn_string, str) or not ssn_string.strip():
            raise ValueError("Bad ssn_string Parameter")
        regex =r"[1-9]{3}[-|\s]?[1-9]{2}[-|\s]?[1-9]{4}"

        return re.fullmatch(regex, ssn_string) is not None

    @staticmethod
    def phone_pattern(phone_string : str) -> bool:
        if not isinstance(phone_string, str) or not phone_string.strip():
            raise ValueError("Bad phone_string Parameter")
        regex =r"(?:\+1\s)?\(?[0-9]{3}\)?[-|\s][0-9]{3}[-|\s][0-9]{4}"

        return re.fullmatch(regex, phone_string) is not None

    @staticmethod
    def name_pattern(name_string : str) -> bool:
        if not isinstance(name_string, str) or not name_string.strip():
            raise ValueError("Bad name_string Parameter")
        regex = r"[a-zA-z]+[\s|\-]?[a-zA-z]+?I{0,1}X{0,1}V{0,1}I{0,3}\,\s[a-zA-z]+\,?\s?[a-zA-z]?"

        return re.fullmatch(regex, name_string) is not None

    @staticmethod
    def date_pattern(date_string : str) -> bool:
        if not isinstance(date_string, str) or not date_string.strip():
            raise ValueError("Bad date_string Parameter")
        regex = date_pattern_helper(date_string)
        return re.fullmatch(regex, date_string) is not None
        
    @staticmethod
    def ipv4_pattern(ipv4_string : str) -> bool:
        if not isinstance(ipv4_string, str) or not ipv4_string.strip():
            raise ValueError("Bad ipv4_string Parameter")
        regex =(r"\b(?:[0-9]|[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\b\.\b(?:[0-9]|[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\b\."
                r"\b(?:[0-9]|[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\b(?:\.\b(?:[0-9]|[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\b)?")

        return re.fullmatch(regex, ipv4_string) is not None

