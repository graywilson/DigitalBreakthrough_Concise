import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Установите устройство (CPU или CUDA, если доступно)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Путь к директории с файлами модели
model_path = ""  # Текущая директория, измените если файлы в другом месте

# Загрузка модели и токенизатора из локальных файлов
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

# Чтение запроса из файла
with open("request.txt", "r", encoding="utf-8") as file:
    prompt = file.read().strip()  # Читаем содержимое файла и убираем лишние пробелы

# Подготовка входных данных
messages = [
    {"role": "system", "content": "Ты - Сотрудник РЖД. Ты - полезный ассистент. Ты пишешь только то, что от тебя просят."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# Токенизация входных данных
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
token_count = len(tokenizer([text], return_tensors="pt")['input_ids'][0])/4 #делю на 4 чтобы уменьшить размер токена
print(f"Token count: {token_count}")

# Генерация ответа
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=token_count,  # Убедитесь, что этот параметр не слишком высок для вашей модели
    do_sample=True,
    temperature=0.7
)

generated_ids = [output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)]

# Декодирование и вывод результата
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
