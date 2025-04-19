# src/summarize_bart.py
from transformers import pipeline
import textwrap

# Initialize once (global)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_words=500):
    words = text.split()
    return [' '.join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

def summarize_text_bart(transcription):
    chunks = chunk_text(transcription)

    summaries = summarizer(
        chunks, max_length=130, min_length=30, do_sample=False
    )

    final_summary = "\n".join([
        textwrap.fill(s['summary_text'], width=100) for s in summaries
    ])

    return final_summary