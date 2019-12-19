from query_sql_server import QuerySQLServer
from query_oracle import QueryOracle

if __name__ == "__main__":
    sql_query = "SELECT * FROM table"

    sql_server = QuerySQLServer()
    sql_server.execute_query("SQL-Server", sql_query)
    print()
    oracle = QueryOracle()
    oracle.execute_query("Oracle", sql_query)
