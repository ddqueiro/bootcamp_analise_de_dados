# Projeto de Integração MongoDB com Google Colab

Este projeto realiza a integração entre o MongoDB e Google Colab, com o objetivo de importar dados de planilhas Google (formatos CSV) para coleções do MongoDB, realizar consultas específicas e manipular os dados utilizando o pandas.

## 🚀 Tecnologias Utilizadas

- **Python**
- **Pandas**
- **PyMongo**
- **MongoDB Atlas**
- **Google Sheets (CSV)**

---

## 📌 Requisitos

Antes de executar o código, instale as dependências necessárias:

```python
!pip install pymongo
 ```

## Configuração do MongoDB
A conexão com o MongoDB é realizada usando a URI do MongoDB Atlas:

```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://danny:102030@cluster0.gchy6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['financeiro']
 ```

## Importação de Dados
O código lê planilhas do Google Sheets no formato CSV e insere os dados no MongoDB:

```python
import pandas as pd

fornecedor = pd.read_csv('<link_do_google_sheet>')
fornecedor = fornecedor.to_dict(orient='records')
colecao_fornecedor = db['fornecedor']
colecao_fornecedor.insert_many(fornecedor)
 ```
O mesmo processo é aplicado para outras coleções: recebimento, cliente, pagamento e banco.


## Consultas no MongoDB
1️⃣ Filtrar clientes de São Paulo:

```python
query = {'UF': "SÃO PAULO"}
cursor = colecao_cliente.find(query)
cidade_sp = pd.DataFrame(list(cursor))
 ```

 2️⃣ Filtrar fornecedores do tipo Pessoa Física:

```python
 query = {'Tipo Pessoa': "Pessoa Física"}
cursor = colecao_fornecedor.find(query)
pessoa_fisica = pd.DataFrame(list(cursor))
 ```

 3️⃣ Listar todos os recebimentos:
```python
 cursor = colecao_recebimento.find()
colecao_recebimentos = pd.DataFrame(list(cursor))
 ```

4️⃣ Listar todos os pagamentos:
 ```python
 cursor = colecao_pagamento.find()
colecao_pagamentos = pd.DataFrame(list(cursor))
 ```


 ## Como Executar:
1.Instale o pacote Pymong:

 ```python

 !pip install pymongo
```

2.Configure sua string de conexão MongoDB Atlas.

3.Carregue os dados CSV e insira no banco de dados.

4.Execute as consultas desejadas e visualize os resultados em DataFrames.
