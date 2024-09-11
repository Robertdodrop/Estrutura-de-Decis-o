valor1 = float(input("digite o preco do primeiro produto: "))
valor2 = float(input("digite o preco do segundo produto: "))
valor3 = float(input("digite o preco do terceiro produto: "))

mais_barato = valor1

if valor2 < mais_barato:
    mais_barato = valor2
if valor3 < mais_barato:
    mais_barato = valor3

print("o produto mais barato custa:", mais_barato)