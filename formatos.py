
texto = "curso de Python 3"

resultado = texto.capitalize()

resultado2 = texto.swapcase()


resultado3 = texto.upper()

print(resultado)

print(resultado2)

print(resultado3)

print(resultado.isupper())

print(resultado.islower())


texto10 = "curso de Python 3, Python basico"

resultado10 = texto10.strip()

print(resultado10)


curso = "Python"
version = "3"

resultado = "Curso de %s %s" %(curso, version)
resultado11 = "Curso de {a} {b}".format(a=curso, b=version)" 

print(resultado)
print(resultado11)


