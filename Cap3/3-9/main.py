dia = int(input("Digite a quantidade de dias: "))
hora = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total_segundos = segundos + (minutos * 60) + (hora * 3600) + (dia * 86400)

print(total_segundos)
