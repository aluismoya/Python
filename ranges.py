
for valor in range(10):
    print(valor)

print(" ")

for valor in range(1, 20):
    print(valor)

for valor in range(-10, 11):
    print(valor)

lista = [1,2,3,4,5,6]
for valor in range( len(lista) ) :
    print("indice", valor, "valor", valor)


lista = [1,2,3,4,5,6]
for indice, valor in enumerate(lista):
    print("Indice:", indice, "valor", valor)


