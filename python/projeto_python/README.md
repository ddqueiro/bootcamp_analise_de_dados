# Projeto de Análise e Gerenciamento de Funcionários

Este projeto tem como objetivo desenvolver um sistema para gerenciamento de dados de funcionários de uma empresa fictícia, com foco em análise de dados e otimização de informações. A aplicação permite registrar, atualizar, listar e excluir dados de funcionários, com um forte foco na validação das entradas e manipulação das informações de forma eficiente. Este projeto foi desenvolvido com Python e foi utilizado como uma prática para aplicar os conceitos de manipulação de dados.

## Objetivo do Projeto

O objetivo principal deste projeto é fornecer uma ferramenta que permita o gerenciamento e análise de dados relacionados aos funcionários de uma empresa. Ele abrange funcionalidades que ajudam a organizar e validar as informações essenciais, como:

- Nome
- Cargo
- Idade
- Escolaridade
- Salário
- Localização (Cidade e Estado)
- E-mail

Além disso, o sistema oferece a possibilidade de gerar relatórios e executar análises sobre as informações coletadas, permitindo um melhor entendimento sobre a composição dos funcionários da empresa.

## Funcionalidades

- **Cadastro de Funcionários:** Adiciona novos funcionários ao sistema com todos os dados necessários.
- **Atualização de Dados:** Permite que os dados de um funcionário sejam atualizados com base em um identificador único (ID).
- **Listagem de Funcionários:** Exibe uma lista de todos os funcionários cadastrados.
- **Remoção de Funcionários:** Exclui um funcionário do sistema utilizando seu ID.
- **Validação de Dados:** As entradas do usuário são validadas para garantir que as informações fornecidas sejam corretas e não contenham erros (por exemplo, salário como número positivo e e-mail com formato válido).

## Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando a linguagem Python, com foco no uso de listas e dicionários para armazenamento e manipulação dos dados dos funcionários. Não foram usadas bibliotecas externas para análise de dados, mantendo o foco em operações simples com a linguagem.

## Como Funciona

1. **Entrada de Dados:** O sistema coleta informações sobre os funcionários, como nome, idade, cargo, salário, cidade, estado e e-mail, através de um menu interativo.
2. **Armazenamento:** Os dados são armazenados em uma lista de dicionários, onde cada dicionário contém as informações de um único funcionário.
3. **Validação:** O sistema valida as entradas, como garantir que o salário seja um número positivo e o e-mail tenha o formato correto.
4. **Menu de Ações:** O usuário pode acessar um menu para escolher a ação desejada (adicionar, atualizar, listar ou remover funcionários).
