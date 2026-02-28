from fastapi import FastAPI, UploadFile, File
import shutil

from asr.whisper_model import transcribe_audio
from nlp.intent_model import predict_intent
from nlp.response_generator import generate_response
from tts.tts_engine import text_to_speech

app = FastAPI()

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    input_path = "input.wav"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = transcribe_audio(input_path)

    return {"transcribed_text": text}


@app.post("/predict-intent")
async def intent_endpoint(text: str):
    intent, confidence = predict_intent(text)

    return {
        "intent": intent,
        "confidence": confidence
    }


@app.post("/generate-response")
async def response_endpoint(intent: str):
    response_text = generate_response(intent)

    return {"response_text": response_text}


@app.post("/synthesize")
async def synthesize_endpoint(text: str):
    audio_path = text_to_speech(text)

    return {"audio_file": audio_path}


@app.post("/voicebot")
async def voicebot(file: UploadFile = File(...)):
    input_path = "input.wav"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Step 1: ASR
    text = transcribe_audio(input_path)

    # Step 2: Intent
    intent, confidence = predict_intent(text)

    # Step 3: Response
    response_text = generate_response(intent)

    # Step 4: TTS
    audio_path = text_to_speech(response_text)

    return {
        "transcribed_text": text,
        "intent": intent,
        "confidence": confidence,
        "response_text": response_text,
        "audio_file": audio_path
    }