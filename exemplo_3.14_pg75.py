# Inicializaçâo das variáveis

qtd_de_vinhos = 0
qtd_vinho_tinto = 0
qtd_vinho_branco = 0
qtd_vinho_rose = 0


while True:
    # Solicita o tipo do vinho
    tipo_vinho = str(input("Digite T para Tinto, B para branco, R para rose e F para finalizar: ").upper())

    # Verifica a condiçâo de saída
    if tipo_vinho == "F":
        break

    # Verifica se o tipo do vinho é válido e conta o total de vinhos
    if tipo_vinho == "T" or tipo_vinho == "B" or tipo_vinho == "R":
        qtd_de_vinhos += 1

        if tipo_vinho == "T":
            qtd_vinho_tinto += 1
        elif tipo_vinho == "B":
            qtd_vinho_branco += 1
        elif tipo_vinho == "R":
            qtd_vinho_rose += 1
    else:
        print("Você digitou um valor inválido")

# Calculo da % de cada vinho
if qtd_de_vinhos > 0:
    perc_vinho_tinto = (100 * qtd_vinho_tinto) / qtd_de_vinhos
    perc_vinho_branco = (100 * qtd_vinho_branco) / qtd_de_vinhos
    perc_vinho_rose = (100 * qtd_vinho_rose) / qtd_de_vinhos

# Exibe os resultados
    print(f"\nNo estoque temos um total de {qtd_de_vinhos} vinhos:")
    print(f"{perc_vinho_tinto:.2f}% são de vinhos tintos, que representam {qtd_vinho_tinto}")
    print(f"{perc_vinho_branco:.2f}% são de vinhos brancos, que representam {qtd_vinho_branco}")
    print(f"{perc_vinho_rose:.2f}% são de vinhos roses, que representam {qtd_vinho_rose}")
else:
    print("\nNenhum vinho foi contabilizado.")

