# Calculadora de IMC (OMS) -- Projeto  em Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Projeto%20Acadêmico-blueviolet)

------------------------------------------------------------------------

## Autora

**Dannyelly Queiroz**\
Projeto desenvolvido para fins de estudo, com foco em prática de lógica
de programação, estruturação de código e boas práticas em Python.

------------------------------------------------------------------------

## Objetivo do Projeto

Desenvolver uma aplicação em linha de comando (CLI) capaz de:

- Calcular o Índice de Massa Corporal (IMC)
- Aplicar regras de classificação segundo diretrizes oficiais
- Validar entradas do usuário
- Implementar lógica condicional baseada em idade e sexo
- Organizar o código de forma modular e legível

Este projeto demonstra domínio de fundamentos importantes da programação
em Python e organização de software.

------------------------------------------------------------------------

## Conceitos Aplicados

Durante o desenvolvimento foram aplicados:

- Estrutura condicional (if / elif / else)
- Laços de repetição (while)
- Tratamento de exceções (try / except)
- Funções com responsabilidades bem definidas
- Separação entre lógica de negócio e entrada de dados
- Validação e sanitização de inputs
- Normalização automática de unidades
- Formatação de saída para melhor experiência do usuário

------------------------------------------------------------------------

## Arquitetura do Código

O sistema foi dividido em camadas funcionais:

### 1️⃣ Camada de Cálculo

`calcular_imc(peso, altura)`\
Responsável apenas pelo cálculo matemático:

IMC = peso / (altura²)

Essa separação facilita manutenção e testes futuros.

------------------------------------------------------------------------

### 2️⃣ Camada de Regra de Negócio

`classificar_imc(imc, idade, sexo)`

Implementa:

- Classificação diferente para adultos (\< 60 anos)
- Classificação específica para idosos (≥ 60 anos)
- Alertas de risco personalizados por sexo

Regras utilizadas:

#### Adultos -- Diretrizes OMS

| IMC            | Classificação        |
|----------------|----------------------|
| < 18.5         | Baixo peso           |
| 18.5 – 24.9    | Peso adequado        |
| 25 – 29.9      | Sobrepeso            |
| 30 – 34.9      | Obesidade Grau I     |
| 35 – 39.9      | Obesidade Grau II    |
| ≥ 40           | Obesidade Grau III   |

#### Idosos – Referência SISVAN

| IMC        | Classificação                          |
|------------|----------------------------------------|
| < 22       | Baixo peso                             |
| 22 – 27    | Peso adequado                          |
| > 27       | Sobrepeso / Risco de obesidade         |

### 3️⃣ Camada de Entrada e Validação

`ler_valor(msg, tipo=float)`

- Garante que o valor seja numérico
- Impede valores negativos ou zero
- Converte vírgula em ponto decimal
- Converte altura digitada em centímetros automaticamente para metros

`ler_sexo(msg)`

- Restringe entrada para M ou F
- Padroniza para letras maiúsculas

------------------------------------------------------------------------

### 4️⃣ Orquestração

`main()`

- Controla o fluxo do programa
- Interrompe execução para menores de 18 anos
- Exibe relatório final formatado

------------------------------------------------------------------------

## 🔎 Diferenciais Técnicos

- Conversão automática de unidade (cm → m)
- Validação robusta contra entradas inválidas
- Segmentação de lógica por faixa etária
- Código organizado e modular
- Estrutura preparada para futuras evoluções (API, interface gráfica,
    testes)

------------------------------------------------------------------------

## Exemplo de Execução

``` text
CALCULADORA DE IMC (OMS)

Sua idade: 32
Sexo (M/F): F
Seu peso (kg): 63
Sua altura (m): 163

RESULTADO PARA: 32 anos | Mulher
-> Seu IMC é: 23.71
-> Classificação: Peso adequado
-> Alerta de Saúde: Risco baixo.
```

------------------------------------------------------------------------

## Possíveis Evoluções Futuras

- Implementação de testes automatizados (pytest)
- Transformação em API REST (FastAPI ou Flask)
- Interface gráfica (Tkinter ou PyQt)
- Interface Web
- Containerização com Docker
- Integração com banco de dados

------------------------------------------------------------------------

## Tecnologias Utilizadas

-Python 3
-Execução via terminal (CLI)

------------------------------------------------------------------------

## Observação

O IMC é um indicador populacional e não substitui avaliação médica
profissional.

