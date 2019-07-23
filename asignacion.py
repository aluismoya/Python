# Python


Ejercicios de estructuras Python
Abrir temario playlist_play
Next
Lo lees en 1 Min.

Los siguientes, son una serie de ejercicios que tienen como finalidad el que tu practiques los conocimientos adquiridos a lo largo de estos bloques.

Dado un diccionario, el cual almacena las calificaciones de un alumno, siendo las llaves los nombres de las materia y los valores las calificación, mostrar en pantalla el promedio del alumno.
Ejemplo: calificaciones = {calculo:10, dibujo:5}

A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio.

Crear una lista la cual almacene 10 números positivos ingresados por el usuario, mostrar en pantalla: la suma de todos los números, el promedio, el número mayor y el número menor.

Dado una lista de frases ingresadas por el usuario, mostrar en pantalla todas aquellas que sean palíndromo.

Mostrar en pantalla la palabra que más se repita junto con la cantidad de veces que lo hace del capituló número uno de Frankenstein

Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde en el abecedario y mostrar el nuevo string en pantalla. (Los espacios no se remplazan) . Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)

Mostrar en pantalla la cantidad de vocales que existe en una frase dada por el usuario.

Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.

Ejemplo : 'Hola Mundo' salida : o=2, a=3, u=1

Eliminar todas las vocales de una frase dado por el usuario y mostrar el nuevo string en pantalla.

Listar todos los números pares del 0 al 100

Funciones Lambda:

sin_parametros = lambda : True

con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

con_asterisco = lambda *args : args[0]

con_doble_asterisco = lambda **kwargs : args[0]

con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)

Funcion map

En Python, la función map nos permite aplicar una función sobre los items de un objeto iterable (lista, tupla, etc...).

map(function, objeto iterable)

La función retornará un objeto map que posteriormente podemos convertir a una lista o tupla.

def cuadrado(numero):
 return numero * numero

lista = [1,2,3,4,5]
resultado = map(cuadrado, lista)

lista_resultado = list(resultado)
print(lista_resultado)

Es posible utilizar map junto con una función lambda. En lo personal considero esta la mejor opción.


lista = [1,2,3,4,5]
resultado = map(lambda numero: numero * numero , lista)

lista_resultado = list(resultado)
print(lista_resultado)

Documentacion de de las Funciones

Documentación de las funciones
Abrir temario playlist_play
Next
Lo lees en 1 Min.

Cómo mencionamos anteriormente, una vez que nosotros definimos una función, podemos llamarla n cantidad de veces, inclusive, fuera de nuestro script, cómo lo veremos más adelante (módulos y paquetes) es por ello que una muy buena practica de programación es documentar nuestras funciones.

Para que nosotros podamos documentar una función lo haremos mediante un comentario, comentario, el cual debe de encontrarse dentro de la función y utilizando triples comillas dobles, cómo podemos observar en el siguiente ejemplo.

def mi_funcion(*args):
  """Esta es la documentación de mi_función"""
  print(args)
Recordemos que al utilizar triples comillas dobles podemos colocar un comentario con saltos de línea.

Podemos trabajar con la documentación a través de su atributo ____doc____

print(mi_funcion.__doc__)



Ahora veamos un ejemplo en el cual podemos sacar provecho a nuestra documentación.

def suma(a, b):
  """Función suma"""
  return a + b

def resta(a, b):
  """Función resta"""
  return a - b

opciones = {'a' : suma, 'b': resta}
print("Ingrese la opción deseada")

for opcion, funcion in opciones.items():
  mensaje = '{}) {}'.format(opcion, funcion.__doc__)
  print(mensaje)

opcion = input("Opción : ")
Almacenamos las funciones dentro de nuestro diccionario, posteriormente iteramos los elementos del diccionario y en cada iteración imprimimos la documentación.
