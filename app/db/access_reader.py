import pyodbc


class AccessReader:
    def __init__(self):
        pass

    def read(self, db_filepath: str):
        connection = self._connect(db_filepath)


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
