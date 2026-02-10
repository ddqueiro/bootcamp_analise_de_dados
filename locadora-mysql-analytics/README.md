
# Locadora MySQL Analytics

Este repositório contém códigos para **consultas e análises de dados de uma locadora de veículos** utilizando **MySQL** e **Python (pandas + mysql-connector-python)**. O foco é extrair informações de clientes, carros, aluguéis e marcas, realizando análises detalhadas de consumo, alugueis e estatísticas gerais.

---

## Estrutura do Projeto

```
locadora-mysql-analytics/
│
├── ingestion/           # Código para conexão e ingestão de dados do MySQL
│   └── mysql_queries.py # Funções para executar queries e retornar DataFrames
│
├── consultas/           # Consultas SQL para análises específicas
│   └── analysis.ipynb   # Notebook com todas as consultas e visualizações
│
└── README.md            # Este arquivo
```

---

## Tecnologias Utilizadas

- **Python 3**
- **pandas**: manipulação e análise de dados
- **mysql-connector-python**: conexão com banco MySQL
- **MySQL**: banco de dados relacional

---

## Instalação

Instale o pacote MySQL connector:

```bash
pip install mysql-connector-python pandas
```

---

## Conexão com o Banco

Configure a conexão com seu banco MySQL:

```python
import mysql.connector
import pandas as pd

user = 'root'
password = ''
database = 'locadora'
host = 'SEU_HOST_AQUI' #host é o ip

def consulta(query, tabela):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        globals()[tabela] = pd.DataFrame(result, columns=cursor.column_names)
        display(globals()[tabela])
    finally:
        cursor.close()
        connection.close()
```

---

## Funcionalidades

O código permite:

- Listar todos os clientes, carros, aluguéis e marcas  
- Filtrar clientes por cidade, estado, sexo ou estado civil  
- Calcular valores total e médio de carros  
- Contar aluguéis por cliente e por carro  
- Consultas avançadas com `JOIN`, `LEFT JOIN`, `GROUP BY` e `HAVING`  
- Identificar clientes que alugaram mais de um carro  
- Agrupar resultados por data, cidade ou marca

---

## Estrutura das Tabelas

- **cliente**: codcliente, nome, cidade, sexo, estado, estadocivil  
- **carro**: codcarro, codmarca, modelo, valor  
- **aluguel**: codaluguel, codcliente, codcarro, data_aluguel  
- **marca**: codmarca, marca  

---

## Autor

- Criado por Dannyelly Queiroz, desenvolvido para análise de locadora de veículos com MySQL e Python.