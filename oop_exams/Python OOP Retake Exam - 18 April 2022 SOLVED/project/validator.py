class Validator:
    @staticmethod
    def get_proper_string(some_string, message):
        if some_string.strip() == "":
            raise ValueError(message)

    @staticmethod
    def get_proper_age(num, message):
        if num < 6:
            raise ValueError(message)

    @staticmethod
    def get_proper_year(num, message):
        if num < 1888:
            raise ValueError(message)
