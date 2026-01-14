deposito_inicial = float(input("Digite o depósito inicial: "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
deposito_mensal = float(input("Digite o valor do depósito mensal: "))

saldo = deposito_inicial
total_depositado = deposito_inicial
mes = 1

while mes <= 24:
    # depósito feito no início do mês
    saldo = saldo + deposito_mensal
    total_depositado = total_depositado + deposito_mensal

    # aplicação dos juros do mês
    saldo = saldo + (saldo * taxa / 100)

    print(f"Mês {mes}: R$ {saldo:.2f}")
    mes = mes + 1

ganho_juros = saldo - total_depositado

print("\nTotal depositado: R$ {:.2f}".format(total_depositado))
print("Total ganho com juros em 24 meses: R$ {:.2f}".format(ganho_juros))

