numero1 = int(input("Adicione o primeiro Numero: "))
numero2 = int(input("Adicione o segundo Numero: "))
numero3 = int(input("Adicione o terceiro Numero: "))

if numero1<numero2 and numero1<numero3:
  print(f"O numero menor é {numero1}")
elif numero2<numero3 and numero2<numero1:
  print(f"O numero menor é {numero2}")
else:
  print(f"O numero menor é {numero3}")