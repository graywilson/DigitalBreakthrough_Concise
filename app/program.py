# program.py

from ai.ai_request import AIRequest  # Предполагается, что класс AIAnalysis находится в файле ai_analysis.py
from vadim.okpd2_get_records_by_number import *


def main():
    #1. шаг для одноой группы ОКПД2
    okpd2_number = "26.11.12.000"
    
    
    
    #2. шаг для одной группы
    # Получаем текущую директорию, где находится скрипт
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Поднимаемся на один уровень вверх, затем строим путь к базе данных
    db_path = os.path.join(base_dir, "..", "data", "accdb", "spravochnik_tovarov.accdb")
    
    # Приводим путь к абсолютному виду
    db_path = os.path.abspath(db_path)
    
    print(f"Путь к базе данных: {db_path}")
    # Получаем результаты из функции get_records_by_number
    result_table = get_records_by_number(okpd2_number, db_path)
    print(result_table)
    
    # Инициализация AIAnalysis
    ai = AIRequest("ai/")  # Если модель находится не в текущей директории, укажите путь: AIAnalysis("path/to/model")
    
    # Чтение запроса из файла
    with open("ai/promts/request_groups.txt", "r", encoding="utf-8") as file:
        request = file.read().strip()

    print("Запрос:")
    print(request)
    print("\nОбработка запроса...\n")

    # Вызов метода analyze
    #result = ai.analyze(request)

    print("\nРезультат анализа:")
    print(result)


if __name__ == "__main__":
    main()