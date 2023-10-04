from sqp import DB, Field

db = DB('test.sqlite')
db.create_table('first_table', Field('x', 'int'))
db.create_table('second_table', Field('y', 'int'), Field('name', 'string'))

if __name__ == '__main__':
    # db.first_table.insert(x=1)
    # print(((db.first_table.x > 0) & (db.second_table.y > 0)).select( distinct=False, orderby=db.first_table.x))
    print(db.first_table.select(distinct=False, orderby=db.first_table.x))