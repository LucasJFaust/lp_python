"""
Elabore um algoritimo que leia o valor de dois números inteiros e a operação aritimética
desejada; calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para
ler qual a operação aritimética escolhida.

Símbolo   Operação Aritimética
   +            Adição
   -           Subtração
   *         Multiplicação
   /            Divisão
"""

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
operador = str(input("Digite um dos operadores a seguir +, -, * ou /: "))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2


print(f"Sua expressão é {n1} {operador} {n2}")

if operador == "+":
    print(f"O resultado da sua expressão de adição é: {soma}")
elif operador == "-":
    print(f"O resultado da sua expressão de subtração é: {subtracao}")
elif operador == "*":
    print(f"O resultado da sua expressão de multiplicação é: {multiplicacao}")
elif operador == "/":
    print(f"O resultado da sua expressão de divisão é: {divisao}")
else:
    print("Você digitou um operador inválido")