from sqp import DB, Field

db = DB('test.sqlite')
db.create_table('first_table', Field('name', 'int'))

if __name__ == '__main__':
    print(db.first_table.name)
