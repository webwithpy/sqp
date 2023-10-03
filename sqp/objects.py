from .dialects.sqlite import SqliteDialect
from .query import Query


class Field:
    def __init__(self, field_name, field_type):
        self.cursor = None
        self.table_name = ''
        self.field_name = field_name
        self.field_type = field_type

    def __str__(self):
        return f"{self.table_name}.{self.field_name}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return Query(self.cursor, SqliteDialect, SqliteDialect.equals, self, other)

    def __ne__(self, other):
        return Query(self.cursor, SqliteDialect, SqliteDialect.neq, self, other)


class Table:
    def __init__(self, table_name: str, fields: list):
        self.cursor = None
        self.table_name = table_name
        self.fields: dict = {field.field_name: field for field in fields}

    def __getattribute__(self, item):
        try:
            return super(Table, self).__getattribute__(item)
        except Exception as e:
            if item in self.fields.keys():
                return self.fields[item]

            raise e

