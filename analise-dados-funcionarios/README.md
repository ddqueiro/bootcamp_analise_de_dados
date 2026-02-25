
# Análise e Tratamento de Dados de Funcionários

Este projeto realiza a exploração, limpeza, transformação e análise de métricas de uma base de dados de funcionários, utilizando a biblioteca **Pandas**. O objetivo é organizar e analisar informações sobre os funcionários, gerar insights e preparar o dataset para análises futuras.

## Estrutura do Projeto

``` bash
analise-dados-funcionarios
│
├─ notebooks/
│ └─ analise_dados_funcionarios.ipynb # Notebook com toda a exploração e análises
│
├─ output/
│ └─ df_limpo.csv # Dataset limpo exportado
│
├─ README.md # Descrição completa do projeto

```

## Importação de Bibliotecas

- pandas – manipulação e análise de dados  
- datetime (via Pandas) – manipulação de datas  

## Exploração Inicial

- Análise da estrutura do dataset (shape, info, head)  
- Identificação de valores ausentes  
- Detecção de padrões inconsistentes nos dados  

## Tratamento de Dados

- Limpeza e padronização de colunas  
- Preenchimento ou substituição de valores ausentes  
- Atualização de departamentos (ex.: "TI" → "Tecnologia da Informação")  

## Engenharia de Atributos

Criação de novas colunas derivadas:  

- Tempo na Empresa  
- Categoria de Salário  
- Desempenho Simplificado  
- Idade em 5 Anos  

## Análises e Métricas

- Total de registros e registros completos  
- Média salarial e substituição de valores ausentes  
- Identificação do salário mais alto e do funcionário correspondente  
- Contagem de funcionários por departamento e categoria salarial  
- Idade média por departamento e cargos únicos  
- Seleção dos top 5 funcionários por tempo de empresa e idade  
- Visualizações rápidas para análise de métricas  

## Exportação do Dataset

- Remoção de registros incompletos  
- Exportação do dataset limpo em arquivo CSV para uso futuro (output/funcionarios_limpo.csv)  

## Estrutura do Dataset

Exemplo de colunas do dataset:  

- Nome  
- Departamento  
- Cargo  
- Salario  
- Data de Admissao  
- Idade  

Colunas derivadas:  

- Tempo na Empresa  
- Categoria de Salário  
- Desempenho Simplificado  
- Idade em 5 Anos  

## Como Utilizar

1. Clonar o repositório:  

```bash
git clone <URL_DO_REPOSITORIO>
```

2.Instalar as bibliotecas necessárias:

```bash
pip install pandas
```

3.Carregar o dataset no notebook:

```python
import pandas as pd
df = pd.read_csv("data/funcionarios.csv")
```

4.Executar etapas de exploração, limpeza, engenharia de atributos e análises.

5.Exportar dataset limpo:

```python
df.to_csv("output/df_limpo.csv", index=False)
```
