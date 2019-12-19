from abc import ABC
from abc import abstractmethod


class QueryTemplate(ABC):
    @abstractmethod
    def format_connect(self, db_name: str) -> str:
        pass

    @abstractmethod
    def format_select(self, spec_query: str) -> str:
        pass

    def execute_query(self, db_name: str, spec_query: str):
        db_command = self.format_connect(db_name)
        print(db_command)
        # here operation connecting to DB using db_command ...

        db_command = self.format_select(spec_query)
        print(db_command)
        # here executing query using db_command ...

        # returns a set of records as the result of a query
