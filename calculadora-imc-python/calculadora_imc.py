# --- MINHAS FUNÇÕES DE CÁLCULO E LÓGICA ---

def calcular_imc(peso, altura):
    """Faz a conta básica: peso dividido pela altura ao quadrado."""
    return peso / (altura ** 2)

def classificar_imc(imc, idade, sexo):
    """
    Aqui separo a lógica por idade (OMS)
    e também coloco os alertas de risco baseados no sexo.
    """
    classificacao = ""
    risco = ""

    # Lógica para ADULTOS (menos de 60 anos)
    if idade < 60:
        if imc < 18.5:
            classificacao = "Baixo peso"
            risco = "Risco de desnutrição."
        elif imc < 25:
            classificacao = "Peso adequado"
            risco = "Risco baixo."
        elif imc < 30:
            classificacao = "Sobrepeso"
            # Diferenciei o risco aqui: Homens tendem a ter mais gordura abdominal
            risco = "Risco moderado." + (" Atenção à gordura visceral." if sexo == "M" else " Atenção ao metabolismo.")
        elif imc < 35:
            classificacao = "Obesidade grau I"
            risco = "Risco alto de doenças cardiovasculares."
        elif imc < 40:
            classificacao = "Obesidade grau II"
            risco = "Risco muito alto, consulte um médico."
        else:
            classificacao = "Obesidade grau III"
            risco = "Risco extremo, consulte um médico urgentemente."

    # Lógica para IDOSOS (60 anos ou mais) - As faixas são diferentes!
    else:
        if imc < 22:
            classificacao = "Baixo peso"
            risco = "Risco elevado de sarcopenia (perda de massa muscular) e quedas."
        elif imc <= 27:
            classificacao = "Peso adequado"
            risco = "Risco baixo (estabilidade clínica)."
        else:
            classificacao = "Sobrepeso / Risco de Obesidade"
            # Aqui eu trato riscos específicos: Homens (hipertensão) e Mulheres (osteoporose)
            if sexo == "F":
                risco = "Risco aumentado de doenças cardiovasculares e osteoporose."
            else:
                risco = "Risco aumentado de doenças cardiovasculares e hipertensão."

    return classificacao, risco

# --- FUNÇÕES DE ENTRADA (VALIDAÇÃO) ---

def ler_valor(msg, tipo=float):
    """Lê o que o usuário digita e garante que não quebre o código."""
    while True:
        try:
            # Já trato se o usuário usar vírgula em vez de ponto
            texto = input(msg).strip().replace(",", ".")
            valor = tipo(texto)
            
            if valor <= 0:
                print("O valor precisa ser maior que zero, né? Tenta de novo.")
                continue
            
            # Se for altura e o usuário digitar 170, eu converto pra 1.70 automaticamente
            if tipo == float and "altura" in msg.lower() and valor > 3:
                valor /= 100
                
            return valor
        except ValueError:
            print("Entrada inválida! Digite um número correto.")

def ler_sexo(msg):
    """Garante que só aceite M ou F (eu converto pra maiúsculo pra não dar erro)."""
    while True:
        sexo = input(msg).strip().upper()
        if sexo in ["M", "F"]:
            return sexo
        print("Ops! Digite apenas 'M' para Masculino ou 'F' para Feminino.")

# --- EXECUÇÃO DO PROGRAMA ---

def main():
    print("="*40)
    print("  CALCULADORA DE IMC (OMS)   ")
    print("="*40)
    
    # Primeiro pego a idade pra saber se sigo com o código
    idade = ler_valor("Sua idade: ", int)
    
    if idade < 18:
        print("\n[!] Esse cálculo é focado em adultos e idosos.")
        print("Para crianças, a tabela de percentil é diferente.")
        return

    # Pego o restante dos dados
    sexo = ler_sexo("Sexo (M/F): ")
    peso = ler_valor("Seu peso (kg): ")
    altura = ler_valor("Sua altura (m): ")

    # Chamo as funções que criei lá em cima
    imc = calcular_imc(peso, altura)
    classificacao, risco = classificar_imc(imc, idade, sexo)

    # Mostro o resultado de forma bem clara, com um resumo do que significa o IMC calculado
    print("\n" + "-"*40)
    print(f" RESULTADO PARA: {idade} anos | {('Homem' if sexo == 'M' else 'Mulher')}")
    print(f" -> Seu IMC é: {imc:.2f}")
    print(f" -> Classificação: {classificacao}")
    print(f" -> Alerta de Saúde: {risco}")
    print("-"*40)
    print(" Lembre-se: O IMC é apenas um indicador. Consulte um médico!")

if __name__ == "__main__":
    main()