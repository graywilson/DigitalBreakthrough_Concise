import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread
import sys

class AIRequest:
    def __init__(self, model_path):
        #print("================>   " + model_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")
        
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype="auto",
            device_map="auto",
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

    def analyze(self, prompt):
        messages = [
            {"role": "system", "content": "Ты - сотрудник РЖД. Ты - полезный ассистент. Ты делаешь только то, о чем тебя просят."},
            {"role": "user", "content": prompt}
        ]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
        
        generated_ids = self.model.generate(
            **model_inputs,
            max_new_tokens=512,
            do_sample=True,
            temperature=0.7
        )
        generated_ids = generated_ids[:, model_inputs.input_ids.shape[-1]:]
        
        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        print(response)
        return response


def main():
    # Пример использования:
    ai = AIRequest(".")
    result = ai.analyze("Напиши стих об осени")
    print(result)  # Раскомментируйте, если хотите вывести результат еще раз

if __name__ == "__main__":
    main()