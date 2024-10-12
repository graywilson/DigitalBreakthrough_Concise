import pyodbc
import os
import json

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

# Функция для сохранения таблицы в файл в формате JSON как массив объектов
def save_to_json(file_path, result_table):
    try:
        # Список для хранения всех записей
        all_records = []
        
        # Перебираем все строки результата
        for row in result_table:
            # Создаём словарь для каждой записи
            row_dict = {
                "КодСКМТР": row[0],
                "Наименование": row[1],
                "Маркировка": row[2],
                "Регламенты": row[3],
                "Параметры": row[4],
                "БазиснаяЕдиницаИзмерения": row[5],
                "ОКПД2": row[6]
            }
            # Добавляем запись в список
            all_records.append(row_dict)
        
        # Записываем весь список как массив JSON-объектов
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(all_records, file, ensure_ascii=False, indent=4)
        
        print(f"Результаты успешно сохранены в файл: {file_path}")
        
        # Возвращаем массив JSON-объектов
        return all_records
    
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")
        return None  # Возвращаем None в случае ошибки

# Функция для поиска записей по ОКПД2
def get_records_by_number(okpd2_code, database_path):
    # Подключаемся к базе данных
    connection = connect_to_db(database_path)
    
    if connection:
        try:
            cursor = connection.cursor()
    
            # SQL запрос для выборки всех необходимых полей по ОКПД2
            query = f"""
                SELECT *
                FROM MTR
                """
            
            cursor.execute(query)
            
            # Получаем все результаты
            records = cursor.fetchall()
            
            output_file_path = 'okpd2_get_records_by_number_outputs.json'
            # Сохраняем результат в файл как JSON
            out_json = save_to_json(output_file_path, records)
        except pyodbc.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрываем соединение
            connection.close()
            return out_json
    else:
        print("Не удалось подключиться к базе данных.")
    
    return "Error"

# Пример использования
if __name__ == "__main__":
    # Получаем текущую директорию, где находится скрипт
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Поднимаемся на один уровень вверх, затем строим путь к базе данных
    db_path = os.path.join(base_dir, "..", "data", "accdb", "spravochnik_tovarov.accdb")
    
    # Приводим путь к абсолютному виду
    db_path = os.path.abspath(db_path)
    
    print(f"Путь к базе данных: {db_path}")
    okpd2_code = '25.73.30.175'  # Заданный ОКПД2 код

    out = get_records_by_number(okpd2_code, db_path)
    #print(out)
