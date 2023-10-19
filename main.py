from sqp import DB, Table, Field
from pathlib import Path


class Test(Table):
    a = Field("int")
    b = Field("image")


class Test2(Table):
    b = Field("int")


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, "rb") as file:
        blobData = file.read()
    return blobData


if __name__ == "__main__":
    db = DB("sqlite:/test.sqlite")
    db.create_tables()

    db.Test.insert(a=10, b=convertToBinaryData("cat.jpg"))

    # db.Test.insert(a=7)
    # db.Test2.insert(b=1)
    # db.Test2.insert(b=7)
