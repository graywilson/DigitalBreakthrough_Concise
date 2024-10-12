from transformers import GPTJForCausalLM, AutoTokenizer
import torch

# Загрузка модели и токенизатора
model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16, local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

# Функция для генерации ответа
def generate_response(prompt, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Пример использования
prompt = "Расскажи мне о искусственном интеллекте"
print(prompt)
response = generate_response(prompt)
print(response)