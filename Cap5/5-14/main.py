cont = 0
soma = 0
while True:
    n = int(input("Digite um numero inteiro: "))
    if n == 0:
        break
    soma += n
    cont += 1
media = soma / cont
print("quantidade de numeros =", cont, "\nsoma =", soma, "\nmedia =", media)