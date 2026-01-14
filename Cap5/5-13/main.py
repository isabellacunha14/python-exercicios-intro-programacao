divida = float(input("Digite o valor inicial da dívida: "))
juros = float(input("Digite a taxa de juros mensal (%): "))
pagamento = float(input("Digite o valor pago por mês: "))

saldo = divida
meses = 0
total_pago = 0

while saldo > 0:
    # aplica juros do mês
    saldo = saldo + (saldo * juros / 100)

    # pagamento mensal
    saldo = saldo - pagamento

    total_pago = total_pago + pagamento
    meses = meses + 1

# cálculo dos juros pagos
total_juros = total_pago - divida

print("\nMeses para quitar a dívida:", meses)
print("Total pago: R$ {:.2f}".format(total_pago))
print("Total pago em juros: R$ {:.2f}".format(total_juros))

