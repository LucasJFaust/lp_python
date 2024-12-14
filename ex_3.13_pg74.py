"""
Imagie um brincadeira entre dois colegas, na qual
um pensa um número e o outro deve fazer chutes até acertar
o número imaginado. Como dica, cada tentativa é dito se
o chute foi alto ou baixo. Elabore um algoritimo dentro deste
contexto, que leia o número imaginado e os chutes, ao final mostre
quantas tentativas foram necessárias para descobrir o número
"""

# Solicita ao primeiro jogador que insira o número imaginado
numero_imaginado = int(input("Jogador 1, pense em um número (não mostre para o Jogador 2): "))
print("\n" * 50)  # Limpa a tela para que o número não seja visível

# Inicializa o contador de tentativas
tentativas = 0

# Loop para o Jogador 2 adivinhar o número
while True:
    # Solicita o chute do jogador
    chute = int(input("Jogador 2, faça seu chute: "))
    tentativas += 1  # Incrementa o contador de tentativas

    # Verifica o chute
    if chute == numero_imaginado:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s).")
        break  # Sai do loop quando o número é acertado
    elif chute < numero_imaginado:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")
