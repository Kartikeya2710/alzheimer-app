import io
import torch
from torchvision import transforms
from PIL import Image

idx_to_labels = {0: 'MildDemented', 1: 'NonDemented', 2: 'VeryMildDemented', 3: 'ModerateDemented'}

def get_transforms():
    transform = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        # transforms.Normalize(mean=(self.config.mean,), std=(self.config.std,))
    ])
    return transform

def transform_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    transform = get_transforms()
    return transform(image).unsqueeze(0)

def predict_image(model, image_bytes, model_path='scripted_model'):
    image_tensor = transform_image(image_bytes=image_bytes)
    output = model.forward(image_tensor)
    _, prediction = torch.max(output.data, 1)

    return idx_to_labels[prediction.item()]