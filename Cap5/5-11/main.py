deposito = float(input("Digite o depósito inicial: "))
taxa = float(input("Digite a taxa de juros mensal (%): "))

saldo = deposito
mes = 1

while mes <= 24:
    saldo = saldo + (saldo * taxa / 100)
    print(f"Mês {mes}: R$ {saldo:.2f}")
    mes = mes + 1

ganho = saldo - deposito

print("\nTotal ganho com juros em 24 meses: R$ {:.2f}".format(ganho))

