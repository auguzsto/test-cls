import os
import json

ARQUIVOS_ALTERADOS = os.environ["CHANGED_FILES"]
ARRAY_ARQUIVOS_ALTERADOS = ARQUIVOS_ALTERADOS.split("\n")

for filename in ARRAY_ARQUIVOS_ALTERADOS:
    conteudo = []
    with open(filename, "r", encoding="utf-8") as file:
        while linha := file.readline():
            conteudo.append(linha.rstrip("\n"))
    conteudoSerializado = json.dumps(conteudo, ensure_ascii=False, indent=2)
    print(conteudoSerializado)