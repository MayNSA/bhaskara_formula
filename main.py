
# será necessario o uso da biblioteca Math

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de C: "))

# cálculo do delta

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (- b + math.sqrt(delta)) / (2 * a)

    print()
    print("A única raiz é: ", raiz1)

elif delta < 0:
    print()
    print("Está equação não possui raizes reais")

else:
    raiz1 = (- b + math.sqrt(delta)) / (2 * a)
    raiz2 = (- b - math.sqrt(delta)) / (2 * a)

    print()
    print("A primeira raiz é: ", raiz1)
    print("A segunda raiz é: ", raiz2)
