
def crear_usuario(nombre, apellido, edad):
    return {
        'nombre' : nombre,
        'apellido': apellido,
        'nombre_completo' : "{} {}".format(nombre, apellido),
        'edad':edad
    }

codi = crear_usuario("Angel", "Luis",43)

print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])




def crear_usuario_2(nombre='', apellido='', edad=45):
    return {
        'nombre' : nombre,
        'apellido': apellido,
        'nombre_completo' : "{} {}".format(nombre, apellido),
        'edad':edad
    }

codi = crear_usuario_2()

print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])
