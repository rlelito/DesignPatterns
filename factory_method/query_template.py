from abc import ABC
from abc import abstractmethod
from database import DataBase
from database_sql_server import DataBaseSQLServer
from database_oracle import DataBaseOracle


class QueryTemplate(ABC):
    @abstractmethod
    def format_connect(self, db_name: str) -> str:
        pass

    @abstractmethod
    def format_select(self, spec_query: str) -> str:
        pass

    def execute_query(self, db_name: str, spec_query: str) -> None:
        # here creating database object
        db: DataBase = self.create_db(db_name)

        db_command = self.format_connect(db_name)
        print(db_command)
        # here connecting to database using db_command ...

        db_command = self.format_select(spec_query)
        print(db_command)
        # here execution of query using db_command ...

        # returns a set of records as the result of a query
        db.execute_select(db_command)

    @staticmethod
    def create_db(db_name: str) -> DataBase:
        return globals()[db_name]()
