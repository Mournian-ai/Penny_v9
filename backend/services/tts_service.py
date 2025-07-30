import subprocess
from pathlib import Path
from uuid import uuid4
from shared.event_bus import event_bus

VOICE_MODEL = "en_US-amy-low.onnx"  # Adjust as needed


def speak(text: str):
    """Use piper TTS to speak the given text."""
    try:
        tmp = Path("/tmp") / f"piper_{uuid4().hex}.wav"
        subprocess.run([
            "piper",
            "-m",
            VOICE_MODEL,
            "-f",
            str(tmp),
            "-t",
            text,
        ], check=True)
        # Play via ffplay to VAC or audio device
        subprocess.run(["ffplay", "-nodisp", "-autoexit", str(tmp)], check=True)
        tmp.unlink(missing_ok=True)
        event_bus.add_log(f"Spoke: {text}")
    except Exception as e:
        event_bus.add_log(f"TTS error: {e}")
