a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

resultado = 0
contador = 0

while contador < b:
    resultado = resultado + a
    contador = contador + 1

print("Resultado da multiplicação:", resultado)
