
# 🎤🖼️ VisuAsk: Speak to the Image. See What It Says.

## Introduction

Imagine asking a photo a question—just by speaking—and getting an instant, intelligent answer, both on-screen and read aloud. That’s exactly what **VisuAsk** does. Powered by the synergy of speech recognition, visual-language understanding, and text-to-speech synthesis, VisuAsk is a mini-app that brings conversational AI to life through multimodal interaction.

This blog post dives into how we built **VisuAsk**, a proof-of-concept app where users can ask questions about images using voice, and receive spoken answers. We'll walk you through the **architecture**, **technical components**, **implementation challenges**, and our **evaluation metrics**.

---

Sure! Here's a **long and detailed `README.md`** file for your **VisuAsk** project, written in Markdown and suitable for direct use on GitHub or other repositories.

---


## 🧠 Overview

**VisuAsk** is a proof-of-concept application that combines **speech-to-text**, **visual question answering (VQA)**, and **text-to-speech (TTS)** to create a natural, human-like interaction with images.

Using advanced models like **Whisper**, **BLIP-2**, and **Flan-T5**, this app enables users to:
- Record or upload voice input (up to 10 seconds).
- Upload or capture an image.
- Get intelligent answers to their spoken questions about the image.
- Hear the answer spoken back using TTS.

VisuAsk brings conversational AI into the multimodal realm — ideal for accessibility, education, and more.

---

## 📸 Demo Preview

![demo-gif](demo/demo.gif)  
*A user asks “What color is the car?” and hears the answer “The car is red.”*

> 🎥 Watch the full demo [here](https://youtu.be/your-demo-link)

---

## 🏗️ Project Structure

```
VisuAsk/
│
├── app.py              # Main application (Streamlit/Flask)
├── asr.py              # Speech-to-text (Whisper)
├── qa.py               # Visual Question Answering (BLIP-2 + Flan-T5)
├── tts.py              # Text-to-Speech (pyttsx3)
│
├── demo/               # Sample audio, images, demo video
│
├── requirements.txt    # Dependencies
├── README.md           # You're reading it!
```

---

## 🚀 Features

- 🎙️ **Voice Input:** Record or upload up to 10 seconds of spoken question.
- 🖼️ **Image Upload:** Accepts `.jpg`, `.png`, `.jpeg` files.
- 🔎 **VQA Engine:** Uses compact generative vision-language model (BLIP-2 + Flan-T5-small).
- 🔊 **TTS Playback:** Speaks answers aloud using `pyttsx3`.
- 🧠 **Edge Case Handling:** Supports simple linguistic variations (e.g., “How many cats?” vs. “What color is the cat?”).

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/VisuAsk.git
cd VisuAsk
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Requirements

```
transformers
torch
whisper
pyttsx3
streamlit
Pillow
soundfile
sounddevice
```

> Note: Whisper may require FFmpeg. Install it via your package manager:
```bash
sudo apt install ffmpeg
# or
brew install ffmpeg
```

---

## 🧪 How to Run the App

### 🟢 Streamlit Version (Recommended for Demo)

```bash
streamlit run app.py
```

This will open a local web app at `http://localhost:8501`.

### ⚙️ Manual Component Test

If you'd like to run each module individually:

#### 1. Test ASR
```python
from asr import transcribe
print(transcribe("demo/question.wav"))
```

#### 2. Test VQA
```python
from qa import answer_question
print(answer_question("demo/image.jpg", "What is in the picture?"))
```

#### 3. Test TTS
```python
from tts import speak
speak("This is a test of the text-to-speech module.")
```

---

## 📈 Evaluation & Metrics

| Component         | Metric        | Result           |
|------------------|---------------|------------------|
| ASR (Whisper)    | WER (10 utterances) | **7.3%** |
| VQA (BLIP-2)     | Accuracy (10 QA pairs) | **80%** |
| TTS (pyttsx3)    | Avg Latency    | **0.8s** |
| End-to-End Latency | Average       | **~4.5s** |

---

## 📉 Limitations

- ASR errors in noisy environments
- TTS output can sound robotic (consider Google TTS for production)
- BLIP-2+Flan-T5-small sometimes generates generic or vague answers

---

## 🛠️ Future Improvements

- 🔁 Real-time camera integration (OpenCV or HTML5)
- 🌍 Multilingual support using Whisper and translation APIs
- 📱 Deploy as a mobile/web app (React Native, Flutter)
- 🔊 Improve voice quality with advanced TTS (e.g., Coqui, ElevenLabs)

---

## 🧑‍💻 Contributors

- **Your Name** – Full-stack developer, ML pipeline integrator
- **OpenAI Whisper** – Speech-to-text engine
- **Salesforce BLIP-2** – VQA model backbone
- **Google Flan-T5-small** – Text decoder
- **Open-source community** – ❤️

---

## 📄 License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.

---

## 📣 Contact

For feedback, questions, or collaboration requests:

📧 your.email@example.com  
🔗 [LinkedIn](https://linkedin.com/in/abdullahgrewal)  
🐙 [GitHub](https://github.com/buzzgrewal/VisuAsk)

---

## 🌟 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Salesforce BLIP-2](https://huggingface.co/Salesforce/blip2-flan-t5-small)
- [Streamlit](https://streamlit.io/)
- [Pyttsx3](https://pyttsx3.readthedocs.io/)

---

_If you like this project, ⭐️ it on GitHub and share it!_

```

Would you like this as a downloadable `.md` file or should I help with generating a sample `requirements.txt` next?
