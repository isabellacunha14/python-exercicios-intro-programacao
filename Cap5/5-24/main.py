n = int(input("Digite a quantidade de números primos: "))

contador = 0      # quantos primos já foram encontrados
numero = 2        # primeiro número a ser testado

while contador < n:
    divisor = 2
    eh_primo = True

    while divisor < numero:
        if numero % divisor == 0:
            eh_primo = False
            break
        divisor += 1

    if eh_primo:
        print(numero)
        contador += 1

    numero += 1
