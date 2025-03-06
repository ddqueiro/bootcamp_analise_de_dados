# Projeto de Consultas e Análise de Dados com MySQL e Pandas

## Descrição do Projeto

Este projeto consiste em um conjunto de consultas SQL realizadas em um banco de dados de locadora de veículos, com o objetivo de realizar diversas análises sobre o comportamento dos clientes e dos carros alugados. As consultas são executadas via Python usando a biblioteca mysql-connector-python para se conectar ao banco de dados, além de utilizar o pandas para armazenar e visualizar os resultados das consultas.

## Tecnologias Utilizadas

MySQL: Banco de dados para armazenar informações sobre os clientes, carros e aluguéis.
Python: Linguagem de programação para realizar as consultas SQL e manipulação dos dados.
Pandas: Biblioteca para armazenar os resultados das consultas em DataFrames e exibir as informações de forma estruturada.
mysql-connector-python: Biblioteca para realizar a conexão com o banco de dados MySQL a partir do Python.
curl: Utilizado para exibir o IP público da máquina, servindo para demonstrar o acesso remoto ao banco de dados.

Como Executar
Instalação das Dependências Para instalar as bibliotecas necessárias, execute o seguinte comando:

```python
!pip install mysql-connector-python
```

## Conectar ao Bando de Dados:

O banco de dados MySQL é acessado utilizando as credenciais e o IP de acesso especificados nas variáveis do script:

```python

host = '34.70.26.188'  # Endereço do banco de dados remoto
user = 'root'  # Usuário do banco
password = ''  # Senha do banco
database = 'locadora'  # Nome do banco de dados
```

## Executando Consultas SQL:

 O projeto permite realizar consultas SQL interativas. O usuário deve informar a query e o nome da tabela do pandas onde os resultados serão armazenados:

A função consulta() executa consultas SQL e armazena os resultados no pandas DataFrame.

# Exemplo de consulta:

```python
SELECT DISTINCT c.cidade
FROM cliente c
WHERE c.codcliente IN (SELECT a.codcliente FROM aluguel a);
```

Esta consulta retorna uma lista de cidades em que há clientes que realizaram aluguéis.
Executando Comandos DDL A função ddl() permite executar comandos DDL (Data Definition Language) no banco de dados, como a criação ou alteração de tabelas:

```python
comando = input('Informe o comando DDL: ')  # Exemplo: CREATE TABLE ...
```

## Consultas Utilizadas Algumas das principais consultas realizadas incluem:

Listar as cidades com clientes que alugaram carros.
Encontrar os modelos de carros mais caros que a média.
Listar clientes que alugaram carros da marca Ford.
Obter os carros alugados apenas por clientes de São Paulo.
Encontrar as datas mais movimentadas em termos de aluguéis.
E muitas outras consultas para análise do comportamento de clientes e carros.

Exemplo de Execução de Consulta
Consulta: Cidades com clientes que alugaram carros Query:

```python
SELECT DISTINCT c.cidade FROM cliente c WHERE c.codcliente IN (SELECT a.codcliente FROM aluguel a);
```

Tabela resultante:

```bash
cidade
---------------
Duque de Caxias
Niterói
São Paulo
```

Consulta: Modelos de carros mais caros que a média Query:


```bash
SELECT modelo FROM carro WHERE valor > (SELECT AVG(valor) FROM carro);
```

Tabela resultante:

```bash
modelo
---------------
Argo
Onix
Polo
```

## Requisitos

MySQL Server configurado com um banco de dados acessível remotamente.
Python (versão 3.x) instalado com as bibliotecas mysql-connector-python e pandas.

# Cnsiderações Finais

Este projeto oferece uma forma interativa de realizar consultas em um banco de dados MySQL, armazenar e analisar os dados utilizando o pandas, facilitando a extração de insights valiosos sobre o comportamento dos clientes e dos carros da locadora.
