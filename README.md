# 🎙 AI-Powered Voice Bot for Customer Support Automation

## 📌 Project Overview

This project implements a production-ready AI Voice Bot capable of handling customer support queries using speech interaction.

The system performs:

Audio → Speech-to-Text → Intent Classification → Response Generation → Text-to-Speech → Audio Output

It demonstrates an end-to-end Machine Learning pipeline integrating ASR, NLP modeling, and API deployment.

---

## 🏗 System Architecture

Voice Input (WAV)
        ↓
Whisper ASR (Speech → Text)
        ↓
BERT Intent Classifier (Fine-tuned)
        ↓
Response Generator (Intent Mapping)
        ↓
Text-to-Speech (TTS)
        ↓
Audio Output (MP3)

Exposed via FastAPI REST API.

---

## 🛠 Technologies Used

- Python
- FastAPI
- OpenAI Whisper (ASR)
- HuggingFace Transformers (BERT)
- PyTorch
- gTTS (Text-to-Speech)
- Scikit-learn (Evaluation Metrics)
- FFmpeg (Audio Processing)

---

## 📂 Project Structure
AI_chatbot/
│
├── api/
│ └── main.py
│
├── asr/
│ └── whisper_model.py
│
├── nlp/
│ ├── intent_model.py
│ └── response_generator.py
│
├── tts/
│ └── tts_engine.py
│
├── evaluation/
│ └── asr_evaluation.py
│
├── model/
│ ├── saved_model/
│ └── label_map.json
│
├── data/
│ └── intent_dataset_updated_noisy.csv
│
└── README.md


---

## 🧠 Model Details

### 1️⃣ ASR (Speech Recognition)
- Model: Whisper (base)
- Handles WAV input
- Supports moderate noise
- Word Error Rate (WER): ~0.25

---

### 2️⃣ Intent Classification

- Model: BERT (bert-base-uncased)
- Fine-tuned on custom dataset
- Dataset size: ~700+ samples (clean + noisy)
- 10 customer-support intents:

    - cancel_order  
    - complaint  
    - goodbye  
    - greeting  
    - order_status  
    - payment_issue  
    - product_query  
    - refund  
    - subscription_issue  
    - technical_support  

## Model Choice Justification

- Whisper was selected for ASR due to strong multilingual performance and robustness to noise.
- BERT (bert-base-uncased) was chosen for intent classification because of its contextual understanding capability.
- gTTS was used for lightweight and simple TTS integration.
- FastAPI was selected for high performance and easy API documentation via Swagger.

Evaluation Results:

- Accuracy: 96.6%
- F1 Score: 96.68%
- Precision: 96.89%
- Recall: 96.66%

---



### 3️⃣ Response Generation

Structured response mapping based on predicted intent.

---

### 4️⃣ Text-to-Speech

- Engine: gTTS
- Returns playable MP3 audio file

---

## 🚀 API Endpoints

### 1️⃣ /transcribe
Speech → Text

### 2️⃣ /predict-intent
Text → Intent + Confidence

### 3️⃣ /generate-response
Intent → Response Text

### 4️⃣ /synthesize
Text → Audio (MP3)

### 5️⃣ /voicebot (Unified Endpoint)
Audio → Audio (Full Pipeline)

---

## API Usage Example

### Voicebot Endpoint

POST /voicebot

Upload WAV file

Response:

{
  "transcribed_text": "Payment failed",
  "intent": "payment_issue",
  "confidence": 0.98,
  "response_text": "We are checking your payment issue.",
  "audio_file": "response.mp3"
}

## 🧪 How to Run the Project

### 1️⃣ Install Dependencies
pip install -r requirements.txt


### 2️⃣ Install FFmpeg
Ensure FFmpeg is installed and added to system PATH.

Check:
ffmpeg -version


### 3️⃣ Run FastAPI Server
uvicorn api.main:app --reload


---

## 📊 Evaluation

### ASR
- Word Error Rate (WER): ~0.25

### NLP
- Accuracy: 96.6%
- Clean confusion matrix with minor realistic misclassifications

---

## ⚠ Limitations

- Dataset is synthetic and semi-structured
- Limited to predefined 10 intents
- Real-world deployment would require larger and more diverse dataset

---

## 🎥 Demo

The demo video shows:
- Uploading voice input
- ASR transcription
- Intent prediction
- Generated response
- Final audio output

---

## 🏆 Conclusion

This project successfully demonstrates:

- End-to-end ML pipeline
- Transformer fine-tuning
- Speech processing
- REST API deployment
- Modular clean architecture

It is production-structured and internship-ready.

---

## 👩‍💻 Author

Anjali Patel  
AI/ML Internship Task Submission