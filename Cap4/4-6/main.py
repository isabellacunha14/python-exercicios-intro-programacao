distancia = float(input("Digite a distancia percorrida"))

if distancia <= 200:
    print("Preço da passagem: ", (distancia * 0.5))
else:
    print("Preço da passagem: ", (distancia * 0.45))