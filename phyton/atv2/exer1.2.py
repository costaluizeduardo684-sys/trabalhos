import random

lista = []

for i in range(10):
    lista.append(random.randint(1, 100))

maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("Lista:", lista)
print("Maior:", maior)
print("Menor:", menor)
