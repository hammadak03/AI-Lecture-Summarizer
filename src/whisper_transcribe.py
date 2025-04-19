# src/whisper_transcribe.py
import whisper

def transcribe_audio_whisper(audio_path):
    model = whisper.load_model("base")  # options: tiny, base, small, medium, large
    print("🔹 Transcribing using Whisper (this may take a while)...")
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    audio_path = "audio_files/sample.wav"  # Change if needed
    transcription = transcribe_audio_whisper(audio_path)
    print("\n📝 Transcription:\n")
    print(transcription)