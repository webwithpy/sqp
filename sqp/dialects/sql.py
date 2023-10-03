class SQLDialect:
    equals = '='
    and_ = 'AND'
    or_ = 'OR'
    neq = '!='

    @classmethod
    def sql_str(cls, value):
        return f"'{value}'"
