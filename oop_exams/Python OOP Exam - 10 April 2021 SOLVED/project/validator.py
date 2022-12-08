class Validator:
    @staticmethod
    def check_for_empty_strings(value: str, message):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def check_for_negative_or_zero_value(value: int, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def set_table_number(value: int, min_num: int, max_num: int, message):
        if not min_num <= value <= max_num:
            raise ValueError(message)
