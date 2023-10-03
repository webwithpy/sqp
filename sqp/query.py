class Query:
    def __init__(self, db, dialect, operator, first=None, second=None):
        self.db = db
        self.dialect = dialect
        self.operator = operator
        self.first = first
        self.second = second

    def select(self, fields: list = "*", orderby=None):
        unpacked = self.dialect.unpack(self)
        tables, where = self._unpacked_as_sql(unpacked).values()
        print(tables)
        join = f"{tables[0]}"
        if len(tables) > 1:
            join += self.tbls_to_join(tables)

        sql = self._select(fields, join, where, orderby)
        print(sql)
        return self.db.execute(sql).fetchall()

    def tbls_to_join(self, tables):
        sql = f""
        for table in tables[1:]:
            sql += f" LEFT JOIN {table} "
        return sql

    def _select(self, fields, tables, where=None, orderby=None):
        return f"SELECT {fields} FROM {tables}{where}"

    def _unpacked_as_sql(self, unpacked: dict):
        sql = {"tables": [], "where": " WHERE "}

        while unpacked["fields"]:
            field1 = str(unpacked["fields"].pop(0))
            field2 = str(unpacked["fields"].pop(0))
            stmt = unpacked["stmts"].pop(0)

            sql["where"] += (tl := self._translate_field(field1))["where"]

            if tl["table"]:
                sql["tables"] += tl["table"]

            sql["where"] += f"{stmt} {(tl := self._translate_field(field2))['where']}"

            if tl["table"] and tl["table"] not in sql["tables"]:
                sql["tables"] += tl["table"]

            if unpacked["stmts"]:
                sql["where"] += unpacked["stmts"].pop(0) + " "

        return sql

    def _translate_field(self, field):
        if "." in str(field):
            table = [field.split(".")[0]]
            where = f"{field} "
        elif str(field).isnumeric():
            table = None
            where = f"{field} "
        else:
            table = None
            where = f"'{field}' "

        return dict(table=table, where=where)

    def __and__(self, other):
        return Query(self.db, self.dialect, self.dialect.and_, self, other)

    def __or__(self, other):
        return Query(self.db, self.dialect, self.dialect.or_, self, other)