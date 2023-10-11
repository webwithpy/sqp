from sqp import DB, Table, Field


class Test(Table):
    a = Field("int")


class Test2(Table):
    b = Field("int")


if __name__ == "__main__":
    db = DB("test.sqlite")
    db.create_tables()
    # db.Test.insert(a=5)
    # db.Test.insert(a=7)
    # db.Test2.insert(b=1)
    # db.Test2.insert(b=7)
    (db.Test.a == db.Test2.b).delete()
