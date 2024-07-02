import torch
if torch.cuda.is_available():
    print(15)
else:
    print(0)