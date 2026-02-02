import os
import json
import requests
import sys

BRANCH = os.environ["BRANCH"]
X_SECRET = os.environ["X_SECRET"]
BASE_API_CI = os.environ["BASE_API_CI_STAGING"] # Padrão é homologação.
ARQUIVOS_ALTERADOS = os.environ["CHANGED_FILES"]
NAMESPACE = os.environ["NAMESPACE"]
ARRAY_ARQUIVOS_ALTERADOS = ARQUIVOS_ALTERADOS.split("\n")

if BRANCH == "staging":
    BASE_API_CI = os.environ["BASE_API_CI_STAGING"]

if BRANCH == "master":
    BASE_API_CI = os.environ["BASE_API_CI_PROD"]

def main():
    extrairConteudoArquivoAlterado()

def extrairConteudoArquivoAlterado():
    for filename in ARRAY_ARQUIVOS_ALTERADOS:
        if not isExtencaoPermitida(filename):
            continue
        
        isFoiDeletado = (os.path.exists(filename) == False)
        if isFoiDeletado:
            deletarCodigoFonte(filename)
            continue

        conteudo = []
        with open(filename, "r", encoding="utf-8") as file:
            while linha := file.readline():
                conteudo.append(linha.rstrip("\n"))
        
        compilarCodigoFonte(filename, conteudo)

def isExtencaoPermitida(filename):
    permitidas = [".cls", ".mac", ".csp", ".int"]
    _, extencao = os.path.splitext(filename)

    for permitida in permitidas:
        if extencao == permitida:
            return True
        
    return False

def deletarCodigoFonte(filename):
    _, extencao = os.path.splitext(filename)
    body = {
        "namespace": NAMESPACE,
        "source": filename,
        "extension": extencao
    }

    request = requests.delete(BASE_API_CI + "/deletar", json=body, headers={"X-Secret": X_SECRET})
    if request.status_code != 200:
        print(request.text)
        sys.exit(0)

def compilarCodigoFonte(filename, conteudo):
    _, extencao = os.path.splitext(filename)
    body = {
        "namespace": NAMESPACE,
        "source": filename,
        "content": conteudo,
        "extension": extencao
    }

    request = requests.post(BASE_API_CI + "/compilar", json=body, headers={"X-Secret": X_SECRET})
    if request.status_code != 200:
        print(request.text)
        sys.exit(0)

main()