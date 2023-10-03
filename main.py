from sqp import DB, Field

db = DB('test.sqlite')
db.create_table('first_table', Field('x', 'int'))
db.create_table('second_table', Field('y', 'int'))

if __name__ == '__main__':
    print(((db.first_table.x != 1) & (db.second_table.y == 3)).select())
