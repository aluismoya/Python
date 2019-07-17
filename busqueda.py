mensaje = "Este es un texto un poco grande en cuanto a longitud de caracters se refiere"

resultado = mensaje.count("z")
resultado2 = "testo" in mensaje
resultado3 = "testo" not in mensaje
resultado4 = mensaje.find("texto")


resultado5 = mensaje[resultado: resultado + len("texto") ]

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)




resultado = mensaje[resultado: resultado + len("texto") ]
print(resultado)


resultado = mensaje.find("codigo")
print(resultado)


resultado = mensaje.starttswith("Este")
print(resultado)

resultado = mensaje.endswith("e")
print(resultado)