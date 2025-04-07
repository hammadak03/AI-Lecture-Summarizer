import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_to_wav(audio_path, save_path="converted/converted.wav"):
    """Converts audio (mp3/m4a) to wav format for SpeechRecognition."""
    audio = AudioSegment.from_file(audio_path)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    audio.export(save_path, format="wav")
    return save_path

def transcribe_audio(wav_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, could not understand the audio."
    except sr.RequestError as e:
        return f"Error with Google API: {e}"
