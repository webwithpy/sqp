class Query:
    def __init__(self, db, operator, first=None, second=None):
        self.db = db
        self.operator = operator
        self.first = first
        self.second = second


