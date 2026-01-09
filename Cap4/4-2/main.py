velocidade = float(input("Digite a velocidade: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Voce foi multado em R$ %.2f" % multa)

if velocidade < 80:
    print("Voce nao foi multado")