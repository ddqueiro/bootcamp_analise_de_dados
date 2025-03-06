# Análise de Dados de Funcionários com Pandas

Este projeto tem como objetivo analisar uma base de dados de funcionários utilizando a biblioteca **pandas** para responder a diversas perguntas sobre os dados. As análises incluem tratamento de valores ausentes, manipulação de colunas, estatísticas descritivas e categorização de informações.

## 📂 Dataset

A base de dados contém informações sobre funcionários, incluindo idade, salário, cargo, departamento, data de contratação e avaliação de desempenho. O conjunto de dados pode ser acessado no seguinte link:

🔗 [Download do CSV](https://docs.google.com/spreadsheets/d/e/2PACX-1vSpCW9yMoUMQ4tknj5Lg_TYVfIC3P9KoVPPqlJKsBu2HzGaC579yCp9Ohxni2ncY-xyLfugXan9K6yf/pub?gid=636707205&single=true&output=csv)

## 📌 Questões a serem respondidas na ánalise:

1. Quantos registros existem na base de dados?
2. Quantos registros têm informações completas (sem valores ausentes)?
3. Substituir os valores ausentes na coluna **Salário** pela média dos salários e exibir a nova média.
4. Substituir todos os valores **"TI"** na coluna **Departamento** por **"Tecnologia da Informação"**.
5. Qual é o salário mais alto e quem o recebe?
6. Quantos funcionários estão no departamento de **Marketing**?
7. Qual é a idade média dos funcionários por departamento?
8. Listar os cargos únicos presentes na base.
9. Criar uma nova coluna **"Tempo na Empresa"** baseada na data de contratação.
10. Listar os **5 funcionários com mais tempo de empresa**.
11. Quantos funcionários têm desempenho avaliado acima de **8**?
12. Qual é o **salário total por departamento**?
13. Listar os **5 funcionários mais jovens**.
14. Existem registros sem salário? Se sim, listá-los.
15. Criar uma nova coluna **"Categoria de Salário"**, classificando:
    - **Baixo**: Salário < 3000
    - **Médio**: 3000 ≤ Salário ≤ 7000
    - **Alto**: Salário > 7000
16. Criar uma nova coluna **"Desempenho Simplificado"**, categorizando a **Avaliação de Desempenho**:
    - **Baixo** (1-3)
    - **Médio** (4-7)
    - **Alto** (8-10)
17. Criar uma nova coluna **"Idade em 5 Anos"**, adicionando 5 anos à idade atual.
18. Quantos funcionários estão na categoria de salário **"Alto"**?
19. Utilizar **dropna()** para excluir registros com valores ausentes e salvar o DataFrame limpo em um novo arquivo CSV.
20. Converter a coluna **"Avaliação de Desempenho"** para o tipo **inteiro** e exibir o DataFrame.

## 🛠 Tecnologias Utilizadas

- 🐍 **Python**
- 📊 **Pandas**

## 🚀 Como Executar

## 1. Instale as dependências necessárias (caso ainda não tenha instalado pandas):

   ```python
   pip install pandas
 ```

✉️ Contato
📧 Email: danydayane2@hotmail.com
🔗 [LinkedIn](https://www.linkedin.com/in/dannyellyqueiroz/)
