# Configuração

### Secrets
Adicionar as secrets abaixo no action do repositório.

- BASE_API_CI_PROD
    - Descrição: URL da API que irá executar a compilação (PRODUÇÃO).
    - Exemplo: https://api/v1/exemplo

- BASE_API_CI_STAGING
    - Descrição: URL da API que irá executar a compilação (HOMOLOGAÇÃO).
    - Exemplo: https://api/v1/exemplo

- NAMESPACE
    - Descrição: Namespace do repositório.
    - Exemplo: USER

- X_SECRET
    - Descrição: Segredo (chave) para requisição.