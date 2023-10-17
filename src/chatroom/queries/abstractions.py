from typing import TypeVar, Generic


class Query:
    pass

TQuery = TypeVar('TQuery', bound=Query)

class QueryHandler(Generic[TQuery]):
    def execute(self, query: TQuery):
        pass