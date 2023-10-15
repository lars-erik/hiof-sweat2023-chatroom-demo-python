from sqlalchemy import desc


class QueryWrapper:

    def __init__(self, query):
        self.query = query

    def __iter__(self):
        return self.query.__iter__()

    def __getitem__(self, item):
        return self.query[item]

    def count(self):
        return self.query.count()

    def skip(self, count):
        return QueryWrapper(self.query.offset(count))

    def limit(self, count):
        return QueryWrapper(self.query.limit(count))

    def order_by_descending(self, name):
        return QueryWrapper(self.query.order_by(desc(name)))
