import os
from src.whisper_transcribe import transcribe_audio_whisper
from src.summarize_bart import summarize_text_bart

TRANSCRIPTION_PATH = "output/transcription.txt"
SUMMARY_PATH = "output/summary.txt"

def clear_file(filepath):
    open(filepath, 'w', encoding='utf-8').close()

def save_text(text, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    print("🔹 AI Lecture Summarizer")
    
    audio_path = input("📂 Enter the path to the audio file: ").strip()
    
    if not os.path.exists(audio_path):
        print("❌ Audio file not found.")
        return

    print("\n🧹 Clearing previous outputs...")
    clear_file(TRANSCRIPTION_PATH)
    clear_file(SUMMARY_PATH)

    print("\n🔊 Transcribing audio...")
    transcription = transcribe_audio_whisper(audio_path)
    print("\n📝 Transcription Complete:\n")
    print(transcription[:500] + "..." if len(transcription) > 500 else transcription)
    save_text(transcription, TRANSCRIPTION_PATH)

    print("\n🧠 Summarizing transcript using BART...")
    summary = summarize_text_bart(transcription)
    print("\n📌 Final Summary:\n")
    print(summary)
    save_text(summary, SUMMARY_PATH)

    print("\n✅ Done! Transcript and summary saved to output/")

if __name__ == "__main__":
    main()
