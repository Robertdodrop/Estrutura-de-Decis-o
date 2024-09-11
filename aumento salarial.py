salario = float(input("Adicione o salario do colaborador: "))

if salario <= 280:
    adicional = 20
elif salario <= 700:
    adicional = 15
elif salario <= 1500:
    adicional = 10
else:
    adicional = 5

aumento = salario * (adicional / 100)
novo_salario = salario + aumento


print(f"Salário antes do reajuste: R$ {salario}")
print(f"Percentual de aumento aplicado: {adicional}%")
print(f"Valor do aumento: R$ {aumento:}")
print(f"Novo salário, após o aumento: R$ {novo_salario:}")