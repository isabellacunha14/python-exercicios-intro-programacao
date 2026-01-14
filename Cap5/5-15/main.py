compra = 0
while True:
    cod = input("Codigo: ")
    qtd = int(input("Quantidade: "))

    if cod == "0":
        break
    elif cod == "1":
        compra += (qtd * 0.5)

    elif cod == "2":
        compra += (qtd)

    elif cod == "3":
        compra += (qtd*4)

    elif cod == "5":
        compra += (qtd*7)

    elif cod == "9":
        compra += (qtd*8)

    else:
        print("Codigo invalido")

print(compra)