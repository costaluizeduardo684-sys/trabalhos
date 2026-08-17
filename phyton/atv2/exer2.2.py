import random

lista = []
PAR = []
IMPAR = []

for i in range(20):
    numero = random.randint(1, 100)
    lista.append(numero)

    if numero % 2 == 0:
        PAR.append(numero)
    else:
        IMPAR.append(numero)

print("Lista:", lista)
print("Pares:", PAR)
print("Ímpares:", IMPAR)
