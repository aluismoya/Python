def saluda():
    print("Hola Mundo!")
saluda()

def crear_mensaje(nombre):
    mensaje = "Hola {}, bienvenido al curo de python3".format(nombre)
    return mensaje

nuevo_mensaje = crear_mensaje("Angel")
print(nuevo_mensaje)

def suma(val1, val2, val3):
    return val1+val2+val3

def obtener_curso():
    return "Curso de Python", "Basico", 3.6

resultado = suma(10,20,30)
print(resultado)

curso, nivel, version = obtener_curso()
print(curso, nivel, version)
