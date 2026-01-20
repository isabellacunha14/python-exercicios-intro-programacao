a = int(input("Digite o dividendo: "))
b = int(input("Digite o divisor: "))

resto = a

while resto >= b:
    resto = resto - b

print(f"Resto da divisão: {resto}")

