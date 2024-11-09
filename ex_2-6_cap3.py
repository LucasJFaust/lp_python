"""
Escreva um algoritimo que leia o código de um determinado produto e
mostre a sua classificação. Utilize a seguinte tabela como referência:

Código             Classificação
1                Alimento não perecível
2, 3 ou 4        Alimento perecível
5 ou 6           Vestuário
7                Higiene pessoal
8 até 15         Limpeza e utensílios domésticos
Qualquer         código  Inválido
"""

codigo = int(input("Digite o código do Produto: "))

print(f"O Código do Produto é: {codigo}")

if codigo == 1:
    print(f"A classificação é Alimento não perecível")
elif codigo >= 2 and codigo <= 4:
    print(f"A classificação é Alimento perecível")
elif codigo == 5 or codigo == 6:
    print(f"A classificação é Vestuário")
elif codigo == 7:
    print(f"A classificação é Higiene pessoal")
elif codigo >= 8 and codigo <= 15:
    print(f"A classificação é Limpeza e utensílios domésticos")
else:
    print("Código  Inválido")