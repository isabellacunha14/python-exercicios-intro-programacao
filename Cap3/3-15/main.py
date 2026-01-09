cigarros = int(input("Cigarros por dia: "))
anos = int(input("Anos: "))

total_cigarros = cigarros * 365 * anos
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 1440  # 1440 minutos em um dia

print(dias_perdidos)