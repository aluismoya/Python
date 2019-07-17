tupla = (1,2,3,4,5,6,7,8,9,0)

elemento = tupla[4]
elemento_0 = tupla[-3]
sub = tupla[:9:2]

#tupla[1] = 20

tupla = (1,2,3,4)
uno,dos,tres,cuatro = tupla[0], tupla[1], tupla[2], tupla[3]

tupla = (1,2,3,4,5,6)
uno, dos, tres, *cuatro = tupla
print(tupla)

tupla = (1,2,3,4,5,6)
uno, *dos, cinco, seis = tupla
print(tupla)

print(elemento)
print(elemento_0)
print(sub)


print(uno)
print(dos)
print(tres)
print(cuatro)


tupla = (1, 2, 3, 4, 5, 6)
lista = (10, 20, 30, 40)
tupla2 = (100, 200, 300, 400)

resultado = zip(tupla,lista,tupla2)
resultado = tuple(resultado)
resultadol = list(resultado)
print(resultado)
print(resultadol)



