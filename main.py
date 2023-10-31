from sqp import DB, Table, Field
from pathlib import Path
import time
from cProfile import Profile
from pstats import SortKey, Stats


class Test(Table):
    a = Field("int")
    b = Field("image")


class Test2(Table):
    name = Field("string")
    email = Field("string")
    profile_picture = Field("blob")


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, "rb") as file:
        blobData = file.read()
    return blobData


if __name__ == "__main__":
    db = DB("sqlite:/test.sqlite")
    db.create_tables()

    # for _ in range(18):
    #     db.Test2.insert(name="John Doe", email="test@gmail.com")

    start = time.time()
    for _ in range(10000):
        (db.Test2.id >= 0).select()
    end = time.time()
    print(end - start)

    # db.Test2.insert(name="John Doe", email="test@gmail.com")
    # db.Test2.insert(name="John Doe", email="test@gmail.com")
