n = int(input("Digite um número inteiro: "))

if n <= 1:
    print("Número não é primo")
else:
    primo = 2
    eh_primo = True

    while primo < n:
        if n % primo == 0:
            eh_primo = False
            break
        primo += 1

    if eh_primo:
        print("Número primo")
    else:
        print("Número não é primo")
