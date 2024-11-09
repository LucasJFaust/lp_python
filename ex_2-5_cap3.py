"""
Faça um algoritimo que leia o ano de nascimento de uma pessoa, calcule e mostre sua idade e, também verifique e mostre
se ela já tem idade para votar (16 anos ou mais) e para conseguir a carteira de habilitação (18 anos ou mais)
"""
ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = 2024
idade = ano_atual - ano_nascimento

print(f"Você tem {idade} anos.")

if idade >= 18:
    print("Você já pode votar e tirar a carteira de habilitação.")
elif idade >= 16:
    print("Você já pode votar, mas ainda não pode tirar a carteira de habilitação.")
else:
    print("Você ainda não pode votar nem tirar a carteira de habilitação.")



