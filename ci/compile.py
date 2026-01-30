import os
import json

ARQUIVOS_ALTERADOS = os.environ["CHANGED_FILES"]
ARRAY_ARQUIVOS_ALTERADOS = ARQUIVOS_ALTERADOS.split("\n")

def main():
    extrairConteudoArquivoAlterado()

def extrairConteudoArquivoAlterado():
    for filename in ARRAY_ARQUIVOS_ALTERADOS:
        conteudo = []
        
        with open(filename, "r", encoding="utf-8") as file:
            if not isExtencaoPermitida(filename):
                continue
            while linha := file.readline():
                conteudo.append(linha.rstrip("\n"))

    conteudoSerializado = json.dumps(conteudo, ensure_ascii=False, indent=2)

    # Futuramento esse conteúdo será enviado para um API para realizar o deploy
    # no servidor.
    print(conteudoSerializado)

def isExtencaoPermitida(filename):
    permitidas = [".cls", ".mac", ".csp", ".int"]
    _, extencao = os.path.splitext(filename)

    for permitida in permitidas:
        if extencao == permitida:
            return True
        
    return False

main()