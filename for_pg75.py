"""
Repetiçâo com variável de controle

Nas estruturas de repetição (while - enquanto) sabemos que um determinado caso será executado
enquanto um condição for satisfeita  ou até que uma condição seja satisfeita mas repetida. 

A estrutura do for (para) é diferente, já que sempre repete a execução do bloco um número predeterminado
de vezes, pois ela não prevê uma condição e possui limites fixos.

"""

# Estrutura básica do for
print("Contando de 1 a 5:")
for i in range(1, 6):  # range(start, stop) gera números de start até stop-1
    print(f"Número: {i}")

"""
Explicação da Estrutura

for Loop:
O for percorre uma sequência de valores, como números gerados pela função range.

range(start, stop):
Gera uma sequência de números:
start: O valor inicial (inclusivo).
stop: O valor final (exclusivo, ou seja, não será incluído na sequência).

Variável i:
Em cada iteração, i assume o próximo valor da sequência gerada por range.
"""

# Iterando com range e Passo
print("Contando de 0 a 10, pulando de 2 em 2:")
for i in range(0, 11, 2):  # range(start, stop, step)
    print(i)

# Iterando Sobre uma String
palavra = "Python"
print("Letras da palavra:")
for letra in palavra:
    print(letra)
