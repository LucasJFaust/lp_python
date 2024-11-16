"""
Contrua um algoritimo que calcule a média aritimética de 50 alunos

ex3: Adicionando agora o calculo da média anual dos alunos usando
um acumulador para fazer a soma.
"""

# Declaração e inicialização das variáveis
ma = 0.0    # Média anual de um aluno
acm = 0.0   # Acumulador das médias
mat = 0.0   # Média anual da turma
con = 0     # Contador de alunos

# Loop para processar as médias de 50 alunos
while con < 50:
    # Leia MA
    ma = float(input("Digite a média anual do aluno: "))

    # Acumula MA em Acm
    acm = acm + ma

    # Incrementa o contador
    con = con + 1

# Calcula a média anual da turma
mat = acm / 50

# Escreve o resultado
print("Média anual da turma =", mat)

