def calcular_imc(peso, altura):
    """Calcula o IMC a partir do peso e altura."""
    return peso / (altura ** 2)

def classificar_imc(imc, idade, sexo):
    """
    Classifica o IMC e indica risco de saúde.
    Adultos (<60 anos) e idosos (>=60 anos) têm faixas diferentes.
    Sexo influencia o risco em idosos.
    """
    risco = ""
    if idade < 60:  # Adultos
        if imc < 18.5:
            classificacao = "Baixo peso"
            risco = "Risco de desnutrição"
        elif 18.5 <= imc < 25:
            classificacao = "Peso adequado"
            risco = "Risco baixo"
        elif 25 <= imc < 30:
            classificacao = "Sobrepeso"
            risco = "Risco moderado de doenças cardiovasculares"
        elif 30 <= imc < 35:
            classificacao = "Obesidade grau I"
            risco = "Risco alto de doenças cardiovasculares"
        elif 35 <= imc < 40:
            classificacao = "Obesidade grau II"
            risco = "Risco muito alto de doenças cardiovasculares e diabetes"
        else:
            classificacao = "Obesidade grau III"
            risco = "Risco extremo de doenças crônicas"
    else:  # Idosos
        if imc < 22:
            classificacao = "Baixo peso / risco de sarcopenia"
            risco = "Risco elevado de fraqueza muscular e quedas"
        elif 22 <= imc <= 27:
            classificacao = "Peso adequado"
            risco = "Risco baixo"
        else:
            classificacao = "Sobrepeso / risco de obesidade"
            risco = "Risco aumentado de doenças cardiovasculares"
            if sexo == "F":
                risco += " e osteoporose"
            else:
                risco += " e hipertensão"

    return classificacao, risco

def ler_valor(msg, tipo=float):
    """Lê o valor do usuário, substitui vírgula por ponto e valida se é positivo."""
    while True:
        try:
            valor = tipo(input(msg).strip().replace(",", "."))
            if valor <= 0:
                print("Valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Digite novamente.")

def ler_sexo(msg):
    """Lê o sexo do usuário, aceitando 'M' ou 'F'."""
    while True:
        sexo = input(msg).strip().upper()
        if sexo in ["M", "F"]:
            return sexo
        print("Entrada inválida. Digite 'M' para masculino ou 'F' para feminino.")

def main():
    print("=== INFORMAÇÕES PARA CÁLCULO DO IMC ===")
    
    idade = int(ler_valor("Digite sua idade (anos): ", int))
    
    # Verifica se é criança/adolescente
    if idade < 18:
        print("O cálculo de IMC não é recomendado para crianças e adolescentes.")
        return
    
    sexo = ler_sexo("Digite seu sexo (M/F): ")
    peso = ler_valor("Digite seu peso (kg): ")
    altura = ler_valor("Digite sua altura (m): ")

    imc = calcular_imc(peso, altura)
    classificacao, risco = classificar_imc(imc, idade, sexo)

    print("\n=== RESULTADO ===")
    print(f"Idade: {idade} anos | Sexo: {sexo}")
    print(f"Peso: {peso} kg | Altura: {altura} m")
    print(f"IMC: {imc:.2f} -> Classificação: {classificacao}")
    print(f"Risco de saúde: {risco}")

if __name__ == "__main__":
    main()
