import os
import torch
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from model_utils import predict_image
import imghdr 

app = FastAPI()

static_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

app.mount("/static", StaticFiles(directory=static_path), name="static")

model = torch.jit.load(
    'scripted_model.pt',
    map_location='cpu'
)
model.eval()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("alzheimer.html", {"request": request})

@app.post("/predict")
async def predict(request: Request, img: UploadFile = File(...)):
    if img.filename == "":
        return templates.TemplateResponse(
            "alzheimer.html",
            {"request": request, "prediction": "No file selected."}
        )

    # Check if the file is an image
    file_extension = imghdr.what(img.file)
    if not file_extension:
        return templates.TemplateResponse(
            "alzheimer.html",
            {"request": request, "prediction": "Invalid file format. Please upload an image."}
        )
    image_bytes = await img.read()
    prediction = predict_image(model, image_bytes)
    return templates.TemplateResponse(
        "alzheimer.html",
        {"request": request, "prediction": prediction}
    )