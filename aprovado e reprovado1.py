aluno = input("Digite o nome do aluno:")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2)/2

if media == 10:
  print("Aprovado com DIstinção!")

elif media >= 7:
  print("Você está aprovado!")

else:
  print("Você foi reprovado!")