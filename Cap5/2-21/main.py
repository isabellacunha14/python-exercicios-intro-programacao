while True:
    valor = float(input("Digite o valor a pagar (0 para sair): "))

    if valor == 0:
        break

    apagar = int(round(valor * 100))

    cedulas = [5000, 2000, 1000, 500, 100, 50, 10, 5, 2, 1]

    for atual in cedulas:
        quantidade = 0

        while apagar >= atual:
            apagar -= atual
            quantidade += 1

        if quantidade > 0:
            print(f"{quantidade} cedula(s) de R${atual / 100:.2f}")

    print("-" * 30)

