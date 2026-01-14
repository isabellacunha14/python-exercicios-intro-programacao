a = int(input("Digite um numero inteiro: "))
b = int(input("Digite outro numero inteiro: "))

print("Operacoes:\n"
      "1 - Soma \n"
      "2 - Subtracao \n"
      "3 - Multiplicacao \n"
      "4 - Divisao \n")
operacao = int(input("Digite uma opcao: "))

if operacao == 1:
      soma = a+b
      print(soma)
if operacao == 2:
      sub = a-b
      print(sub)
if operacao == 3:
      mul = a*b
      print(mul)
if operacao == 4:
      div = a/b
      print(div)