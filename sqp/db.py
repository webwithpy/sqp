from .objects import Table, Field
from sqlite3 import dbapi2 as sqlite
from pathlib import Path
from typing import Union


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class DB:
    def __init__(self, db_path: Union[Path, str]):
        if isinstance(db_path, str):
            db_path = Path(db_path)

        # make sure the db exists
        db_path.touch()

        self.conn = sqlite.connect(db_path)
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()

        self.tables = {}

    def create_table(self, table_name: str, *fields: Field):
        tbl = Table(table_name, fields)
        self.tables[table_name] = tbl

    def __getattribute__(self, item):
        try:
            return super(DB, self).__getattribute__(item)
        except Exception as e:
            if item in self.tables.keys():
                return self.tables[item]
            raise e
