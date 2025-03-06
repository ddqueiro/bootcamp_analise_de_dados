# Pipeline de ETL - Mercado Livre

Este projeto implementa um pipeline de ETL (Extract, Transform, Load) utilizando dados da API pública do Mercado Livre, realizando as seguintes tarefas:

## Tarefas Executadas:

### 1. **Extração de Dados da API do Mercado Livre**
   A primeira etapa do pipeline extrai os dados sobre um termo específico da API pública do Mercado Livre. Um termo de pesquisa como "webcam" é utilizado para coletar informações sobre produtos disponíveis na plataforma.

### 2. **Armazenamento dos Dados em um DataFrame Pandas**
   Após a extração, os dados são armazenados em um `DataFrame` do Pandas, onde as informações são organizadas de forma tabular para facilitar a manipulação.

### 3. **Transformações nos Dados**
   O `DataFrame` passa por diversas transformações, incluindo:
   - Renomeação de colunas para torná-las mais legíveis.
   - Conversão de tipos de dados, remoção de dados nulos e criação de novas colunas, conforme necessário.

### 4. **Salvamento dos Dados em Arquivo CSV**
   Após as transformações, o `DataFrame` é salvo em um arquivo CSV local, que será utilizado em etapas posteriores do pipeline.

### 5. **Envio do Arquivo CSV para um Bucket no Google Cloud Storage**
   O arquivo CSV gerado é enviado para um bucket no Google Cloud Storage, utilizando o cliente da API do Google Cloud Storage.

### 6. **Envio dos Dados para o MongoDB Atlas**
   O arquivo CSV é convertido em coleções e os dados são enviados para um banco de dados no MongoDB Atlas. Essa etapa armazena os dados de produtos da pesquisa de forma não relacional.

### 7. **Armazenamento dos Dados em um Banco de Dados SQL**
   Os dados são também carregados em um banco de dados MySQL, criando a tabela e inserindo as informações extraídas da API do Mercado Livre.

### 8. **Integração com o BigQuery**
   O pipeline conecta o banco de dados SQL no Google Cloud ao BigQuery, enviando os dados para um conjunto de dados chamado `mercado_livre`.

### 9. **Envio do Arquivo CSV para Outro Conjunto de Dados no BigQuery**
   O arquivo CSV é enviado diretamente do Colab para outro conjunto de dados no BigQuery chamado `mercado2`.

### 10. **Integração com o Looker Studio**
   Por fim, o arquivo CSV é integrado a um relatório no Looker Studio, permitindo a visualização e análise dos dados de maneira interativa.

## Requisitos

Certifique-se de que você tenha as seguintes bibliotecas instaladas para que o pipeline funcione corretamente:

```python
pip install mysql.connector
pip install pymongo
pip install google-cloud-storage
pip install google-cloud-bigquery
```

## Configuração de Conexões

### Conexão com o Google Cloud Storage
Certifique-se de que você tenha configurado o acesso ao Google Cloud e criado o bucket no Google Cloud Storage.

### Conexão com o MongoDB Atlas
Substitua a string de conexão do MongoDB Atlas com suas credenciais e a URL do seu cluster.

### Conexão com o MySQL
Substitua os parâmetros de conexão com seu banco de dados MySQL, como `user`, `password`, `host` e `database`.

### Conexão com o BigQuery
Certifique-se de autenticar seu ambiente e configurar o projeto no Google Cloud para enviar dados ao BigQuery.

## Execução do Pipeline

### 1. Extração dos Dados
O pipeline inicia com a extração de dados da API do Mercado Livre, que são armazenados em um DataFrame Pandas.

### 2. Transformação dos Dados
Realize as transformações necessárias nos dados, como renomeação de colunas e alteração de tipos de dados.

### 3. Carregamento dos Dados

- **CSV**: O arquivo CSV gerado é salvo localmente e enviado para o Google Cloud Storage.
- **MongoDB**: Os dados são convertidos em coleções e enviados para o MongoDB Atlas.
- **MySQL**: Os dados são inseridos em uma tabela no banco de dados MySQL.
- **BigQuery**: Os dados são enviados para dois conjuntos de dados no BigQuery.
- **Looker Studio**: O arquivo CSV é integrado com o Looker Studio para visualização interativa.

## Considerações Finais sobre o projeto

Este pipeline é uma implementação completa de ETL que envolve múltiplos serviços do Google Cloud e integrações com bancos de dados SQL e NoSQL. Certifique-se de configurar corretamente as credenciais e os acessos para que todas as etapas possam ser executadas com sucesso.
