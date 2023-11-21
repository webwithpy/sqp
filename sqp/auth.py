from .objects import Table, Field


class AuthUser(Table):
    table_name = "auth_user"
    username = Field("string")
    email = Field("string")
    password = Field("string")
    password_two = Field("string")
