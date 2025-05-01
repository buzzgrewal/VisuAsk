from gtts import gTTS
from tempfile import NamedTemporaryFile

def text_to_speech(text: str) -> str:
    tts = gTTS(text=text)
    temp_audio = NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_audio.name)
    return temp_audio.name
