# imc# Calculadora de IMC com Python

Este repositório contém um script em Python para calcular o Índice de Massa Corporal (IMC) e classificar o resultado segundo os padrões da OMS, considerando adultos e idosos.

---

## Funcionalidades

- Recebe idade, peso e altura do usuário.
- Calcula o IMC utilizando a fórmula:  
  `IMC = peso / (altura ** 2)`
- Classifica o IMC em categorias:
  - Adultos (<60 anos): Baixo peso, Peso adequado, Sobrepeso, Obesidade grau I, II e III.
  - Idosos (>=60 anos): Baixo peso / risco de sarcopenia, Peso adequado, Sobrepeso / risco de obesidade.
- Validação de inputs: garante que os valores digitados sejam positivos e numéricos.

---

## Como usar

1. Clone ou faça download do repositório.
2. Abra o terminal na pasta do projeto.
3. Execute o script:

```bash
python calculadora_imc.py

Autor
Criado por Dannyelly Queiroz