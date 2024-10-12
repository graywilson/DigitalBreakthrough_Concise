import pyodbc
from collections import Counter

# Подключение к базе данных Access
def connect_to_db(database_path):
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={database_path};"
    )
    try:
        connection = pyodbc.connect(conn_str)
        return connection
    except pyodbc.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

# Функция для получения количества уникальных ОКПД2 и топ 10 самых часто встречающихся кодов
def get_unique_okpd2_count_and_top10(connection):
    cursor = connection.cursor()
    
    # SQL запрос для выборки всех кодов ОКПД2
    query = "SELECT [ОКПД2] FROM MTR"
    
    cursor.execute(query)
    
    # Получаем все результаты
    records = cursor.fetchall()
    
    # Извлекаем все ОКПД2 коды (исключаем None)
    okpd2_codes = [record[0] for record in records if record[0] is not None]
    
    # Подсчитываем количество уникальных ОКПД2 кодов
    unique_okpd2 = set(okpd2_codes)
    unique_count = len(unique_okpd2)
    
    # Используем Counter для подсчета частоты встречаемости каждого кода
    code_counter = Counter(okpd2_codes)
    
    # Получаем топ 10 самых часто встречающихся кодов ОКПД2
    top_10_okpd2 = code_counter.most_common(100)
    
    return unique_count, top_10_okpd2

# Путь к файлу базы данных
database_path = r'..\db\data\spravochnik_tovarov.accdb'

# Пример использования
if __name__ == "__main__":
    # Подключаемся к базе данных
    connection = connect_to_db(database_path)
    
    if connection:
        try:
            # Получаем количество уникальных ОКПД2 и топ-10 самых частых кодов
            unique_okpd2_count, top_10_okpd2 = get_unique_okpd2_count_and_top10(connection)
            
            # Выводим количество уникальных кодов
            print(f"Количество уникальных ОКПД2 кодов: {unique_okpd2_count}")
            
            # Выводим топ 10 ОКПД2 кодов
            print("Топ 10 самых часто встречающихся ОКПД2 кодов:")
            for code, count in top_10_okpd2:
                print(f"ОКПД2 код: {code}, Количество строк: {count}")
        
        except pyodbc.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрываем соединение
            connection.close()
    else:
        print("Не удалось подключиться к базе данных.")
