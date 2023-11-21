from sqp import DB, Table, Field
from sqp.tools import cacher
from pathlib import Path
import time


class Test(Table):
    a = Field("int")
    b = Field("image")


class Test2(Table):
    cache = True
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
    db.create_tables(Test, Test2)
    db.create_auth()

    # for _ in range(1000):
    #     db.Test2.insert(name="John Doe", email="test@gmail.com")

    # start = time.time()
    # for _ in range(10000):
    #     (db.Test2.id >= 0).select()
    #
    # end = time.time()
    # print(f"Time taken: {(end - start):.4f} s")

    # cacher.print_cache()
    # db.Test2.insert(name="John Doe", email="test@gmail.com")
    # db.Test2.insert(name="John Doe", email="test@gmail.com")
