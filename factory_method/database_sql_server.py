from database import DataBase


class DataBaseSQLServer(DataBase):
    @staticmethod
    def execute_select(spec_query: str) -> None:
        print(f"Query '{spec_query}' was sent to SQL Server DB.")
