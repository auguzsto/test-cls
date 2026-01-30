import os
import json
import requests
import sys

BASE_API_COMPILAR = os.environ["BASE_API_COMPILAR"]
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

    #conteudoSerializado = json.dumps(conteudo, ensure_ascii=False, indent=2)

    # Futuramento esse conteúdo será enviado para um API para realizar o deploy
    # no servidor.
    #print(conteudoSerializado)
    compilarCodigoFonte(filename, conteudo)

def isExtencaoPermitida(filename):
    permitidas = [".cls", ".mac", ".csp", ".int"]
    _, extencao = os.path.splitext(filename)

    for permitida in permitidas:
        if extencao == permitida:
            return True
        
    return False

def compilarCodigoFonte(filename, conteudo):
    body = {
        "namespace": "USER",
        "source": filename,
        "content": conteudo
    }

    request = requests.post(BASE_API_COMPILAR, json=body)
    if request.status_code != 200:
        print(request.text)
        sys.exit(0)

main()