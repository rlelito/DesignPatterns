from query_template import QueryTemplate


class QueryOracle(QueryTemplate):
    def format_connect(self, db_name: str) -> str:
        return f"Connecting to {db_name}..."

    def format_select(self, spec_query: str) -> str:
        return f"{spec_query};"
