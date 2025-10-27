import queue
import sys
import time
import numpy as np
import sounddevice as sd
import soundfile as sf
import tempfile
import whisper

SAMPLE_RATE = 16000
CHANNELS = 1
DURATION_LIMIT = 15  # seconds max per utterance

def record_to_wav(seconds=DURATION_LIMIT, samplerate=SAMPLE_RATE, channels=CHANNELS):
    print(f"🎤 Recording for up to {seconds}s… press Ctrl+C to stop early.")
    q = queue.Queue()

    def callback(indata, frames, time_info, status):
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())

    with sd.InputStream(samplerate=samplerate, channels=channels, callback=callback):
        frames = []
        start = time.time()
        try:
            while time.time() - start < seconds:
                frames.append(q.get())
        except KeyboardInterrupt:
            pass

    audio = np.concatenate(frames, axis=0)
    # Write to a temp WAV
    wav_path = tempfile.mktemp(suffix=".wav")
    sf.write(wav_path, audio, samplerate)
    return wav_path

def transcribe_whisper(model_size="small", language=None):
    # language=None lets Whisper auto-detect. Or set like "hi", "en", "fr", etc.
    print(f"⏳ Loading Whisper model: {model_size}")
    model = whisper.load_model(model_size)  # uses CPU if no GPU
    wav_path = record_to_wav()

    print("🧠 Transcribing…")
    result = model.transcribe(wav_path, language=language)  # or remove language to auto-detect
    print("✅ Transcript:", result["text"].strip())

if __name__ == "__main__":
    # Options: tiny, base, small, medium, large (bigger = more accurate + slower)
    # For Macs without GPU, "base" or "small" are good starts.
    transcribe_whisper(model_size="small", language="en")
