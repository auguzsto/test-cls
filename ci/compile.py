import os
import json

ARQUIVOS_ALTERADOS = os.environ["CHANGED_FILES"]
ARRAY_ARQUIVOS_ALTERADOS = ARQUIVOS_ALTERADOS.split("\n")

def isExtencaoPermitida(filename):
    permitidos = [".cls", ".mac", ".csp", ".int"]
    _, extencao = os.path.splitext(filename)

    for permitido in permitidos:
        if extencao == permitido:
            return True
        
    return False

for filename in ARRAY_ARQUIVOS_ALTERADOS:
    conteudo = []
    
    with open(filename, "r", encoding="utf-8") as file:
        if not isExtencaoPermitida(filename):
            continue
        while linha := file.readline():
            conteudo.append(linha.rstrip("\n"))

    conteudoSerializado = json.dumps(conteudo, ensure_ascii=False, indent=2)
    print(conteudoSerializado)