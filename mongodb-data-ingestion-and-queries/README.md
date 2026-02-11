# 📊 Integração MongoDB Atlas + Google Colab

Este projeto demonstra um pipeline de dados completo: desde a extração de dados brutos de planilhas até à análise avançada. O repositório está estruturado para separar o processo de carga (ETL) da análise exploratória.

## Estrutura do Projeto

O repositório está organizado nas seguintes pastas e arquivos:

### 1. ingestao_dados

Scripts responsáveis pela carga inicial:

* Leitura de arquivos CSV vindos do Google Sheets.
* Tratamento inicial de dados com **Pandas**.
* Conexão e envio de dados para o **MongoDB Atlas** usando `insert_many()`.

### 2. consultas_mongodb

Scripts focados em análise e extração de dados:

* Execução de queries NoSQL para filtragem de dados.
* Conversão de resultados (cursores) para **DataFrames**.

### 3.  requirements.txt

Arquivo com as dependências do projeto: `pymongo` e `pandas`.

---

## Tecnologias Utilizadas

* **Python**: Linguagem principal.
* **Pandas**: Manipulação e análise de dados.
* **PyMongo**: Driver oficial para integração com MongoDB.
* **MongoDB Atlas**: Banco de dados NoSQL gerido na nuvem.

---

## Como Instalar e Executar

### Opção A: No Google Colab(Nuvem)

No Colab, você instala as bibliotecas diretamente em uma célula de código:

```python
# Instalação direta no notebook
!pip install pymongo pandas
```

### Opção B: Ambiente Local(PC/VS Code)

Se estiver rodando no seu computador, utilize o arquivo requirements.txt para instalar as dependências:

No seu terminal ou prompt de comando:

```bash
pip install -r requirements.txt

```

## Configuração da Conexão

Em ambos os ambientes, a conexão com o banco de dados segue o mesmo padrão:

```python
from pymongo import MongoClient
import pandas as pd

# Substitua USUARIO e SENHA pelas suas credenciais do Atlas

uri = "mongodb+srv://USUARIO:SENHA@cluster0.gchy6.mongodb.net/"
client = MongoClient(uri)
db = client['financeiro']

```

## Exemplos de Consultas

Para extrair os dados e transformá-los em tabelas (DataFrames):

```python
import pandas as pd

# 1. Filtrar Clientes de São Paulo
query_sp = {'UF': "SÃO PAULO"}
df_sp = pd.DataFrame(list(db.cliente.find(query_sp)))

# 2. Filtrar Fornecedores Pessoa Física
query_pf = {'Tipo Pessoa': "Pessoa Física"}
df_pf = pd.DataFrame(list(db.fornecedor.find(query_pf)))

```

## Segurança e Boas Práticas

Aviso: Por segurança, nunca deixe sua senha exposta no código final ou no GitHub. No Colab, utilize o ícone de chave (Secrets) para gerenciar sua string de conexão com segurança.

## Feito por Dannyelly Queiroz

Projeto desenvolvido para fins de estudo em Engenharia e Análise de Dados.
