"""
Contrua um algoritimo que calcule a média aritimética entre 4 notas
bimestrai quaisquer fornecidas por um aluno.

ex 1:
Agora insire no algoritimo uma avaliação da situação do aluno, onde se a média
for superior ou igual a 7, ele será aprovado.

ex2:
Agora o mesmo problema mas contando com 50 alunos
 e usando uma estrutura de loop com while e um contador."""

contador_alunos = 0

while contador_alunos < 50:
    print(f"\nAluno {contador_alunos + 1}:")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    media_aritmetica = (n1 + n2 + n3 + n4) / 4
    print(f"As notas foram: {n1}, {n2}, {n3}, {n4}")
    print(f"A média aritmética é: {media_aritmetica}")

    if media_aritmetica >= 7:
        print(f"Sua média foi {media_aritmetica}, portanto você foi Aprovado!")
    else:
        print(f"Sua média foi {media_aritmetica}, logo você foi Reprovado!")

    contador_alunos += 1
