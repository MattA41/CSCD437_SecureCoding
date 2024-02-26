import re

class CSCD437RegExMethods:
    
    @staticmethod
    def ssn_pattern(ssn_string : str) -> bool:
        if not isinstance(ssn_string, str) or not ssn_string.strip():
            raise ValueError("Bad ssn_string Parameter")
        regex ="[1-9]{3}[-|\s]?[1-9]{2}[-|\s]?[1-9]{4}"

        return re.fullmatch(regex, ssn_string) is not None

    @staticmethod
    def phone_pattern(phone_string : str) -> bool:
        if not isinstance(phone_string, str) or not phone_string.strip():
            raise ValueError("Bad phone_string Parameter")
        regex ="\+1?\s?\(?[0-9]{3}\)?[\s-]?[0-9]{3}[\s-]?[0-9]{4}"

        return re.fullmatch(regex, phone_string) is not None

    @staticmethod
    def name_pattern(name_string : str) -> bool:
        if not isinstance(name_string, str) or not name_string.strip():
            raise ValueError("Bad name_string Parameter")
        regex = ""

        return re.fullmatch(regex, name_string) is not None

    @staticmethod
    def date_pattern(date_string : str) -> bool:
        if not isinstance(date_string, str) or not date_string.strip():
            raise ValueError("Bad date_string Parameter")
        regex =""

        return re.fullmatch(regex, date_string) is not None
        
    @staticmethod
    def ipv4_pattern(ipv4_string : str) -> bool:
        if not isinstance(ipv4_string, str) or not ipv4_string.strip():
            raise ValueError("Bad ipv4_string Parameter")
        regex =""

        return re.fullmatch(regex, ipv4_string) is not None

