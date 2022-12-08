from project.table.table import Table
from project.validator import Validator


class InsideTable(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.set_table_number(value, 1, 50, "Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value
