import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_audio_to_wav(audio_path):
    """
    Converts audio file to WAV format if needed (e.g., from mp3).
    Returns the path to the .wav file.
    """
    if audio_path.lower().endswith(".wav"):
        return audio_path
    
    sound = AudioSegment.from_file(audio_path)
    wav_path = os.path.splitext(audio_path)[0] + ".wav"
    sound.export(wav_path, format="wav")
    return wav_path

def speech_to_text(audio_path):
    """
    Converts a speech audio file to text using Google's Speech Recognition API.
    """
    recognizer = sr.Recognizer()
    wav_path = convert_audio_to_wav(audio_path)

    with sr.AudioFile(wav_path) as source:
        print("🎧 Listening to audio...")
        audio_data = recognizer.record(source)

        print("🧠 Converting speech to text...")
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "⚠️ Could not understand audio."
        except sr.RequestError:
            return "⚠️ Could not connect to speech recognition service."

# Test script
if __name__ == "__main__":
    audio_file = "audio_files/sample.m4a"  # Path to your audio file
    transcript = speech_to_text(audio_file)
    print("📝 Transcript:\n", transcript)