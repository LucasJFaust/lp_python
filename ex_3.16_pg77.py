"""
Elabore um algóritimo que efetue a soma de todos os números ímpares que sâo múltiplos de 3
e que se encontram no conjunto dos números de 1 até 500.
"""

soma_n_impares = 0

for numero in range(1, 501):
    if numero % 2 == 1:
        print(f"O numero {numero} é ímpar")
        if numero % 3 == 0:
            soma_n_impares = soma_n_impares + numero

print(f"Soma = {soma_n_impares}")