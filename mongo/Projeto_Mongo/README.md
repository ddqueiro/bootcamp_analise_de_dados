# 🚗 Gerenciamento de Aluguéis de Carros com MongoDB

Este projeto tem como objetivo gerenciar os dados de uma locadora de veículos utilizando **MongoDB** e **Python (Pandas e PyMongo)**. Ele realiza a inserção, consulta e análise de dados referentes aos aluguéis, clientes e veículos.

## 📌 Tecnologias Utilizadas

- **Python** 🐍
- **MongoDB Atlas** 🍃
- **PyMongo** 🔗
- **Pandas** 📊
- **Google Colab** ☁️

## 📂 Estrutura do Projeto

1. **Conexão com o MongoDB Atlas** utilizando `MongoClient`
2. **Carregamento dos dados** de diferentes coleções a partir de arquivos CSV
3. **Inserção de dados** nas coleções do MongoDB (`aluguel`, `carro`, `cliente`, `marca`)
4. **Consultas no MongoDB** utilizando PyMongo:
   - Operadores de comparação (`$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`)
   - Operadores de verificação (`$exists`, `$type`)
   - Operadores lógicos (`$and`, `$or`)
   - Estágios de agregação (`$group`, `$sum`, `$mean`, `$lookup`, `$unwind`, `$project`, `$match`)
5. **Geração de relatórios** como:
   - Modelos mais alugados
   - Clientes que mais alugaram carros
   - Análise dos preços dos veículos
   - Relatórios combinando clientes e veículos alugados

## 🔧 Configuração e Execução

1. **Clone o repositório**
   ```python
   git clone https://github.com/seuusuario/repositorio.git

#Instale as dependências
 ```python

pip install pymongo pandas
```

Execute o script no Google Colab ou localmente para interagir com o MongoDB.

