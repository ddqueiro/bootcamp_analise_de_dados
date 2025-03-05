#  Processamento e Upload de Dados no Google Cloud
Este projeto tem como objetivo realizar o processamento de dados inconsistentes de uma planilha CSV, tratar esses dados, e, por fim, fazer o upload para o Google Cloud Storage. O processo inclui a limpeza dos dados e a conversão de informações para o formato adequado.

## Funcionalidades
Carregamento de Dados: O código carrega um arquivo CSV contendo dados inconsistentes de uma URL externa usando o Pandas.

Conversão para Dicionários: Converte o DataFrame original para uma lista de dicionários.

Limpeza de Dados: O código realiza a limpeza dos dados, removendo valores inválidos, como NaN e strings vazias, e transforma os valores para os tipos corretos (como float para salario e int para idade).

Criação de Novo DataFrame: Com os dados tratados, o código recria um DataFrame a partir dos dados limpos.

Autenticação e Upload no Google Cloud: O script faz a autenticação no Google Cloud, configura o projeto e realiza o upload do DataFrame tratado para um bucket no Google Cloud Storage.

## Como Funciona
1. Leitura dos Dados

A função pd.read_csv é utilizada para carregar o arquivo CSV com dados inconsistentes para um DataFrame.

```python
tabela = pd.read_csv('https://storage.googleapis.com/cloud_projeto/dados-brutos/dados_inconsistentes%20-%20dados_inconsistentes.csv')
```
## 2. Conversão para Listas de Dicionários
Os dados do DataFrame são convertidos para uma lista de dicionários, onde cada dicionário representa uma linha da tabela original.

## 3. Limpeza de Dados
São feitas verificações e conversões para garantir que os dados estejam em um formato adequado para análise.

```python
if (lista_nomes[i] != '' and lista_nomes[i] != 'nan' and
    lista_idade[i] != '' and lista_idade[i] != 'nan' and
    lista_salario[i] != '' and lista_salario[i] != 'nan' and
    lista_cargo[i] != '' and lista_cargo[i] != 'nan' and
    lista_departamento[i] != '' and lista_departamento[i] != 'nan'):

```

## 4. Criação do Novo DataFrame
Após o processamento, os dados tratados são armazenados em um novo DataFrame df_tratado.

```python
df_tratado = pd.DataFrame(lista_dicionarios)
```

## 5. Upload para o Google Cloud Storage
O código autentica o usuário no Google Cloud e faz o upload do arquivo CSV tratado para o Google Cloud Storage.

```python
from google.cloud import storage
client = storage.Client()
bucket_name = 'cloud_projeto'
bucket = client.bucket(bucket_name)
df_tratado.to_csv('dadostratados.csv', index=False)
destination_blob_name = 'dados-tratados/tratados.csv'
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename('dadostratados.csv')
```

## Pré-Requisitos
Python 3.x

## Bibliotecas:
pandas
google-cloud-storage
## Instalação das Dependências:

Execute o seguinte comando para instalar as dependências necessárias:

```python
pip install pandas google-cloud-storage
```