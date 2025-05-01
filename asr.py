import whisper

# Load Whisper model once
whisper_model = whisper.load_model("small")

def transcribe(audio_path):
    result = whisper_model.transcribe(audio_path)
    return result["text"]
