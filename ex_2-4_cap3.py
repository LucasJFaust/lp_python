h = float(input("Digite a sua altura aqui: "))
s = str(input("Digite o seu sexo M ou F: "))

p_ideal_m = (72.7 * h) - 58
p_ideal_f = (62.1 * h) - 44,7

if s == "M":
    print(F"Seu peso ideal é: {p_ideal_m}")
else:
    print(f"Seu peso ideal é: {p_ideal_f}")