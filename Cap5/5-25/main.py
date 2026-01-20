n = float(input("Digite um número: "))

b = 2.0
p = (b + (n / b)) / 2

while abs(n - (p ** 2)) >= 0.0001:
    b = p
    p = (b + (n / b)) / 2

print(f"Raiz quadrada aproximada: {p}")
