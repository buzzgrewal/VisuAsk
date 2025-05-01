import gradio as gr
from asr import transcribe
from qa import generate_answer
from tts import text_to_speech
from PIL import Image

def ask_the_image(image: Image.Image, audio_path: str):
    question = transcribe(audio_path)
    answer = generate_answer(image, question)
    spoken_audio_path = text_to_speech(answer)
    return answer, spoken_audio_path

iface = gr.Interface(
    fn=ask_the_image,
    inputs=[
        gr.Image(type="pil", label="Upload an Image"),
        gr.Audio(type="filepath", label="Ask a Question (via Mic, 10s max)")
    ],
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Audio(label="Spoken Answer")
    ],
    title="Ask-the-Image: Multimodal QA App",
    description="Upload an image and ask a question using your voice. The app answers and speaks it back."
)

if __name__ == "__main__":
    iface.launch(debug=True)
