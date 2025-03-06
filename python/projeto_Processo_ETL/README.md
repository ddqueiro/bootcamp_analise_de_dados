### Projeto de ETL - Mercado Livre
Este projeto consiste na criação de um processo completo de ETL utilizando a API pública do Mercado Livre. O objetivo é realizar a extração, transformação e carga de dados em diversas plataformas e ferramentas, como Google Cloud, MongoDB Atlas, SQL e BigQuery.

## Tarefas Realizadas:

## 1. Extração de Dados
Utilizamos a API pública do Mercado Livre para buscar todos os resultados de uma consulta sobre um termo específico.
Os dados são extraídos em formato JSON e processados para gerar informações relevantes sobre os produtos, como título, preço, link, condição e categoria.

## 2. Armazenamento em DataFrame
Após a extração, os dados são armazenados em um DataFrame do Pandas para facilitar a transformação e manipulação.

## 3. Transformação de Dados
Realizamos algumas transformações nos dados:
Mudança nos nomes das colunas.
Tratamento de valores nulos e tipos de dados.
Criação de novas colunas, se necessário.

## 4. Salvamento em CSV
Os dados transformados são salvos em um arquivo CSV local para uso posterior.

## 5. Envio para Google Cloud Storage (GCS)
O arquivo CSV gerado é enviado para um bucket do Google Cloud Storage (GCS) com o nome mercadolivre_seunome.

## 6. Envio para MongoDB Atlas
O arquivo CSV é convertido para coleções e enviado para o banco de dados MongoDB hospedado no MongoDB Atlas.

## 7. Criação e Inserção no Banco SQL
Criamos um banco de dados chamado mercado em uma instância SQL e inserimos os dados provenientes do arquivo CSV na tabela webcam.

## 8. Conexão com BigQuery
Estabelecemos uma conexão entre o banco de dados SQL e o BigQuery, enviando os dados do banco para um conjunto de dados chamado mercado_livre.
## 9. Envio de Arquivo CSV para BigQuery
O arquivo CSV gerado no Colab é enviado para um conjunto de dados chamado mercado2 no BigQuery.

## 10. Conexão com Looker Studio
Estabelecemos a conexão entre o BigQuery e o Looker Studio, permitindo a criação de relatórios baseados nos dados processados.

## Requisitos
Google Cloud Storage
MongoDB Atlas
SQL Database (MySQL)
Google BigQuery
Looker Studio
Bibliotecas Python:
pandas
requests
mysql.connector
pymongo
google-cloud-storage
google-cloud-bigquery


## Como Rodar o Projeto

1. Instale as bibliotecas necessárias:

```python
!pip install mysql.connector
!pip install pymongo
!pip install google-cloud-storage
!pip install google-cloud-bigquery
Execute cada célula do notebook conforme a sequência do processo de ETL.
```

2. Certifique-se de configurar corretamente o seu projeto no Google Cloud e as credenciais de acesso ao MongoDB Atlas.

Após o processamento, os dados serão enviados para os destinos especificados (GCS, MongoDB Atlas, SQL e BigQuery).

Conecte os dados no Looker Studio para gerar relatórios interativos.

Conclusão
Este projeto fornece um pipeline completo de ETL utilizando ferramentas e serviços da Google Cloud, MongoDB Atlas e Looker Studio. Ele permite realizar a extração de dados de uma API pública, transformá-los, e enviá-los para diversas plataformas para análise e visualização.