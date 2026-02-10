def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc, idade):
    if idade < 60:
        if imc < 18.5: return "Baixo peso"
        elif 18.5 <= imc < 25: return "Peso adequado"
        elif 25 <= imc < 30: return "Sobrepeso"
        else: return "Obesidade"
    else:
        if imc < 22: return "Baixo peso"
        elif 22 <= imc <= 27: return "Peso adequado"
        else: return "Sobrepeso"

def ler_valor(msg, tipo=float):
    while True:
        try:
            valor = tipo(input(msg).replace(",", "."))
            if valor <= 0: continue
            return valor
        except ValueError:
            print("Valor inválido.")

def main():
    print("=== INFORAMAÇÕES PARA CÁLCULO DO IMC ===")
    idade = ler_valor("Digite sua idade: ", int)
    peso = ler_valor("Digite seu peso (kg): ")
    altura = ler_valor("Digite sua altura (m): ")
    imc = calcular_imc(peso, altura)
    print(f"Resultado: {classificar_imc(imc, idade)} (IMC: {imc:.2f})")

if __name__ == "__main__":
    main()