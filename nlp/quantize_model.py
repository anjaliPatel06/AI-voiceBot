import torch
import json
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from huggingface_hub import hf_hub_download

model_name = "PatelAnjali/voicebot-intent-distilbert-int8"

tokenizer = DistilBertTokenizer.from_pretrained(model_name)

model = DistilBertForSequenceClassification.from_pretrained(model_name)
model.eval()

model = torch.quantization.quantize_dynamic(
    model,
    {torch.nn.Linear},
    dtype=torch.qint8
)

# 🔹 Load label map
label_map_path = hf_hub_download(
    repo_id=model_name,
    filename="label_map.json"
)

with open(label_map_path, "r") as f:
    label_map = json.load(f)


