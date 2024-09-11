turno = input("Qual seu turno? Digite 'M' para Matutino, 'V' Para Vespertino ou 'N' para Noturno: ").strip().upper()

if turno == "M":
  print("Bom Dia!")
elif turno == "V":
  print("Boa Tarde!")
elif turno == "N": #Para ser sincero, não sei como isso funcionou, testei, rodou então ta certo s2 (não sabia que dava para por 2 elif)
  print("Boa Noite!")
else:
  print("Turno Invalido")