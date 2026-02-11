# Calculadora de IMC com Classificação e Riscos de Saúde

## Descrição
Este projeto é uma calculadora de IMC (Índice de Massa Corporal) feita em Python.  
Ela calcula o IMC com base no peso e altura do usuário, classifica o resultado e indica riscos de saúde específicos considerando idade e sexo.  

- Adultos (18 a 59 anos) e idosos (60 anos ou mais) possuem faixas diferentes de classificação.  
- Crianças e adolescentes (menos de 18 anos) **não devem utilizar o cálculo**, pois o IMC segue padrões diferentes nessa faixa etária.  

## Funcionalidades
- Calcula IMC a partir de peso (kg) e altura (m)  
- Classifica o IMC em categorias de peso  
- Indica risco de saúde relacionado à faixa de IMC, idade e sexo  
- Valida entradas do usuário (não aceita valores negativos ou inválidos)  

## Estrutura do Código

- **calcular_imc(peso, altura)**: retorna o IMC.  
- **classificar_imc(imc, idade, sexo)**: retorna a classificação do IMC e o risco de saúde.  
- **ler_valor(msg, tipo=float)**: lê e valida valores numéricos do usuário.  
- **ler_sexo(msg)**: lê o sexo do usuário, aceitando apenas `M` ou `F`.  
- **main()**: função principal que executa a calculadora.

## Como usar

1. Certifique-se de ter o Python instalado na sua máquina.  
2. Salve o arquivo `imc.py` em uma pasta de sua preferência.  
3. Abra o terminal ou prompt de comando e navegue até a pasta do arquivo.  
4. Execute o código com o comando:  

```bash
python imc.py

Siga as instruções no terminal:


O programa retornará:

- IMC calculado
- Classificação do peso
- Risco de saúde relacionado

Regras de Classificação

## Tabela de Classificação do IMC

### Adultos (18 a 59 anos)

| Faixa de IMC (kg/m²) | Classificação     |Risco de saúde                                           |
|----------------------|-------------------|---------------------------------------------------------|
| < 18.5               | Baixo peso        | Risco de desnutrição                                    |
| 18.5 – 24.9          | Peso adequado     | Risco baixo                                             |
| 25 – 29.9            | Sobrepeso         | Risco moderado de doenças cardiovasculares              |
| 30 – 34.9            | Obesidade grau I  | Risco alto de doenças cardiovasculares                  |
| 35 – 39.9            | Obesidade grau II | Risco muito alto de doenças cardiovasculares e diabetes |
| ≥ 40                 | Obesidade grau III| Risco extremo de doenças crônicas                       |

### Idosos (60 anos ou mais)

| Faixa de IMC (kg/m²) | Classificação                 | Risco de saúde                                                  |
|----------------------|-------------------------------|----------------------------------------------------------------|
| < 22                 | Baixo peso / risco de sarcopenia | Risco elevado de fraqueza muscular e quedas                    |
| 22 – 27              | Peso adequado                  | Risco baixo                                                    |
| > 27                 | Sobrepeso / risco de obesidade | Risco aumentado de doenças cardiovasculares + sexo específico:<br>- F: risco de osteoporose<br>- M: risco de hipertensão |


O cálculo de IMC não é recomendado para menores de 18 anos.

Autor

Criado por Dannyelly Queiroz
