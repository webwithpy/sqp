from sqp import DB, Table, Field

db = DB("test.sqlite")


class Test(Table):
    a = Field("int")


db.create_tables()

if __name__ == "__main__":
    print((db.Test.a > 0).select())
