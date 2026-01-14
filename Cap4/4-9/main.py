salario = float(input("Salario: "))
casa = float(input("Casa: "))
anos = int(input("Anos a pagar: "))

meses = anos * 12
parcela = casa /meses
limite = salario * 0.30

print(f"Valor da parcela mensal: R$ {parcela:.2f}")
print(f"Limite de 30% do salário: R$ {limite:.2f}")

if parcela < limite:
    print("Emprestimo aprovado!")
else:
    print("Emprestimo não aprovado!")
