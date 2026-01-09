salario = float(input("Digite seu salario: "))
aumento = float(input("Digite seu aumento (em porcentagem) : "))

valor_aumento = salario * aumento / 100
novo_salario = salario + valor_aumento

print(valor_aumento)
print(novo_salario)