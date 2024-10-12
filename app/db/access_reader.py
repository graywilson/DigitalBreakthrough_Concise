import pyodbc


class AccessReader:
    def __init__(self):
        pass

    def read_all(self, db_filepath: str):
        records = []
        connection = self._connect(db_filepath)
        if connection is not None:
            query = f"""
                SELECT *
                FROM MTR
                """
            cursor = connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            connection.close()
        return records

    def _connect(self, db_filepath: str) -> pyodbc.Connection | None:
        conn_str = (
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
            f"DBQ={db_filepath};"
        )
        try:
            connection = pyodbc.connect(conn_str)
            return connection
        except pyodbc.Error as e:
            print(f"Ошибка при подключении к базе данных: {e}")
            return None
