salario = float(input("Digite seu salario"))

if salario > 1250.00:
    aumento = salario * 0.10
if salario <= 1250.00:
    aumento = salario * 0.15

print("Aumento: ", aumento)