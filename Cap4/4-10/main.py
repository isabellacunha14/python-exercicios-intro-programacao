energia = float(input("Energia consumida: "))
resid = input("Instalação \n R - Residencia \n I - Industria \n C - Comercio \n")

if resid == "R" or resid == "r":
    if energia <= 500:
        preco = energia * 0.40
    else:
        preco = energia * 0.65

if resid == "I" or resid == "i":
    if energia <= 5000:
        preco = energia * 0.55
    else:
        preco = energia * 0.60

if resid == "C" or resid == "c":
    if energia <= 1000:
        preco = energia * 0.55
    else:
        preco = energia * 0.60

print("Preco a pagar: ", preco)