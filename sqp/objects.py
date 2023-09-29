class Table:
    def __init__(self, table_name: str, fields: list):
        self.cursor = None
        self.table_name = table_name
        self.fields: dict = {field.field_name: field for field in fields}

    def __getattribute__(self, item):
        try:
            return super(Table, self).__getattribute__(item)
        except Exception as e:
            for field in self.fields:
                if field.field_name == item:
                    return field

            raise e


class Field:
    def __init__(self, field_name, field_type):
        self.cursor = None
        self.table_name = ''
        self.field_name = field_name
        self.field_type = field_type

