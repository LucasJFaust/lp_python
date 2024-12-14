"""
Construa um algoritimo que calcule a média aritimética de um conjunto de números
pares que forem fornecidos pelo usuário. O valor da finalização será a entrada 0.
Observe que nada impede que o usuário forneça quantos números ímpares quiser, com a ressalva
de que eles não poderam ser acumulados.
"""
# declaração de variáveis
# numero = int(input(f" Digite um número inteiro ou 0 para finalizar o programa:"))
# contador = int(0)
# acumulador = 0.0

# #lógica do finalizador
# while numero != 0:
#     if numero % 2 == 0:
#         acumulador = acumulador
#         contador += 1
#         media_aritimetica_n_pares = acumulador / contador
#         print(f"A média aritimética dos números pares digitados é {media_aritimetica_n_pares:.2f}")
#     else:
#         print(f"Você não digitou um número inteiro")

"""
Erros cometidos no meu código acima:

O problema no seu código está relacionado a dois aspectos principais:

Atualização da variável numero:
No loop while, a entrada de um novo número (numero) só ocorre antes de entrar no loop.
Como não há uma nova solicitação dentro do loop, ele continua processando o mesmo número indefinidamente.

Erro no cálculo do acumulador:
Na linha acumulador += acumulador, você está somando o acumulador a ele mesmo em vez de somar o número fornecido.
Isso gera um resultado incorreto para o cálculo da média.
"""

# declaração de variáveis
contador = 0  # Contador para números pares
acumulador = 0.0  # Soma dos números pares

# Lógica do finalizador
while True:
    # Solicita ao usuário um número
    numero = int(input("Digite um número inteiro ou 0 para finalizar o programa: "))

    if numero == 0:  # Verifica o critério de parada
        break  # Sai do loop se o número for 0

    if numero % 2 == 0:  # Verifica se o número é par
        acumulador += numero  # Soma o número par ao acumulador
        contador += 1  # Incrementa o contador de números pares
    else:
        print("Você digitou um número ímpar. Ele será ignorado.")

# Cálculo da média aritmética dos números pares
if contador > 0:
    media_aritimetica_n_pares = acumulador / contador
    print(f"A média aritmética dos números pares digitados é {media_aritimetica_n_pares:.2f}")
else:
    print("Nenhum número par foi digitado.")

