class SQLDialect:
    equals = '='
    and_ = 'AND'
    neq = '!='

    @classmethod


    @classmethod
    def sql_str(cls, value):
        return f"'{value}'"
