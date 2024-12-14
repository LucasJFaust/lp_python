"""
Imagie um brincadeira entre dois colegas, na qual
um pensa um número e o outro deve fazer chutes até acertar
o número imaginado. Como dica, cada tentativa é dito se
o chute foi alto ou baixo. Elabore um algoritimo dentro deste
contexto, que leia o número imaginado e os chutes, ao final mostre
quantas tentativas foram necessárias para descobrir o número
"""

n_de_tentativas = 0
n_pensado = int(input("Pense em um número: "))

while True:
    chute = int(input("Adivinhe o número: "))
    n_de_tentativas += 1
    if chute == n_pensado:
        print(f"Parabéns, você acertou o número pensado {n_pensado}, em {n_de_tentativas} tentativas")
        break
    elif chute < n_pensado:
        print("Valor está inferior ao número pensado")
    else:
        print("Valor está superior ao número pensado")