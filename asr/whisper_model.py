from faster_whisper import WhisperModel

model = None

def get_model():
    global model
    if model is None:
        model = WhisperModel(
            "tiny",
            device="cpu",
            compute_type="int8"   
        )
    return model


def transcribe_audio(file_path):
    model = get_model()

    segments, info = model.transcribe(file_path)

    text = ""
    for segment in segments:
        text += segment.text

    return text.strip()
