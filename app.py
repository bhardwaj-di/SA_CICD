from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

app= FastAPI()

MODEL_NAME = 'distilbert-base-uncased-finetuned-sst-2-english'
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Input data format using Pydantic
class TextInput(BaseModel):
    text: str


# Mapping from class index to sentiment label
LABEL_MAP = {0: "negative", 1: "positive"}

# Prediction route
@app.post("/predict")
async def predict(input_data: TextInput):
    # Tokenize the input text
    inputs = tokenizer(input_data.text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    # Model inference
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        # Map class index to sentiment label
    sentiment = LABEL_MAP[predicted_class]
    
    # Return the predicted sentiment
    return {"prediction": sentiment}
