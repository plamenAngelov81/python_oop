class Checker:
    @staticmethod
    def check_for_empty_strings(value: str, message):
        if value.strip() == "":
            raise ValueError(message)