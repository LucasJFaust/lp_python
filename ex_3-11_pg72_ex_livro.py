"""
Construa um algoritimo que calcule a média aritimética de um conjunto de números
pares que forem fornecidos pelo usuário. O valor da finalização será a entrada 0.
Observe que nada impede que o usuário forneça quantos números ímpares quiser, com a ressalva
de que eles não poderam ser acumulados.
"""

# declaração de variáveis
contador = int(0)
acumulador = int(0)

n = int(input("Digite um número inteiro (ou 0 para finalizar): "))

while n > 0:
    print(f"Número atual: {n}")
    if n > 0 and n % 2 == 0:
        acumulador = acumulador + n
        contador +=1

    n = int(input("Digite um número inteiro (ou 0 para finalizar): "))

if contador > 0:
    media_n_pares = acumulador / contador
    print(f"Média do conjunto de números pares é: {media_n_pares:.2f}")
else:
    print("Nenhum par foi fornecido")
