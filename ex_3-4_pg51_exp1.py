"""
Contrua um algoritimo que calcule a média aritimética entre 4 notas
bimestrai quaisquer fornecidas por um aluno.
ex 1:
Agora insire no algoritimo uma avaliação da situação do aluno, onde se a média
for superior ou igual a 7, ele será aprovado.
"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a primeira segunda: "))
n3 = float(input("Digite a primeira terceira: "))
n4 = float(input("Digite a primeira quarta: "))
media_aritimetica = (n1 + n2 + n3 + n4) / 4

if media_aritimetica >= 7:
    print(f"Sua média foi {media_aritimetica}, portanto você foi Aprovado!")
else:
    print(f"Sua média foi {media_aritimetica}, logo você foi Reprovado!")