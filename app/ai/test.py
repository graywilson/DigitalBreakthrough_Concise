import torch
print(torch.cuda.is_available())  # Для CUDA, должно быть False
print(torch.version.hip)  # Для ROCm, должно вывести версию ROCm, если всё установлено верно
