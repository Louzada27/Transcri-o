import whisper
import os

# Caminho manual pro ffmpeg.exe
FFMPEG_PATH = r"C:\Users\20221si014\Downloads\trasncrição\ffmpeg.exe"

# Faz o Python saber onde está o ffmpeg
os.environ["PATH"] = os.path.dirname(FFMPEG_PATH) + os.pathsep + os.environ["PATH"]

VIDEO_PATH = "The boondocks 1Temporada Ep2 (Dublado PT-BR).mp3"
MODEL_SIZE = "base"

print(f"Carregando modelo Whisper ({MODEL_SIZE})...")
model = whisper.load_model(MODEL_SIZE)

print("Transcrevendo vídeo...")
result = model.transcribe(VIDEO_PATH, language="pt")

with open("transcricao.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("✅ Transcrição salva em transcricao.txt")
