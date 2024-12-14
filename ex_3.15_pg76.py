"""
Voltando ao cálculo da média aritimética de uma turma fixa de 50 alunos,
resolvendo o problema com a repetição for - para teríamos:
"""

# Inicialização das Variáveis
acumulador = 0.0  # Soma das médias
media_anual = 0.0  # Média anual da turma

# Loop para processar as médias de 50 alunos
for aluno in range(1, 51):  # De 1 a 50 (inclusive)
    media = float(input(f"Digite a média anual do aluno {aluno}: "))  # Solicita a média do aluno
    acumulador += media  # Soma a média ao acumulador

# Calcula a média da turma
media_anual = acumulador / 50

# Exibe o resultado
print(f"Média anual da turma = {media_anual:.2f}")

