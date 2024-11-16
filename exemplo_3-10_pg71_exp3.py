"""
Contrua um algoritimo que calcule a média aritimética de 50 alunos

ex4: Aplicando o conceito de critério de parada. Nesta lógica
não importa a quantidade de alunos.
"""

# # inicialização das variáveis
# ma = 0.0  # média anual de um dado aluno
# acm = 0.0  # acumulador
# mat = 0.0  # média anual da turma
# con = 0  # contador

# # estrutura de repetição com finalizador
# while ma != -1:  # teste da condição de parada
#     ma = float(input("digite a média anual do aluno (ou -1 para finalizar): "))  # lê a média anual

#     if ma != -1:  # evita acumular o valor finalizador
#         acm += ma  # soma a média ao acumulador
#         con += 1  # incrementa o contador

# # verifica se houve pelo menos uma execução
# if con > 0:
#     mat = acm / con  # calcula a média anual da turma
#     print(f"média anual da turma: {mat:.2f}")
# else:
#     print("nenhuma média válida foi inserida.")

"""
 No código acima, havia um problema na lógica que fazia com que o loop não parasse de solicitar entradas, mesmo quando
 o critério de parada -1 fosse digitado. Isso acontecia porque o valor de ma era atualizado depois do teste da condição no while,
 o que causava um comportamento inesperado.
"""


# inicialização das variáveis
acm = 0.0  # acumulador
mat = 0.0  # média anual da turma
con = 0  # contador

# estrutura de repetição com finalizador
while True:  # loop infinito até que o usuário digite -1
    entrada = input("digite a média anual do aluno (ou -1 para finalizar): ")  # lê a entrada como string

    # verifica se o usuário digitou -1
    if entrada == "-1":
        break  # sai do loop

    # tenta converter a entrada para float
    ma = float(entrada)
    acm += ma  # soma a média ao acumulador
    con += 1  # incrementa o contador

# verifica se houve pelo menos uma execução
if con > 0:
    mat = acm / con  # calcula a média anual da turma
    print(f"média anual da turma: {mat:.2f}")
else:
    print("nenhuma média válida foi inserida.")


