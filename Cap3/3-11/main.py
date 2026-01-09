preco = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite desconto (em porcentagem) : "))

valor_desconto = preco * desconto / 100
novo_preco = preco - valor_desconto

print(valor_desconto)
print(novo_preco)