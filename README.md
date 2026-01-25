# InterSystem Caché/IRIS
<i>Este repositório é apenas para estudo visando o desenvolvimento do lado do cliente (client-side) para melhor isolamento de ambiente e deploy</i>

# Requisitos.
- Visual Studio Code.
- InterSystems ObjectScript Extension Pack
- Uma instância (servidor) Caché/IRIS.

## Subindo um ambiente via Docker (Opcional)
Caso não possua uma instância local para teste instalada, utilize o comando abaixo para iniciar um container do IRIS Community:

```bash
docker run --name my-iris -d --publish 1972:1972 --publish 52773:52773 intersystems/iris-community:latest-cd
```

# Configurando ambiente
1. Arquivo de Configuração: Renomeie o arquivo .vscode/settings.example.json para .vscode/settings.json.
2. Conexão: Ajuste o campo objectscript.conn de acordo com as credenciais do seu servidor ou instância.

Exemplo de configuração no arquivo settings.json:
```
"objectscript.conn": {
    "host": "localhost",
    "ns": "USER",
    "https": false,
    "port": 52773,
    "username": "_SYSTEM",
    "password": "SYS",
    "active": true
},
```

# Como funciona a sincronização?
A extensão ObjectScript permite a sincronização direta com o servidor configurado no arquivo de preferências (.vscode/settings.json). Isso abrange os códigos-fonte armazenados no banco de dados (cache.dat/iris.dat).

## Estrutura de Pastas e Mapeamento
O mapeamento segue a convenção e a hierarquia de nomes da plataforma:

- src/: Considerada a raiz para códigos-fonte (.cls, .int, .mac).
    - Exemplo: Se houver uma classe ``Teste.Chamada.cls`` no servidor, ela deve estar localizada em ``src/Teste/Chamada.cls`` neste repositório.

- csp/: Pasta configurada para a sessão Web do namespace.
    - Nota: Se o seu namespace define que os arquivos CSP ficam em /home/meu/csp/, você precisará replicar essa estrutura dentro desta pasta.

A sincronização é realizada automaticamente assim que o arquivo é salvo no editor.

