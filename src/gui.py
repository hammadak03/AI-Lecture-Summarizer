# src/gui.py
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from .whisper_transcribe import transcribe_audio_whisper
from .summarize_bart import summarize_text_bart
import os

class LectureSummarizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Lecture Summarizer")

        # File selection
        self.file_label = tk.Label(root, text="Select Audio File:")
        self.file_label.pack(pady=(10, 0))

        self.select_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.select_button.pack()

        # Transcription Box
        self.transcription_box = scrolledtext.ScrolledText(root, height=10, width=80, wrap=tk.WORD)
        self.transcription_box.pack(pady=10)
        self.transcription_box.insert(tk.END, "📝 Transcription will appear here...")
        self.transcription_box.config(state=tk.DISABLED)

        # Summary Box
        self.summary_box = scrolledtext.ScrolledText(root, height=10, width=80, wrap=tk.WORD)
        self.summary_box.pack(pady=10)
        self.summary_box.insert(tk.END, "📌 Summary will appear here...")
        self.summary_box.config(state=tk.DISABLED)

        # Action Button
        self.summarize_button = tk.Button(root, text="Transcribe & Summarize", command=self.process_audio)
        self.summarize_button.pack(pady=10)

        self.audio_path = ""

    def browse_file(self):
        filetypes = [("Audio files", "*.wav *.mp3 *.m4a"), ("All files", "*.*")]
        self.audio_path = filedialog.askopenfilename(title="Select Audio File", filetypes=filetypes)

        if self.audio_path:
            self.file_label.config(text=f"Selected: {os.path.basename(self.audio_path)}")

    def process_audio(self):
        if not self.audio_path:
            messagebox.showerror("Error", "Please select an audio file first.")
            return

        self.transcription_box.config(state=tk.NORMAL)
        self.summary_box.config(state=tk.NORMAL)
        self.transcription_box.delete("1.0", tk.END)
        self.summary_box.delete("1.0", tk.END)
        self.transcription_box.insert(tk.END, "🔄 Transcribing...")
        self.root.update()

        try:
            transcription = transcribe_audio_whisper(self.audio_path)
            self.transcription_box.delete("1.0", tk.END)
            self.transcription_box.insert(tk.END, transcription)

            summary = summarize_text_bart(transcription)
            self.summary_box.delete("1.0", tk.END)
            self.summary_box.insert(tk.END, summary)

        except Exception as e:
            messagebox.showerror("Error", str(e))

        self.transcription_box.config(state=tk.DISABLED)
        self.summary_box.config(state=tk.DISABLED)