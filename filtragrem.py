import re

# Arquivos de entrada e saída
TRANSCRICAO_FILE = "transcricao.txt"
DICIONARIO_FILE = "dicionario.txt"
SAIDA_FILE = "frases_filtradas.txt"

# 1. Lê o dicionário de palavras
with open(DICIONARIO_FILE, "r", encoding="utf-8") as f:
    palavras = [linha.strip() for linha in f if linha.strip()]

# Escapa as palavras para uso seguro no regex
padrao_palavras = r"\b(" + "|".join(re.escape(p) for p in palavras) + r")\b"

# 2. Lê a transcrição
with open(TRANSCRICAO_FILE, "r", encoding="utf-8") as f:
    texto = f.read()

# 3. Divide em frases (considera ., ?, ! como delimitadores)
frases = re.split(r'(?<=[.!?])\s+', texto)

# 4. Filtra frases que contenham qualquer palavra do dicionário
frases_filtradas = [frase for frase in frases if re.search(padrao_palavras, frase, flags=re.IGNORECASE)]

# 5. Salva resultado
with open(SAIDA_FILE, "w", encoding="utf-8") as f:
    for frase in frases_filtradas:
        f.write(frase.strip() + "\n")

print(f"✅ {len(frases_filtradas)} frases encontradas e salvas em '{SAIDA_FILE}'")
