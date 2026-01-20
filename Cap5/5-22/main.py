while True:
    print("\nMENU")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Programa encerrado.")
        break

    numero = int(input("Digite um número: "))

    i = 1
    while i <= 10:
        if opcao == 1:
            print(f"{numero} + {i} = {numero + i}")
        elif opcao == 2:
            print(f"{numero} - {i} = {numero - i}")
        elif opcao == 3:
            print(f"{numero} x {i} = {numero * i}")
        elif opcao == 4:
            print(f"{numero} / {i} = {numero / i}")
        else:
            print("Opção inválida.")
            break

        i += 1
