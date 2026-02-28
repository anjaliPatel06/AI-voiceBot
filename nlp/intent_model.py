import torch
import json
from transformers import BertTokenizer, BertForSequenceClassification
from huggingface_hub import hf_hub_download

model_name = "PatelAnjali/voicebot-intent-model"

# Load tokenizer & model
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

model.eval()

# Download label_map.json from HF repo
label_map_path = hf_hub_download(
    repo_id=model_name,
    filename="label_map.json"
)

with open(label_map_path, "r") as f:
    label_map = json.load(f)

def predict_intent(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs).item()
    confidence = torch.max(probs).item()

    intent = label_map[str(pred)]

    return intent, confidence