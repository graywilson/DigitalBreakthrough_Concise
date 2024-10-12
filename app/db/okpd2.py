import pyodbc

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

# Функция для поиска записей по ОКПД2
def find_records_by_okpd2(connection, okpd2_code):
    cursor = connection.cursor()
    
    # SQL запрос для выборки записей с заданным ОКПД2
    query = f"""
    SELECT Наименование, Параметры
    FROM MTR
    WHERE [ОКПД2] = '{okpd2_code}'
    """
    
    cursor.execute(query)
    
    # Получаем все результаты
    records = cursor.fetchall()
    
    # Создаем словарь для уникальных записей
    unique_records = {}
    
    # Добавляем записи в словарь, чтобы исключить дубликаты по Наименованию
    for record in records:
        name = record[0]
        params = record[1]
        
        if name not in unique_records:
            unique_records[name] = params
    
    # Преобразуем словарь в список для сохранения
    result_table = [(name, params) for name, params in unique_records.items()]
    
    return result_table

# Функция для сохранения таблицы в текстовый файл
def save_to_txt(file_path, result_table):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for name, params in result_table:
                file.write(f"('{name}') ('{params}')\n")
        print(f"Результаты успешно сохранены в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")

def save_names_to_txt(file_path, result_table):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for name, params in result_table:
                file.write(f"('{name}')\n")
        print(f"Результаты успешно сохранены в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")
        
# Путь к файлу базы данных
database_path = r'..\db\data\spravochnik_tovarov.accdb'  # Используем полный путь
# Путь для сохранения txt-файла
output_file_path = 'result_table.txt'

def get_names(okpd2_code):
    # Подключаемся к базе данных
    connection = connect_to_db(database_path)
    
    if connection:
        try:
            # Получаем записи по ОКПД2
            result_table = find_records_by_okpd2(connection, okpd2_code)
            
            # Сохраняем результат в файл
            save_names_to_txt("result_ name_table.txt", result_table)
        
        except pyodbc.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрываем соединение
            connection.close()
    else:
        print("Не удалось подключиться к базе данных.")

# Пример использования
if __name__ == "__main__":
    okpd2_code = '25.73.30.175'  # Заданный ОКПД2 код
    get_names(okpd2_code)

    # Подключаемся к базе данных
    connection = connect_to_db(database_path)
    
    if connection:
        try:
            # Получаем записи по ОКПД2
            result_table = find_records_by_okpd2(connection, okpd2_code)
            
            # Сохраняем результат в файл
            save_to_txt(output_file_path, result_table)
        
        except pyodbc.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрываем соединение
            connection.close()
    else:
        print("Не удалось подключиться к базе данных.")
