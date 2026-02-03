import torch

class DummyVoiceModel(torch.nn.Module):
    def forward(self, x):
        return torch.tensor([0.88])  # fake confidence

model = DummyVoiceModel()
model.eval()
