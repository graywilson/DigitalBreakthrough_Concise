import os
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


def main():
    # Пример использования:
    db = AccessReader()

    # Строим абсолютный путь к базе данных относительно текущего скрипта
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "..", "data", "accdb", "spravochnik_tovarov.accdb")
    
    print(f"Путь к базе данных: {db_path}")
    
    records = db.read_all(db_path)

    for record in records:
        print(record)

if __name__ == "__main__":
    main()